
from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):pass

    @abstractmethod
    def accelerate(self):pass

    @abstractmethod
    def stop(self):pass



class Dio(Bike):

    def start(self):
        print("dio bike start method")

    def accelerate(self):
        print("dio accelerate method")

    def stop(self):
        print("dio stop method")


dio_instance=Dio()

dio_instance.start()

dio_instance.accelerate()
