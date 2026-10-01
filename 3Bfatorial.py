#Declaração de variáveis
valornum : int = 0

def fatorial(valor):
    fat: int = 0
    if valor == 1 or valor == 0:
        return 1
    else:
        fat = (valor * fatorial(valor - 1))
        return 1 / fat

def divisaovalores(valor1, valor2):
    rdivisao: float = 0.0
    rdivisao = (valor1 / valor2)    
    return rdivisao

def main():
    global valornum 
    num1: int = 0
    num2: int = 0
    num1 = int(input("Digite o primeiro valor para a divisão: "))
    num2 = int(input("Digite o segundo valor para a divisão: "))
    valornum = int(input("Digite um valor para o fatorial: "))
    fatorial(valornum)
    divisaovalores(num1, num2)

    print (fatorial(valornum))

if (__name__ == '__main__'):
    main()