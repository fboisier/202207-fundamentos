class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)    

    def cumpleaños(self):
        self.edad += 1

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad}"
    
    def __repr__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

usuarios = []

usuarios.append(Usuario("Francisco", 'Boisier', 37))
usuarios.append(Usuario("Javier", 'Boisier', 37))
usuarios.append(Usuario("Pancho", 'Boisier', 37))

print(usuarios)


for usuario in usuarios:
    usuario.cumpleaños()

print(usuarios)



