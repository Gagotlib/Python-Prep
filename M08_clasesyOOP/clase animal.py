class Animal:
     def __init__(self, especie, edad):
         self.especie = especie
         self.edad = edad        
     def hablar(self):
         pass
 
     def moverse(self):
         pass
 
     def describeme(self):
         print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
     def __init__(self, especie, edad, dueño):
         # Alternativa 1
         # self.especie = especie
         # self.edad = edad
         # self.dueño = dueño
 
         # Alternativa 2
         super().__init__(especie, edad)
         self.dueño = dueño
 
mi_perro = Perro('mamífero', 7, 'Luis')
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)

mi_perro.describeme()