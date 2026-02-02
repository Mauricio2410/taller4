# usuarios/application/servicios.py

class UsuarioService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_nuevo_usuario(self, id, nombre, email):
        # Aquí es donde pondrías reglas de negocio si el profe las pide
        # Por ahora, simplemente enviamos los datos al repositorio
        print(f"Procesando registro para: {nombre}")
        return self.repository.guardar({"id": id, "nombre": nombre, "email": email})

    def obtener_usuario(self, id):
        return self.repository.buscar_por_id(id)