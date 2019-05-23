#golang添加管理员启动和图标

###工具
go get github.com/akavel/rsrc

###命令
rsrc.exe -arch amd64 -manifest window_administrator.manifest -ico golang.ico -o myapp.syso

###说明
-arch &nbsp;平台  
-manifest  &nbsp;manifest文件，可以添加管理员权限启动  
-ico  &nbsp;图标文件  
-o  &nbsp;目标文件(.syso)

将生成的.syso文件放到项目路径进行build