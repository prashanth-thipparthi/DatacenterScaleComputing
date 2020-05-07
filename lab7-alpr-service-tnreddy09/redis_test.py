import redis

redis_server = redis.StrictRedis(host='redisvm', db=2)

print(redis_server.smembers("e5a38c28141a09b39e8f5976db4e0d16"))
#print(redis_server.get("T9SJL1"))
