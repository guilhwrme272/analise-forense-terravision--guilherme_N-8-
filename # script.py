# script.py
# Aluno: Guilherme Pimentel Nogueira dos Santos
# Tema 8: Bacias Hidrográficas, Rios e Corpos d'Água Interiores

def carregar_camada_satelite(lista_altitudes):
    """
    Simula o carregamento adaptativo de camadas de satélite (LoD - Level of Detail)
    com base na altitude da câmera virtual para o tema de Bacias Hidrográficas e Rios.
    """
    if not isinstance(lista_altitudes, (list, tuple)) or len(lista_altitudes) < 5:
        print("Erro: Forneça uma lista com no mínimo 5 valores de altitude.")
        return

    print("=== INICIANDO RENDERIZAÇÃO ADAPTATIVA DE CAMADAS (LoD) ===")
    print("Tema: Bacias Hidrográficas, Rios e Corpos d'Água Interiores\n")

    for index, altitude in enumerate(lista_altitudes, start=1):
        print(f"Leitura {index}: Altitude = {altitude:.1f}m")
        
        if altitude > 10000:
            print("  [LoD Baixo - Resolução Continental]")
            print("  -> Renderizando: Mosaico global dos continentes, traçado das grandes bacias hidrográficas mundiais e delimitação do contorno dos grandes oceanos e lagos gigantes.\n")
        
        elif 1000 <= altitude <= 10000:
            print("  [LoD Médio - Resolução Regional]")
            print("  -> Renderizando: Mosaico regional da bacia hidrográfica, rede de drenagem dos rios principais e secundários, represas e contornos de grandes reservatórios de água interior.\n")
        
        else: # altitude < 1000m
            print("  [LoD Alto - Alta Resolução / Detalhes Finos]")
            print("  -> Renderizando: Meandros finos dos rios, leitos fluviais, margens com vegetação ciliar, reflexos especulares na superfície da água, pequenas lagoas e canais urbanos/rurais.\n")

if __name__ == "__main__":
    # Teste de execução com pelo menos 5 valores de altitude (em metros)
    altitudes_simuladas = [15000.0, 8500.0, 4200.0, 850.0, 150.0]
    carregar_camada_satelite(altitudes_simuladas)# script.py
# Aluno: Guilherme Pimentel Nogueira dos Santos
# Tema 8: Bacias Hidrográficas, Rios e Corpos d'Água Interiores

def carregar_camada_satelite(lista_altitudes):
    """
    Simula o carregamento adaptativo de camadas de satélite (LoD - Level of Detail)
    com base na altitude da câmera virtual para o tema de Bacias Hidrográficas e Rios.
    """
    if not isinstance(lista_altitudes, (list, tuple)) or len(lista_altitudes) < 5:
        print("Erro: Forneça uma lista com no mínimo 5 valores de altitude.")
        return

    print("=== INICIANDO RENDERIZAÇÃO ADAPTATIVA DE CAMADAS (LoD) ===")
    print("Tema: Bacias Hidrográficas, Rios e Corpos d'Água Interiores\n")

    for index, altitude in enumerate(lista_altitudes, start=1):
        print(f"Leitura {index}: Altitude = {altitude:.1f}m")
        
        if altitude > 10000:
            print("  [LoD Baixo - Resolução Continental]")
            print("  -> Renderizando: Mosaico global dos continentes, traçado das grandes bacias hidrográficas mundiais e delimitação do contorno dos grandes oceanos e lagos gigantes.\n")
        
        elif 1000 <= altitude <= 10000:
            print("  [LoD Médio - Resolução Regional]")
            print("  -> Renderizando: Mosaico regional da bacia hidrográfica, rede de drenagem dos rios principais e secundários, represas e contornos de grandes reservatórios de água interior.\n")
        
        else: # altitude < 1000m
            print("  [LoD Alto - Alta Resolução / Detalhes Finos]")
            print("  -> Renderizando: Meandros finos dos rios, leitos fluviais, margens com vegetação ciliar, reflexos especulares na superfície da água, pequenas lagoas e canais urbanos/rurais.\n")

if __name__ == "__main__":
    # Teste de execução com pelo menos 5 valores de altitude (em metros)
    altitudes_simuladas = [15000.0, 8500.0, 4200.0, 850.0, 150.0]
    carregar_camada_satelite(altitudes_simuladas)
