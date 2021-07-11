from bson.objectid import ObjectId
import redis


r = redis.Redis(
    host='127.0.0.1',
    port=6379
)


# data = {'_id': ObjectId('60e5c22cb4b14043acd4474c'), 'name': 'Mihail', 'surname': 'Zmiiov', 'adress': 'Kyiv, Ukraine', 'note': ['Repair car'], 'tag': ['Cars', 'Moto'], 'email': ['z@i.ua', 'zm@i.ua'], 'phone': ['380953128882'], 
# 'birthday': '22 07 1983'}


def save_to_redis(data):
    r.hmset(str(data['_id']), data)


def extract_from_redis(field, value):
    for item in r.scan_iter():
        res = r.hgetall(item)
        for key, data in res.items():
            if key.decode('utf-8') == field and data.decode('utf-8') == value:
                return r.hgetall(item)


