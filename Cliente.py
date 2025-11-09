"""Módulo que define la clase Cliente para representar un cliente bancario."""


class Cliente:
    """Clase que representa un cliente bancario."""

    def __init__(self, cliente_id: int, nombre: str):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        """Agrega una cuenta bancaria al cliente."""
        self.cuentas.append(cuenta)

    def __str__(self):
        """Devuelve al cliente, su nombre y sus cuentas asociadas."""
        return (
            f"Cliente {self.cliente_id}: {self.nombre} "
            f"(Cuentas: {len(self.cuentas)})"
        )
