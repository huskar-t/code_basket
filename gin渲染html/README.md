#gin渲染html
####起源
由于项目中使用了压缩中间件并且只能获取到gin.IRouter对象同时不使用静态html文件，将静态页面变成变量后输出，所以无法通过gin.engine加载变量为模板。
####解决
通过template创建模板  
构建render.HTMLProduction  
htmlRender.Instance创建Render实例
```go 
import(
    "github.com/gin-gonic/gin/render"
    "html/template"
)
const INDEX = `<div id="remoteVideos"></div> <br/>`
var templateName = "test"
var pageInstance render.Render
func createPageInstance(){
	pageContent := template.Must(template.New(templateName).Parse(INDEX))
	htmlRender := render.HTMLProduction{Template: pageContent}
	pageInstance = htmlRender.Instance(templateName, map[string]interface{}{})
}
```

使用  
c.Render渲染Render实例
```go 
c.Render(http.StatusOK, pageInstance)
```