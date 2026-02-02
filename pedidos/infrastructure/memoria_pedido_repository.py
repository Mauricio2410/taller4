class MemoriaPedidoRepository:
    def __init__(self):
        self._almacen_pedidos = {}
        self._next_id = 1

    def guardar_pedido(self, pedido):
        pedido.id = self._next_id
        self._almacen_pedidos[self._next_id] = pedido
        self._next_id += 1
        return pedido

    def listar_todos(self):
        return list(self._almacen_pedidos.values())