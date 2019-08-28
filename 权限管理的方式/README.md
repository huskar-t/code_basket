#权限管理

##权限比较少并且已确定的权限：
参考linux的读写执行权限，规定以二进制方式确定权限
```go 
const (
	ReadWeight = 1 << iota
	UpdateWeight
	WriteWeight
	DeleteWeight
)
func weightAuth(userWeight, targetWeight int) (bool, string) {
	return (userWeight & targetWeight) == targetWeight
}
```
特点：位计算高效,实现简单  
缺陷：权限可读性不高，对复杂权限支持困难

##权限复杂且动态添加
针对模块化的权限设置角色表，用户表与角色表做对应形成用户组。  
角色表可以使用json格式存储每个角色对应功能的权限
```go 
type User struct {
	Id        uint   `gorm:"column:id" form:"id" json:"id" comment:"自增id" sql:"int(11),PRI"`
	Uid       string `gorm:"column:uid" form:"uid" json:"uid" comment:"内部id" sql:"varchar(40)"`
	Account   string `gorm:"column:account;unique_index:set_account" form:"account" json:"account" comment:"账号" sql:"varchar(255),UNI"`
	Password  string `gorm:"column:password" form:"password" json:"password" comment:"密码" sql:"varchar(255)"`
	Secretkey string `gorm:"column:secretkey" form:"secretkey" json:"-" comment:"找回密码用的秘钥" sql:"varchar(255)"`
	IsSuper   string `gorm:"column:is_super" form:"is_super" json:"is_super" comment:"是否是超级用户" sql:"varchar(1)"`
	NickName  string `gorm:"column:nick_name" form:"nick_name" json:"nick_name" comment:"昵称" sql:"varchar(255)"`
	Role      uint    `gorm:"column:role" form:"role" json:"role" comment:"角色id" sql:"int(11)"`
}
type Role struct {
	Id          uint               `gorm:"column:id" form:"id" json:"id" comment:"自增id" sql:"int(11),PRI"`
	Name        string             `gorm:"column:name" form:"name" json:"name" comment:"角色名" sql:"varchar(255)"`
	Description string             `gorm:"column:description" form:"description" json:"description" comment:"描述" sql:"varchar(255)"`
	Ext         string             `gorm:"column:ext" form:"ext" json:"-" comment:"保留字段" sql:"varchar(255)"`
	Permission  *types.StringArray `gorm:"type:json;column:permission" form:"permission" json:"permission" comment:"权限"`
}

type StringArray []string
func (data *StringArray) Scan(val interface{}) (err error) {
	if val == nil {
		return nil
	}
	if payload, ok := val.([]byte); ok {
		var value []string
		err = json.Unmarshal(payload, &value)
		if err == nil {
			*data = value
		}
	}
	return
}
func (data *StringArray) Value() (driver.Value, error) {
	if data == nil {
		return nil, nil
	}
	return json.Marshal([]string(*data))
}
func (data *StringArray) Get() []string {
	if data == nil {
		return nil
	}
	return []string(*data)
}
```
User.Role对应Role.Id  
Role.Permission用字符串数组存储权限  
权限定义为"接口的请求方法_接口"如："get_/api/v1/user"  
通过中间件进行权限检查
```go 
var apiInterfaceAuthCheckMiddleware = apiInterfaceAuthCheck()

func apiInterfaceAuthCheck() gin.HandlerFunc {
	return func(c *gin.Context) {
		user, ok := c.MustGet(gin.AuthUserKey).(*models.User)
		if !ok || user.Uid == "" {
			jsonError(c, "Need Administrator Account")
			return
		}
		method := c.Request.Method
		url := c.Request.URL.Path
		if !user.IsSuperAccount() {
			permissionFunc := strings.ToLower(fmt.Sprintf("%s_%s", method, url))
			haveAuth := models.CheckRolePermission(uint(user.Role), permissionFunc)
			if !haveAuth {
				jsonError(c, "Permission deny")
				return
			}
		}
		c.Next()
	}
}
//model.go
func CheckRolePermission(roleId uint, permissionFunc string)bool{
	if roleId == 0 {
		return false
	}
	mRole := Role{Id: roleId}
	role, err := mRole.One()
	if err != nil {
		return false
	}
	for _,permission := range *role.Permission{
		if strings.HasPrefix(permissionFunc,permission){
			return true
		}
	}
	return false
}
```
特点：灵活，对复杂权限可以动态添加，可读性高  
缺陷：实现复杂，性能损失高