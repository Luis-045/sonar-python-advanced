"""Módulo encargado de gestionar los clientes y sus cuentas bancarias."""

from Cliente import Cliente
from CuentaBancaria import CuentaBancaria


class GestorCuentas:
    """Clase para manejar el registro y la administración de clientes y cuentas bancarias."""

    def __init__(self):
        """Inicializa los diccionarios de clientes y cuentas."""
        self.clientes = {}
        self.cuentas = {}

    def registrar_cliente(self, cliente_id: int, nombre: str):
        """Registra un nuevo cliente si el ID no está ocupado.

        Args:
            cliente_id (int): Identificador único del cliente.
            nombre (str): Nombre del cliente.

        Returns:
            Cliente: Instancia del cliente registrado.

        Raises:
            ValueError: Si el cliente ya está registrado.
        """
        if cliente_id in self.clientes:
            raise ValueError("El cliente ya está registrado.")
        cliente = Cliente(cliente_id, nombre)
        self.clientes[cliente_id] = cliente
        return cliente

    def crear_cuenta(self, numero_cuenta: int, cliente_id: int, saldo_inicial: float = 0.0):
        """Crea una nueva cuenta para un cliente existente.

        Args:
            numero_cuenta (int): Número de cuenta bancaria.
            cliente_id (int): ID del cliente titular.
            saldo_inicial (float, optional): Monto inicial. Defaults to 0.0.

        Returns:
            CuentaBancaria: Objeto cuenta creada.

        Raises:
            ValueError: Si el número de cuenta ya existe o el cliente no se encuentra.
        """
        if numero_cuenta in self.cuentas:
            raise ValueError("El número de cuenta ya existe.")
        cliente = self.clientes.get(cliente_id)
        if cliente is None:
            raise ValueError("Cliente no encontrado.")
        cuenta = CuentaBancaria(numero_cuenta, cliente, saldo_inicial)
        self.cuentas[numero_cuenta] = cuenta
        cliente.agregar_cuenta(cuenta)
        return cuenta

    def buscar_cuenta(self, numero_cuenta: int):
        """Busca y devuelve una cuenta bancaria según su número."""
        return self.cuentas.get(numero_cuenta)

    def listar_clientes(self):
        """Devuelve la lista completa de clientes registrados."""
        return list(self.clientes.values())

    def listar_cuentas(self):
        """Devuelve la lista completa de cuentas registradas."""
        return list(self.cuentas.values())
