#Declaração de variáveis
investimento: int = 0
valorinv: float = 0.0
valorcor: float = 0.0

def investimento(valorinv):
    if (valorinv < 0):
        print ("Valor inválido.")
    else:
        investimento = int(input("Qual o tipo de investimento? 1 = poupança, 2 = renda fixa:"))
        if (investimento > 2) or (investimento < 1):
            print ("Tipo de investimento inválido.")
        else:
            if investimento == 1:
                valorcor = valorinv * 1.03
                print (f"O valor apos 30 dias é {valorcor:.2f}.")
            else:
                valorcor = valorinv * 1.05
                print (f"O valor apos 30 dias é {valorcor:.2f}.")

def main():
    global valorinv
    global valorcor
    valorinv = float(input("Digite o valor investido:"))
    investimento(valorinv)

if (__name__ == "__main__"):
    main()