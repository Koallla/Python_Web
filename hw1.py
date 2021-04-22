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
