from usuarios.domain.usuario_repository import UsuarioRepository

class MemoriaUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self._datos = {} 
        self._index = 1

    def guardar(self, usuario):
        if hasattr(usuario, 'id'):
            usuario.id = self._index
            self._datos[self._index] = usuario
        else:
            usuario['id'] = self._index
            self._datos[self._index] = usuario
            
        self._index += 1
        nombre = getattr(usuario, 'nombre', 'Usuario')
        return f"Registro exitoso: {nombre} (ID: {self._index - 1})"

    def buscar_por_id(self, id):
        return self._datos.get(id)