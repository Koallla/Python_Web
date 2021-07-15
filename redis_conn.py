from ast import literal_eval
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

# rec = {'_id': ObjectId('60eaf6a4738383b3eb88854e'), 'name': 'Test1', 'surname': 'Save', 'adress': 'Kuiv', 'note': ['dsfsdf'], 'tag': ['sdfsdfsd'], 'email': ['adsdf@d.ua', 's@ds.is'], 'phone': ['380503051268'], 'birthday': '22 01 2020'}

# save_to_redis(rec)



# print((extract_from_redis('name', 'Test1')))

# for item in r.scan_iter():
    # # r.delete(item)
    # for k, v in r.hgetall(item).items():
    #     if k.decode() == 'email':
    #         print(literal_eval(v.decode()))



