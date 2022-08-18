class Mueble:
    def __init__(self, material, patas, color, estilo):
        self.material = material
        self.patas = patas
        self.color = color
        self.estilo = estilo

    def limpiar(self):
        print("el mueble se esta limpiando con un articulo de limpieza de mueble")
