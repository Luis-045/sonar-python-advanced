"""Genera reportes simples de clientes y cuentas."""
class Reportes:
    """Genera reportes de cuentas y transacciones."""

    @staticmethod
    def reporte_saldos(cuentas):
        print("\n📊 Reporte de saldos:")
        for cuenta in cuentas:
            print(f"{cuenta}")

    @staticmethod
    def reporte_historial(cuenta):
        print(f"\n📒 Historial de la cuenta {cuenta.numero_cuenta}:")
        for mov in cuenta.historial:
            print(f" - {mov}")
