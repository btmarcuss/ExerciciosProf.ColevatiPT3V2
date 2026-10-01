#Declaração de Variáveis
pnovo: float = 0.0
patual: float = 0.0
vmensal: int = 0

def novopreco(patual, vmensal):
    if (vmensal < 500) and (patual < 30.0): 
        pnovo = patual * 1.10
        print (f"O novo preço do produto é {pnovo:.2f}.")
    elif (vmensal > 499) and (patual > 29.99) and (patual <80.00):
        pnovo = patual * 1.15
        print (f"O novo preço do produto é {pnovo:.2f}.")
    elif (vmensal > 999) and (patual > 79.99):
        pnovo = patual * 0.95
        print (f"O novo preço do produto é {pnovo:.2f}.")
    else:
        pnovo = patual
        print (f"O novo preço do produto é {pnovo:.2f}.")

def main():
    global patual
    global vmensal
    patual = float(input("Digite o valor atual do produto:"))
    vmensal = int(input("Digite a quantidade de vendas mensal:"))
    novopreco(patual, vmensal)

if (__name__ == "__main__"):
    main()