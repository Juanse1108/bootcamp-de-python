class CuentaCorriente:
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado {monto} en tu cuenta corriente.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > self.saldo:
            print(f"Fondos insuficientes. Tu saldo actual es {self.saldo}.")
        elif monto > 0:
            self.saldo -= monto
            print(f"Has retirado {monto} de tu cuenta corriente.")
        else:
            print("El monto a retirar debe ser positivo.")

    def mostrar_saldo(self):
        return self.saldo


class CuentaAhorros:
    def __init__(self):
        self.saldo = 0.0
        self.interes_mensual = 0.006  # 0.6% de interés mensual

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado {monto} en tu cuenta de ahorros.")
        else:
            print("El monto a depositar debe ser positivo.")

    def avanzar_mes(self):
        self.saldo += self.saldo * self.interes_mensual
        print(f"El saldo de tu cuenta de ahorros ha aumentado a {self.saldo} debido al interés mensual.")

    def mostrar_saldo(self):
        return self.saldo


class CDT:
    def __init__(self):
        self.capital = 0.0
        self.interes_mensual = 0.0
        self.abierto = False

    def abrir(self, capital, interes_mensual):
        if capital > 0 and 0 < interes_mensual <= 100:
            self.capital = capital
            self.interes_mensual = interes_mensual / 100  # Convertir porcentaje a decimal
            self.abierto = True
            print(f"Has abierto un CDT con {capital} de capital y {interes_mensual * 100}% de interés mensual.")
        else:
            print("El capital y el interés deben ser positivos y el interés no puede superar el 100%.")

    def cerrar(self):
        if self.abierto:
            total = self.capital + (self.capital * self.interes_mensual)
            self.capital = 0.0
            self.interes_mensual = 0.0
            self.abierto = False
            print(f"Has cerrado el CDT. El monto total de {total} ha sido transferido a tu cuenta corriente.")
            return total
        else:
            print("No tienes un CDT abierto.")
            return 0.0

    def avanzar_mes(self):
        if self.abierto:
            self.capital += self.capital * self.interes_mensual

    def mostrar_saldo(self):
        if self.abierto:
            return self.capital
        else:
            return 0.0


class CuentaBancaria:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.corriente = CuentaCorriente()
        self.ahorros = CuentaAhorros()
        self.cdt = CDT()

    def mostrar_saldo_total(self):
        total = self.corriente.mostrar_saldo() + self.ahorros.mostrar_saldo() + self.cdt.mostrar_saldo()
        print(f"El saldo total de la cuenta es {total}.")
        return total


# Solicitar datos del cliente
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cédula: ")

# Crear el objeto CuentaBancaria con los datos del cliente
cliente = CuentaBancaria(nombre, cedula)

# Menú de operaciones bancarias
while True:
    print("\n--- Menú de operaciones bancarias ---")
    print("1. Depositar en cuenta corriente")
    print("2. Retirar de cuenta corriente")
    print("3. Depositar en cuenta de ahorros")
    print("4. Avanzar un mes")
    print("5. Abrir un CDT")
    print("6. Cerrar CDT")
    print("7. Mostrar saldo total")
    print("8. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        monto = float(input("Ingrese el monto a depositar en cuenta corriente: "))
        cliente.corriente.depositar(monto)
    elif opcion == 2:
        monto = float(input(f"Tu saldo en la cuenta corriente es {cliente.corriente.mostrar_saldo()}. Ingrese el monto a retirar: "))
        cliente.corriente.retirar(monto)
    elif opcion == 3:
        monto = float(input("Ingrese el monto a depositar en cuenta de ahorros: "))
        cliente.ahorros.depositar(monto)
    elif opcion == 4:
        cliente.ahorros.avanzar_mes()
        cliente.cdt.avanzar_mes()
        print("Has avanzado un mes.")
    elif opcion == 5:
        capital = float(input("Ingrese el capital a invertir en el CDT: "))
        interes = float(input("Ingrese el interés mensual acordado para el CDT (%): "))
        cliente.cdt.abrir(capital, interes)
    elif opcion == 6:
        total = cliente.cdt.cerrar()
        cliente.corriente.depositar(total)
    elif opcion == 7:
        cliente.mostrar_saldo_total()
    elif opcion == 8:
        print("Saliendo del simulador bancario.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
