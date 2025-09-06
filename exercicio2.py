import sys

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a // b, a % b

# Espera: python script.py num1 num2 operacao
if len(sys.argv) != 4:
    sys.stdout.write("Uso: python script.py num1 num2 operacao\n")
    sys.exit()

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    sys.stdout.write("Erro: num1 e num2 devem ser inteiros.\n")
    sys.exit()

operacao = sys.argv[3]

if operacao == "soma":
    resultado = soma(a, b)
    sys.stdout.write(f"Resultado: {resultado}\n")
elif operacao == "sub":
    resultado = subtracao(a, b)
    sys.stdout.write(f"Resultado: {resultado}\n")
elif operacao == "mult":
    resultado = multiplicacao(a, b)
    sys.stdout.write(f"Resultado: {resultado}\n")
elif operacao == "div":
    resultado = divisao(a, b)
    sys.stdout.write(f"Resultado: {resultado}\n")
else:
    sys.stdout.write("Operação inválida. Use: soma, sub, mult, div\n")
