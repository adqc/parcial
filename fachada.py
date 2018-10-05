import factory_method
import sys
import state_modificado

class EmpleadosManager:
    def iniciarLabores(self):
        factory = factory_method.FactoryEmpleado()
        emp = factory.obtener_empleado("mozo", "peps")
        emp1 = factory.obtener_empleado("cocinero", "otto")
        emp.iniciarLabores()
        emp1.iniciarLabores()
def main():
    empleadosFachada = EmpleadosManager()
    empleadosFachada.iniciarLabores()
    
if __name__=="__main__":
    main()