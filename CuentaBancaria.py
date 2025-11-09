"""Módulo que define la clase CuentaBancaria."""


from Cliente import Cliente


class CuentaBancaria:
    """Clase que representa una cuenta bancaria."""

    def __init__(self, numero_cuenta: int, cliente: Cliente, saldo_inicial: float = 0.0):  # noqa: E501
        """
        Inicializa una cuenta bancaria.

        Parameters
        ----------
        numero_cuenta : int
            Número único de la cuenta.
        cliente : Cliente
            Objeto que representa al cliente dueño de la cuenta.
        saldo_inicial : float, optional
            Saldo inicial de la cuenta (por defecto 0.0).
        """
        self.numero_cuenta = numero_cuenta
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.historial: list[str] = []

    def depositar(self, monto: float):
        """
        Deposita un monto en la cuenta bancaria.

        Parameters
        ----------
        monto : float
            Cantidad de dinero a depositar. Debe ser un valor positivo.

        Raises
        ------
        ValueError
            Si el monto es menor o igual a cero.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto
        self.historial.append(f"Depósito: +${monto:.2f}")

    def retirar(self, monto: float):
        """
        Retira un monto de la cuenta bancaria.

        Parameters
        ----------
        monto : float
            Cantidad de dinero a retirar.

        Raises
        ------
        ValueError
            Si el monto es menor o igual a cero o si no hay fondos suficientes.
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= monto
        self.historial.append(f"Retiro: -${monto:.2f}")

    def __str__(self) -> str:
        """
        Representación en cadena de la cuenta bancaria.

        Returns
        -------
        str
            Información legible de la cuenta.
        """
        return (
            f"Cuenta {self.numero_cuenta} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Saldo: ${self.saldo:.2f}"
        )
