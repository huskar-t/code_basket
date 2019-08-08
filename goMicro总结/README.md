#goMicro框架使用总结
##简介
**多网卡机器就别折腾了！！！**

goMicro框架是golang的微服务框架，支持多种服务发现框架，支持rpc,grpc,http,nats等通信方式且易于扩展。
##选型
>goMicro微服务框架  
consul服务发现  
nats broker  
gin框架  
gorm  
redis缓存  
postgresql持久化数据库
##使用
###封装server
```go
type MicroServer struct {
	Service micro.Service
	cancel  context.CancelFunc
	Name    string
	Version string
}
//创建微服务
func NewMicroServer(name, version string, init func(srv micro.Service) error, opts ...micro.Option) *MicroServer {
	serv := &MicroServer{
		Name:    name,
		Version: version,
	}
	serv.init(opts...)
	if err := init(serv.Service); err != nil {
		panic(err)
	}
	return serv
}

func (serv *MicroServer) init(opts ...micro.Option) {
	ctx, cancel := context.WithCancel(context.Background())
	serv.cancel = cancel

	options := []micro.Option{
		micro.Name(serv.Name),
		micro.Version(serv.Version),
		micro.Context(ctx),
		micro.RegisterTTL(time.Second * 30),
		micro.RegisterInterval(time.Second * 15),
		//serv.Address(":0"),
	}
	for _, o := range opts {
		options = append(options, o)
	}

	serv.Service = micro.NewService(options...)
	serv.Service.Init()
	microClient = serv.Service.Client()
}
//启动微服务
func (server *MicroServer) Run() error {
	return server.Service.Run()
}
```
使用示例
```go
server := service.NewMicroServer("demo.microName", "1.0.0",
    func(microService micro.Service) error {
        //proto_gateway.RegisterGatewayServiceHandler(microService.Server(), new(mqtt.ServiceHandler))
        return nil
    },micro.Metadata(map[string]string{
        "type": "demo",
	}),
)
var g errgroup.Group
g.Go(server.Run)
```
###使用自定义broker
```go
import (
	_ "github.com/micro/go-micro"
	"github.com/micro/go-micro/broker"
	"github.com/micro/go-plugins/broker/nats"
	"os"
)

var (
	Broker broker.Broker
)
func init() {
    log.Println("初始化微服务Broker")

    Broker = nats.NewBroker()

    if err := Broker.Init(broker.Addrs(os.Getenv("MICRO_BROKER_ADDRESS"))); err != nil {
        log.Fatalf("Broker Init error: %v", err)
    }
    if err := Broker.Connect(); err != nil {
        log.Fatalf("Broker Connect error: %v", err)
    }
}

```
注册topic
```go
subscriber, err = Broker.Subscribe(topic, func(p broker.Publication) error {
    fmt.Println("[sub] received message:", string(p.Message().Body), "header", p.Message().Header)
    return nil
})
```
发布消息
```go
topic := "demo"
msg := &broker.Message{
    Header: map[string]string{
        "title": "demo",
    },
    Body: []byte("Hello"),
}
if err := Broker.Publish(topic, msg); err != nil {
    fmt.Println(err.Error())
}
```

###框架内broker
导入
```go
	_ "github.com/micro/go-plugins/broker/nats"
```
定义proto协议
```proto
//siteEvent.proto
syntax = "proto3";
package proto.site.event;
// Event message
message SiteEvent {
	//	命令
	string cmd = 1;
	// siteId
	string site_id = 2;
}
```
生成项目使用的代码  
```protoc --proto_path=. --micro_out=. --go_out=. siteEvent.proto```

注册topic
```go
var microClient = client.NewClient()
type ISiteEvent interface {
	Process (ctx context.Context, event *proto_site_event.SiteEvent) error
}
type SiteEvent struct{}
func (e *SiteEvent) Process(ctx context.Context, event *proto_site_event.SiteEvent) error {
	if event.Cmd == "siteDelete" {
	
	}
	return nil
}
type siteEventHandler struct {
	publisher micro.Publisher
}
func (ph *siteEventHandler) SubEvent(server *MicroServer, event ISiteEvent) error {
    // 会执行event里面全部的方法
    err := micro.RegisterSubscriber(siteTopic, server.Service.Server(), event)
    return err
```
发布
```go 
func (ph *siteEventHandler) RegPublisher() {
    if ph.publisher == nil {
        publisher := micro.NewPublisher(siteTopic, microClient)
        ph.publisher = publisher
    }
}
func (ph *siteEventHandler) Publish(msg proto_site_event.SiteEvent) error {
    if ph.publisher == nil {
        return errors.New(fmt.Sprintf("publisher %s not found", siteTopic))
    }
    err := ph.publisher.Publish(context.Background(), msg)
    return err
```

###web服务(micro+gin)
```go
type httpServerController struct{}
var (
	HttpServer = httpServerController{}
)

func (ctl *httpServerController) RunWebService() error {
	return ctl.Run("v1.httpServer", ctl)
}

func (ctl *httpServerController) Init(router gin.IRouter) {
	api := router.Group("/v1/httpServer")
	api.GET("", ctl.one)
}
func (httpServerController) one(c *gin.Context) {
    return
}
func (ctl *BaseController) Run(serviceName string, controller WebServiceController) error {
	// Create service
	service := web.NewService(
		web.Name("go.micro.api." + serviceName),
		web.Id(uuid.New().String()),
		web.Address(config.ServerAddress),
	)

	if err := service.Init(); err != nil {
		panic(err)
	}
    // 创建gin实例
	router := CreateRouter()
	// 路由
	controller.Init(router)

	// Register Handler
	service.Handle("/", router)
	// Run server
	return service.Run()
}
func CreateRouter() *gin.Engine{
	router := gin.Default()
	//压缩传输
	router.Use(gzip.Gzip(gzip.DefaultCompression))
	//跨域
	corsConfig := cors.DefaultConfig()
	corsConfig.AllowAllOrigins = true
	corsConfig.AllowMethods = []string{"GET", "POST", "PUT", "HEAD", "DELETE"}
	corsConfig.AllowHeaders = []string{"Origin", "Content-Length", "Content-Type", "Authorization", "AccessKey", "X-AccessKey", "X-SiteID"}
	corsConfig.ExposeHeaders = []string{"Authorization"}
	router.Use(cors.New(corsConfig))
	return router
}
```
使用
```go
var g errgroup.Group
g.Go(HttpServer.RunWebService)
```

###TRANSPORT(nats)
proto
```proto
syntax = "proto3";
package proto.rules;

// protoc --proto_path=. --micro_out=. --go_out=. rules.proto
service RuleEngine {
    rpc CreateRule(RuleRequest) returns (Response) {}
}

message Request {
}

message RuleRequest {
    string siteID = 1;
}
message Response {
}

```
客户端
```go
var microClient = client.NewClient()
type TService struct {}
func (tService *TService) getServiceName() string {
	return fmt.Sprintf("demo.microName.%s", "v1")
}
//"T."+method为微服务endpoint即：结构体名+"."+方法名
func (tService *TService) newRequest(method string, req interface{}) client.Request {
	return microClient.NewRequest(tsdbService.getServiceName(), "T."+method, req, client.WithContentType("application/json"))
}
//json传输
type BaseRequest struct {
	SiteID   string `json:"siteID,omitempty"`
}
func (tService *TService) CreateTable(siteID string) error {
	request := tService.newRequest("CreateTable", BaseRequest{SiteID: siteID})
	return microClient.Call(context.TODO(), request, nil)
}
//protobuf传输
func (tService *TService) CreateRule(siteID string) error {
    //调用protobuf接口
	_, err := ruleService.serviceHandler.CreateRule(context.TODO(), &proto_rules.RuleRequest{SiteID: siteID})
	return err
}
```
服务端
```go 
type ServiceHandler struct { }
func (ServiceHandler) CreateRule(ctx context.Context, req *proto_rules.RuleRequest, resp *proto_rules.Response) error {
	return InnerHandler.CreateRule(req.SiteID)
}

type T struct { }
func (T) CreateTable(ctx context.Context, req *rpc_tsdb.BaseRequest, resp *string) error {
	return InnerHandler.CreateTable(req.SiteID)
}
func main() {
	server := service.NewMicroServer("iotopo.rules."+serverID, "1.0.0",
		func(microService micro.Service) error {
		    //注册protobuf接口
			proto_rules.RegisterRuleEngineHandler(microService.Server(), new(ServiceHandler))
			//注册json传输接口
			return micro.RegisterHandler(microService.Server(), new(T))
			return nil
		},
	)
	var g errgroup.Group
	g.Go(server.Run)
}
```

###redis-lua
```go
const (
	// 通配符key获取全部value
	GET_ITEMS = `
		local keys = redis.call("KEYS", KEYS[1])
		local values = {}
		for i = 1 , #keys do
			local value = redis.call("GET",keys[i])
			table.insert(values, value)
		end
		return values
	`
	// 通配符key删除全部value
	DELETE_ITEMS = `
		local keys = redis.call("KEYS", KEYS[1])
		local values = {}
		for i = 1 , #keys do
			local value = redis.call("DEL",keys[i])
		end
	`
)
```
###部署
设置环境变量:  
MICRO_BROKER : nats  
MICRO_REGISTRY : consul  
MICRO_TRANSPORT : nats  


