from bson.objectid import ObjectId
import redis


r = redis.Redis(
    host='127.0.0.1',
    port=6379
)


def save_to_redis(data):
    r.hmset(str(data['_id']), data)


def extract_from_redis(field, value):
    try:
        for item in r.scan_iter():
            res = r.hgetall(item)
            for key, data in res.items():
                if key.decode('utf-8') == field and data.decode('utf-8') == value:
                    return r.hgetall(item)
    except:
        return None

