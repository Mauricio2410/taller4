# usuarios/infrastructure/memoria_usuario_repository.py
from usuarios.domain.usuario_repository import UsuarioRepository

class MemoriaUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self.usuarios = []

    def guardar(self, usuario):
        self.usuarios.append(usuario)
        return f"Usuario {usuario['nombre']} guardado en memoria."

    def buscar_por_id(self, id):
        for u in self.usuarios:
            if u['id'] == id:
                return u
        return None