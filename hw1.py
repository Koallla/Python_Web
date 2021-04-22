from abc import abstractmethod, ABC
import json
import pickle


some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

class MyBaseClass(ABC):
    @abstractmethod
    def serialize(self):
        pass
        

class SerializeJson(MyBaseClass):
    def serialize(self, data, path):
        with open(path, 'w') as file:
            json.dump(data, file)



class SerializeBin(MyBaseClass):
    def serialize(self, data, path):
        with open(path, 'wb') as file:
            pickle.dump(data, file)


to_json = SerializeJson()
to_json.serialize(some_data, 'test.json')

to_bin = SerializeBin()
to_bin.serialize(some_data, 'test.bin')


class Meta(type):

    def __new__(cls, clsname, bases, dct):
        dct['class_number'] = cls.children_number
        cls.children_number += 1
        return type.__new__(cls, clsname, bases, dct)


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
