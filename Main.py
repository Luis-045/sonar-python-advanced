"""Módulo principal del sistema bancario.

Permite ejecutar desde consola las operaciones de registro de clientes,
creación de cuentas, depósitos, retiros, transferencias y reportes.
"""

from GestorCuentas import GestorCuentas  # pylint: disable=E0611
from Reportes import Reportes  # pylint: disable=E0611
from Transaccion import Transaccion  # pylint: disable=E0611

# 🔹 Constantes de mensajes para evitar duplicaciones
MSG_ID_CLIENTE = "ID del cliente: "
MSG_NOMBRE_CLIENTE = "Nombre del cliente: "
MSG_NUMERO_CUENTA = "Número de cuenta: "
MSG_SALDO_INICIAL = "Saldo inicial: "
MSG_MONTO_DEPOSITAR = "Monto a depositar: "
MSG_MONTO_RETIRAR = "Monto a retirar: "
MSG_CUENTA_ORIGEN = "Cuenta origen: "
MSG_CUENTA_DESTINO = "Cuenta destino: "
MSG_MONTO_TRANSFERIR = "Monto a transferir: "


def menu():
    """Muestra el menú principal del sistema bancario."""
    print("\n=== Sistema Bancario ===")
    print("1. Registrar cliente")
    print("2. Crear cuenta")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Transferir")
    print("6. Ver reporte de saldos")
    print("7. Ver historial de cuenta")
    print("8. Salir")


def main():
    """Función principal que gestiona las operaciones bancarias desde consola."""
    banco = GestorCuentas()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                cid = int(input(MSG_ID_CLIENTE))
                nombre = input(MSG_NOMBRE_CLIENTE)
                cliente = banco.registrar_cliente(cid, nombre)
                print(f"Cliente registrado: {cliente}")

            elif opcion == "2":
                nc = int(input(MSG_NUMERO_CUENTA))
                cid = int(input(MSG_ID_CLIENTE))
                saldo = float(input(MSG_SALDO_INICIAL))
                cuenta = banco.crear_cuenta(nc, cid, saldo)
                print(f"Cuenta creada: {cuenta}")

            elif opcion == "3":
                nc = int(input(MSG_NUMERO_CUENTA))
                monto = float(input(MSG_MONTO_DEPOSITAR))
                cuenta = banco.buscar_cuenta(nc)
                Transaccion("deposito", monto, cuenta).ejecutar()
                print("Depósito realizado.")

            elif opcion == "4":
                nc = int(input(MSG_NUMERO_CUENTA))
                monto = float(input(MSG_MONTO_RETIRAR))
                cuenta = banco.buscar_cuenta(nc)
                Transaccion("retiro", monto, cuenta).ejecutar()
                print("Retiro realizado.")

            elif opcion == "5":
                origen = int(input(MSG_CUENTA_ORIGEN))
                destino = int(input(MSG_CUENTA_DESTINO))
                monto = float(input(MSG_MONTO_TRANSFERIR))
                c1 = banco.buscar_cuenta(origen)
                c2 = banco.buscar_cuenta(destino)
                Transaccion("transferencia", monto, c1, c2).ejecutar()
                print("✅ Transferencia realizada.")

            elif opcion == "6":
                Reportes.reporte_saldos(banco.listar_cuentas())

            elif opcion == "7":
                nc = int(input(MSG_NUMERO_CUENTA))
                cuenta = banco.buscar_cuenta(nc)
                Reportes.reporte_historial(cuenta)

            elif opcion == "8":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except (ValueError, TypeError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
