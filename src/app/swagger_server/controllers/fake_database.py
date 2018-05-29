class FakeDatabase:
    # Here will be the instance stored.
    __instance = None

    _associativeArrayId = dict()

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
        for obj in self._associativeArrayId:
            if obj['name'] == name:
                res.append(obj)

        return res


    @staticmethod
    def getInstance():
        """ Static access method. """
        if FakeDatabase.__instance == None:
            FakeDatabase()
        return FakeDatabase.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if FakeDatabase.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            FakeDatabase.__instance = self
