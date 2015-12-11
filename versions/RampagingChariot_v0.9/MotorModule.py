from abc import ABCMeta, abstractmethod

class MotorAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def forward(self, speed):
        pass

    @abstractmethod
    def reverse(self):
        pass
        
    @abstractmethod
    def right(self, rspeed):
        pass

    @abstractmethod
    def left(self, lspeed):
        pass

    @abstractmethod
    def center(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
