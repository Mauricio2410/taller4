class UsuarioService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_nuevo_usuario(self, usuario_obj):
        return self.repository.guardar(usuario_obj)