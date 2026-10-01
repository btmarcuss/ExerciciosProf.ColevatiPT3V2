#Declaração de Variáveis
nvoltas: int = 0
extcirc: int = 0
duracao: int = 0

def calcvelomed(voltas, extensao, tempo):
    distancia: int = 0
    vmedia:int = 0
    distancia = (voltas * extensao)
    vmedia = ((distancia / tempo) / 16.667)
    print (f"A velocidade média é {vmedia:.2f} Km/H.")

def main():
    global nvoltas
    global extcirc
    global duracao
    nvoltas = int(input("Digite o numero de voltas dadas:"))
    extcirc = int(input("Digite quantos metros o circuito possui:"))
    duracao = int(input("Digite quantos minutos durou:"))
    calcvelomed(nvoltas, extcirc, duracao)

if (__name__ == "__main__"):
    main()