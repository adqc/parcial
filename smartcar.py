from sensor import Sensor

class AccionesGiro:
    def virar_derecha(self):
        pass
    def virar_izquierda(self):
        pass

class Computador:
    def __init__(self, sensor):
        self._sensor = sensor
        self.componentes = []

    def agregar_componentes(self, acciones_giro):
        self.componentes.append(acciones_giro)

    def obtener_datos(self):
        
        prob=self._sensor.obtener_data()
        
        for i in self.componentes:
            print(prob)
            if prob<=0.5:
                i.virar_izquierda()
            elif prob>0.5:
                i.virar_derecha()
        
class Faro:
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
        self.direccional_derecha_prendida=True

    def virar_izquierda(self):
        self.direccional_izquierda_prendida=True

class Motor:
    def __init__(self):
        self.velocidad = 20
    def virar_derecha(self):
        self.velocidad = self.velocidad + 5

    def virar_izquierda(self):
        self.velocidad = self.velocidad - 5

class Timon:
    def __init__(self):
        self.torque = 20

    def virar_derecha(self):
        self.torque = self.torque + 5
        print("torque: {}".format(self.torque))

    def virar_izquierda(self):
        self.torque = self.torque - 5

def main():

    motor = Motor()
    computador=Computador(Sensor())
    timon=Timon()
    faro=Faro()
    computador.agregar_componentes(motor)
    computador.agregar_componentes(timon)
    computador.agregar_componentes(faro)
    
    computador.obtener_datos()
    
    
if __name__=="__main__":
    main()