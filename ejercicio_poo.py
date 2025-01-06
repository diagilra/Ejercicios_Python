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

personaje1 = Personaje("Destructor", 350, 100, 180, 200)
personaje1.atributos()

personaje2 = Personaje("Otro por ahí", 190, 102, 100, 210)
personaje2.atributos()

personaje1.ataque(personaje2)
