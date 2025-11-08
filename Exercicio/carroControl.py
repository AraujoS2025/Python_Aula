from carro import Carros

def exibirCarros(crr):
    i = 0
    while i < len(crr):
        print(crr[i])
        i = i + 1


def exibirCarrosNovos(crr):
    i = 0
    while i < len(crr):
        if crr[i].ano >= 2024:
            print(crr[i])
        i = i + 1


def exibirCarrosPorAno(crr, ano):
    i = 0
    while i < len(crr):
        if crr[i].ano >= ano:
            print(crr[i])
        i = i + 1


Carros = []
Carros.append(Carros("Toyota", "Corolla", 2025))
Carros.append(Carros("Ford", "Mustang", 2022))
Carros.append(Carros("Fiat", "Palio", 2018))


exibirCarrosNovos(Carros)

