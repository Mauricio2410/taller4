from abc import ABC, abstractmethod

class UsuarioRepository(ABC):
    @abstractmethod
    def guardar(self, usuario):
        pass

    @abstractmethod
    def buscar_por_id(self, id):
        pass