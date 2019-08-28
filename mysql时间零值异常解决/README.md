#mysql 时间空值异常
golang 的time.Time类型转换到数据库语句时如果为空值则为空串 '0000-00-00 00:00:00' 而从mysq5.7之后sql_mode 默认有NO_ZERO_DATE和NO_ZERO_IN_DATE认为日期 '0000-00-00'

###解决办法：
先查询sql_mod
```sql
select @@global.sql_mode;
```
删除NO_ZERO_DATE和NO_ZERO_IN_DATE

1.修改本次连接的sql_mode
```sql
set sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```
2.修改全局sql_mode
```sql
set sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
```
>* 如果修改全局的sql_mode需要新建连接才会生效，已建立的连接不生效  

3.修改数据库的配置文件

###具体例子：
如果使用mysql的docker镜像则修改配置不是特别方便，采用修改程序的方法，先修改全局的sql_mod再创建连接池
```go 
var mysqlDB *gorm.DB

func init() {

	//init mysql
	conn := fmt.Sprintf("%s:%s@(%s)/%s?charset=%s&parseTime=True&loc=Local", viper.GetString("mysql.user"),
		viper.GetString("mysql.password"), viper.GetString("mysql.addr"), viper.GetString("mysql.database"),
		viper.GetString("mysql.charset"))

	//mysql 空值问题
	{
		db, err := sql.Open("mysql", conn)
		if err != nil {
			logrus.Fatal(err)
		}
		_, err = db.Exec("set global sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'")
		if err != nil {
			logrus.WithError(err).Fatal(err)
		}
		defer func() {
			db.Close()
		}()
	}
	//end
	
	if gormDb, err := gorm.Open("mysql", conn); err == nil {
		mysqlDB = gormDb
	} else {
		logrus.WithError(err).Fatalln("initialize mysql database failed")
	}
}
```