# dis_hla_lib/dis_hla_library.py
from abc import ABC, abstractmethod

class Platform(ABC):
    def __init__(self, id, name, x, y, z):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    @abstractmethod
    def send(self):
        """Muss in der abgeleiteten Klasse implementiert werden."""
        pass
