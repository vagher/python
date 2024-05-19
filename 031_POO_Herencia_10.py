


# Clase con Herencia

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def descripcion(self):
        return f"{super().descripcion()} con {self.num_puertas} puertas"

# Uso
coche = Coche("Toyota", "Corolla", 4)
print(coche.descripcion())
