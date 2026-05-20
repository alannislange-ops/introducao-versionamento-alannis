
def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def divisao(a, b):
    if b == 0:
        return "Div0"
    else:
        return a/b

def multi(a, b):
    return a*b

def exponent(a,b):
    return a**b

def porcent(a,b):
    return a

while True:
    
    print("\n=====Calculadora=====")
    print("Escolha uma operação a seguir: ")
    print("Soma: 1")
    print("Multiplicação: 2")
    print("Divisão: 3")
    print("Subtração: 4")
    print("Exponênciação: 5")
    print("Sair: 0")
    
    opcao = int(input("Escolha a operação: "))
    
    if opcao == 0:
        break
    
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))
    
    if opcao == 1:
        resultado = soma(num1, num2)
        
    elif opcao == 2:
        resultado = multi(num1, num2)
        
    elif opcao == 3:
        resultado = divisao(num1, num2)
        
    elif opcao == 4:
        resultado = subtracao(num1, num2)
        
    elif opcao == 5:
        resultado = exponent(num1, num2)
    else:
        print("Opção inválida!")
        
    print(f"Resultado: {resultado}")

    