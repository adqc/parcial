from sensor import Sensor

class AccionesGiro:
    def virar_derecha(self):
        pass
    def virar_izquierda(self):
        pass

# Observado
class Computador:
    def __init__(self, sensor):
        self.sensor = sensor
        self.componentes = []

    def agregar_componentes(self, acciones_giro):
        self.componentes.append(acciones_giro)

    def obtener_datos(self):
        datos = self.sensor.obtener_data()
        for comp in self.componentes:
            if datos >= 0.5:
                comp.virar_derecha()
            else:
                comp.virar_izquierda()

#Observador
class Faro(AccionesGiro):
    def __init__(self):
        self.direccional_derecha_prendida = False
        self.direccional_izquierda_prendida = False

    def apagar_direccionales(self):
        pass

    def is_direccional_izquierda_prendida(self):
        return self.direccional_izquierda_prendida

    def isdireccional_derecha_prendida(self):
        return self.direccional_derecha_prendida
    
    def virar_derecha(self):
        self.direccional_derecha_prendida = True
        self.direccional_izquierda_prendida = False
        
    def virar_izquierda(self):
        self.direccional_derecha_prendida = False
        self.direccional_izquierda_prendida = True

#Observador
class Motor(AccionesGiro):
    def __init__(self):
        self.velocidad = 20
    def virar_derecha(self):
        if self.velocidad >= 5:
            self.velocidad = self.velocidad - 5
    def virar_izquierda(self):
        if self.velocidad >= 5:
            self.velocidad = self.velocidad - 5

#Observador
class Timon(AccionesGiro):
    def __init__(self):
        self.torque = 20

    def virar_derecha(self):
        self.torque = self.torque + 5

    def virar_izquierda(self):
        self.torque = self.torque - 5

def main():
    sensor = Sensor()
    computador = Computador(sensor)
    motor = Motor()
    faro = Faro()
    timon = Timon()
    
    # Agregamos observadores al observado
    computador.agregar_componentes(motor)
    computador.agregar_componentes(faro)
    computador.agregar_componentes(timon)
    
    computador.obtener_datos()
    print("Velocidad: {}".format(motor.velocidad))
    print("Timon: {}".format(timon.torque))
    print("Direccional Izquierda: {}".format(faro.direccional_izquierda_prendida))
    print("Direccional Derecha: {}".format(faro.direccional_derecha_prendida))
    
    

if __name__ == "__main__":
    main()

















#
