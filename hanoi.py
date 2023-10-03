class Varilla():
    def __init__(self, N_Varilla):
        self.ListaDiscos = []
        self.NumeroVarilla = N_Varilla
    def AgregarDisco(self,Disco):
        self.ListaDiscos.append(Disco)
    def QuitarDisco(self):
        self.ListaDiscos.pop()
    def DiscoAlto(self):
        return self.ListaDiscos[len(self.ListaDiscos)-1]
    def ImprimirVarilla(self):
        print("[]")
        print(f"El numero de varilla {self.NumeroVarilla}")
        print(f"Tiene los discos {self.ListaDiscos}")
    

def hanoi(n, origen, auxiliar, destino):
    if n > 0:
        # Mover n-1 discos de la varilla origen a la auxiliar
        hanoi(n-1, origen, destino, auxiliar)
        
        # Mover el disco n desde la varilla origen a la destino
        disco = origen.DiscoAlto()
        origen.QuitarDisco()
        destino.AgregarDisco(disco)
        
        # Imprimir el estado de las varillas después del movimiento
        print("Estado de las varillas después del movimiento:")
        for varilla in [origen, auxiliar, destino]:
            varilla.ImprimirVarilla()
        
        # Mover los n-1 discos de la varilla auxiliar a la destino
        hanoi(n-1, auxiliar, origen, destino)

# Para resolver el problema con 3 discos:
varillas = [Varilla(i) for i in range(3)]
for i in range(3, 0, -1):
    varillas[0].AgregarDisco(i)
hanoi(3, varillas[0], varillas[1], varillas[2])

