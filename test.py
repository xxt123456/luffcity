import redis
conn = redis.Redis(host='192.168.52.76',port=6379,password='123456',max_connections=100)
v=conn.keys()
print(v)
