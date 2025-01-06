class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Fuerza: {self.__fuerza}")
        print(f"Inteligencia: {self.__inteligencia}")
        print(f"Defensa: {self.__defensa}")
        print(f"Vida: {self.__vida}")
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(f"El personaje {self.__nombre } ha muerto")

    def dano(self, enemigo):
        return  self.__fuerza - enemigo.__defensa
    
    def ataque(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.__vida -= dano
        print(f"{self.__nombre} hizo un daño de {dano} a {enemigo.__nombre}")
        if enemigo.esta_vivo():
            print(f"La vida actual de {enemigo.__nombre} es: {enemigo.__vida}")
        else:
            enemigo.morir()

personaje1 = Personaje("Destructor", 350, 100, 180, 200)
personaje1.atributos()

personaje2 = Personaje("Otro por ahí", 190, 102, 100, 210)
personaje2.atributos()

personaje1.ataque(personaje2)
