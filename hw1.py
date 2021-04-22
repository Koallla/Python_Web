from abc import abstractmethod, ABC
import json
import pickle

# 1
some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

class SerializationInterface(ABC):
    @abstractmethod
    def serialization(self):
        pass
        

class SerializationJson(SerializationInterface):
    def serialization(self, data, path):
        with open(path, 'w') as file:
            json.dump(data, file)



class SerializationBin(SerializationInterface):
    def serialization(self, data, path):
        with open(path, 'wb') as file:
            pickle.dump(data, file)


to_json = SerializationJson()
to_json.serialization(some_data, 'test.json')

to_bin = SerializationBin()
to_bin.serialization(some_data, 'test.bin')


# 2

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
