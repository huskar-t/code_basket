#coding:utf-8
import redis
# redis = redis.Redis(host=options.redis_host, port=options.redis_port, password=options.redis_password, db=options.redis_db)
redis_client = redis.Redis(host="127.0.0.1", port="6379", password="123", db=10)

redis_client.get("key")
redis_client.set("key","value")
redis_client.setex("key","value",30)
redis_client.delete(["key1","key2"])
redis_client.exists("key")