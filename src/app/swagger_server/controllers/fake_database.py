import base64
import uuid
class FakeDatabase:
    # Here will be the instance stored.
    __instance = None

    _associativeArrayId = dict()


    def get_a_uuid(self):
        u = uuid.uuid4()
        return str(u)

    def save(self, id, object):
        """Gets the name of this NewConfiguration.


        :return: The name of this NewConfiguration.
        :rtype: str
        """
        self._associativeArrayId[id] = object

    def read(self, id):
        """Gets the name of this NewConfiguration.

        :return: The name of this NewConfiguration.
        :rtype: str
        """
        if uuid.UUID(id).version == 4:
            return self._associativeArrayId[id]

    def remove(self, id):
        """Gets the name of this NewConfiguration.


        :return: The name of this NewConfiguration.
        :rtype: str
        """
        del self._associativeArrayId[id]

    def search(self, name):
        """Gets the name of this NewConfiguration.


        :return: The name of this NewConfiguration.
        :rtype: str
        """
        res = []
        for id in self._associativeArrayId:
            obj = self._associativeArrayId[id]
            if obj.name == name:
                res.append(obj)

        return res

    def load(self, db):
        self._associativeArrayId = db
  


    @staticmethod
    def getInstance():
        """ Static access method. """
        if FakeDatabase.__instance == None:
            FakeDatabase()
        return FakeDatabase.__instance 

    # @staticmethod
    # def factoryDB(dictionary):
    #     """ Static access method. """
    #     db = FakeDatabase.getInstance()
    #     FakeDatabase.getInstance()._associativeArrayId = dictionary
        

    def __init__(self):
        """ Virtually private constructor. """
        if FakeDatabase.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            FakeDatabase.__instance = self
