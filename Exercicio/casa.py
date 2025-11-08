class Casa:
    
    def __init__(self, codigo, tamanho_m2, engenheiro, custo_estimado, tempo_construcao):
        self.codigo = codigo
        self.tamanho_m2 = tamanho_m2
        self.engenheiro = engenheiro
        self.custo_estimado = custo_estimado
        self.tempo_construcao = tempo_construcao

    
    def __str__(self):
        return (f"Codigo: {self.codigo} | "
                f"Tamanho: {self.tamanho_m2} m | "
                f"Engenheiro: {self.engenheiro} | "
                f"Custo: R${self.custo_estimado:.2f} | "
                f"Tempo: {self.tempo_construcao} meses")





def exibir_todas(casas):
    print("\n--- Todas as Casas ---")
    for casa in casas:
        print(casa)



def exibir_maiores_que(casas, tamanho):
    print(f"\n--- Casas com mais de {tamanho} m---")
    for casa in casas:
        if casa.tamanho_m2 > tamanho:
            print(casa)



def exibir_por_engenheiro(casas, nome_parcial):
    print(f"\n--- Casas do engenheiro contendo '{nome_parcial}' ---")
    for casa in casas:
        if nome_parcial.lower() in casa.engenheiro.lower():
            print(casa)



if __name__ == "__main__":
    
    c1 = Casa("A01", 120, "Carlos Silva", 250000, 8)
    c2 = Casa("B02", 85, "Ana Souza", 180000, 6)
    c3 = Casa("C03", 150, "Carla Moura", 300000, 10)

   
    casas = [c1, c2, c3]

    
    exibir_todas(casas)
    exibir_maiores_que(casas, 100)
    exibir_por_engenheiro(casas, "Ar")
