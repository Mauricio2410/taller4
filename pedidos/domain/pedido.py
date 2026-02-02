from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Pedido(BaseModel):
    id: Optional[int] = None
    cliente_id: int
    producto: str
    cantidad: int
    precio_total: float
    estado: str = "procesando" 
    fecha: datetime = datetime.now() 