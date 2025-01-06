class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f"El personaje {self.nombre } ha muerto")

    def dano(self, enemigo):
        return  self.fuerza - enemigo.defensa
    
    def ataque(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.vida -= dano
        print(f"{self.nombre} hizo un daño de {dano} a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida actual de {enemigo.nombre} es: {enemigo.vida}")
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma ):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma

    def seleccionar_arma(self):
        print("Seleccione un arma")
        opcion = int(input("1. Espada valkiriana daño 8 \n 2. Espada matadragones daño 10 \n 3. Escopeta daño 15 \n 4. Lanzallamas daño 6 "))
        if opcion == 1:
            self.arma = 8
        elif opcion == 2:
            self.arma = 10
        elif opcion == 3:
            self.arma = 15
        elif opcion == 4:
            self.arma = 6
        else:
            print("Ingrese un valor co33rrecto")

    def atributos(self):
        super().atributos()
        print(f"El daño del arma es: {self.arma} ")

    def dano(self, enemigo):
        return self.fuerza*self.arma-enemigo.defensa
    



guerrero1 = Guerrero("Laurent", 20, 80, 100, 150, 2)
guerrero1.seleccionar_arma()
guerrero1.atributos()


# personaje1 = Personaje("Destructor", 350, 100, 180, 200)
# personaje1.atributos()

# personaje2 = Personaje("Otro por ahí", 190, 102, 100, 210)
# personaje2.atributos()

# personaje1.ataque(personaje2)
