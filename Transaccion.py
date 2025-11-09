class Transaccion:
    """Clase que representa una transacción bancaria."""

    def __init__(self, tipo: str, monto: float, cuenta_origen, cuenta_destino=None):
        self.tipo = tipo
        self.monto = monto
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino

    def ejecutar(self):
        """Ejecuta la transacción."""
        if self.tipo == "deposito":
            self.cuenta_origen.depositar(self.monto)
        elif self.tipo == "retiro":
            self.cuenta_origen.retirar(self.monto)
        elif self.tipo == "transferencia":
            if self.cuenta_destino is None:
                raise ValueError("Debe especificarse una cuenta destino para la transferencia.")
            self.cuenta_origen.retirar(self.monto)
            self.cuenta_destino.depositar(self.monto)
            self.cuenta_origen.historial.append(f"Transferencia enviada: -${self.monto:.2f}")
            self.cuenta_destino.historial.append(f"Transferencia recibida: +${self.monto:.2f}")
        else:
            raise ValueError("Tipo de transacción no válido.")
