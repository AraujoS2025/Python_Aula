def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    quociente = a // b
    resto = a % b
    return quociente, resto


print(somar(10, 5))         
print(subtrair(10, 5))      
print(multiplicar(10, 5))   
print(dividir(10, 3))    