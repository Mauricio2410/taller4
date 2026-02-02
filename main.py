from fastapi import FastAPI
from typing import List

from usuarios.application.servicios import UsuarioService
from usuarios.infrastructure.memoria_usuario_repository import MemoriaUsuarioRepository
from usuarios.domain.usuario import Usuario

from pedidos.domain.pedido import Pedido
from pedidos.infrastructure.memoria_pedido_repository import MemoriaPedidoRepository

app = FastAPI(
    title="Sistema de Gestión Taller 4 - Alex Gonzalez",
    description="Microservicios de Usuarios y Pedidos con Arquitectura Hexagonal",
    version="1.0.0"
)

repo_u = MemoriaUsuarioRepository()
serv_u = UsuarioService(repo_u)

repo_p = MemoriaPedidoRepository()

@app.get("/", tags=["General"])
def bienvenida():
    return {
        "mensaje": "Panel de Control Activo", 
        "alumno": "Mauricio Alexander Gonzalez",
        "materia": "Taller de Desarrollo 4"
    }

@app.post("/registrar-usuario/", response_model=str, tags=["Usuarios"])
def api_usuario(u: Usuario):
    return serv_u.registrar_nuevo_usuario(u)

@app.get("/listar-usuarios/", tags=["Usuarios"])
def api_listar_usuarios():
    return list(repo_u._datos.values())

@app.post("/registrar-pedido/", response_model=Pedido, tags=["Pedidos"])
def api_pedido(p: Pedido):
    return repo_p.guardar_pedido(p)

@app.get("/ver-pedidos/", response_model=List[Pedido], tags=["Pedidos"])
def api_ver_pedidos():
    return repo_p.listar_todos()