#coding:utf-8
from demo_pb2 import DemoRequest

demo_request = DemoRequest()
demo_request.user_id = 1
demo_request.user_name = "MAX"
demo_request.ext = "demo"
# 序列化
serialize = demo_request.SerializeToString()
print (serialize)
# 反序列化
deserialize = DemoRequest()
deserialize.ParseFromString(serialize)
print (deserialize)