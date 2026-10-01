#Declaração de variáveis
valornum : int = 0

def fatorial(valor):
    if valor == 1 or valor == 0:
        return 1
    else:
        return valor * fatorial(valor - 1)
    
def main():
    global valornum 
    valornum = int(input("Digite um valor: "))
    fatorial(valornum)
    print (fatorial(valornum))

if (__name__ == '__main__'):
    main()