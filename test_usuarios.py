from usuarios.infrastructure.memoria_usuario_repository import MemoriaUsuarioRepository
from usuarios.application.servicios import UsuarioService

# 1. Creamos la infraestructura real (Memoria)
repo = MemoriaUsuarioRepository()

# 2. Se la inyectamos al servicio (Aplicación)
app_service = UsuarioService(repo)

# 3. Probamos registrar un usuario
print("--- Iniciando prueba de microservicio ---")
resultado = app_service.registrar_nuevo_usuario(1, "Alex", "alex@ejemplo.com")
print(f"Resultado: {resultado}")

# 4. Probamos buscarlo
usuario_encontrado = app_service.obtener_usuario(1)
print(f"Usuario recuperado: {usuario_encontrado}")