"""
Script para buscar e filtrar provas de forma fácil
"""

import json
import pandas as pd

def buscar_por_banca(banca):
    """Busca provas por banca"""
    with open('provas_concursos.json', 'r', encoding='utf-8') as f:
        provas = json.load(f)
    
    resultados = [p for p in provas if banca.upper() in p.get('banca', '').upper()]
    
    print(f"\n🔍 Encontradas {len(resultados)} provas de {banca}\n")
    
    for i, prova in enumerate(resultados, 1):
        print(f"{i}. {prova.get('titulo', 'N/A')}")
        print(f"   📅 Data: {prova.get('data_aplicacao', 'N/A')}")
        print(f"   ❓ Questões: {prova.get('num_questoes', 0)}")
        print(f"   📄 PDF: {prova.get('link_prova_pdf', 'Não disponível')[:60]}")
        print()
    
    return resultados

def buscar_por_orgao(orgao):
    """Busca provas por órgão"""
    with open('provas_concursos.json', 'r', encoding='utf-8') as f:
        provas = json.load(f)
    
    resultados = [p for p in provas if orgao.upper() in p.get('orgao', '').upper()]
    
    print(f"\n🏢 Encontradas {len(resultados)} provas do {orgao}\n")
    
    for i, prova in enumerate(resultados, 1):
        print(f"{i}. {prova.get('titulo', 'N/A')}")
        print(f"   🏢 Órgão: {prova.get('orgao', 'N/A')}")
        print(f"   ❓ Questões: {prova.get('num_questoes', 0)}")
        print()
    
    return resultados

def buscar_por_cargo(cargo):
    """Busca provas por cargo"""
    with open('provas_concursos.json', 'r', encoding='utf-8') as f:
        provas = json.load(f)
    
    resultados = [p for p in provas if cargo.upper() in p.get('cargo', '').upper()]
    
    print(f"\n💼 Encontradas {len(resultados)} provas para {cargo}\n")
    
    for i, prova in enumerate(resultados, 1):
        print(f"{i}. {prova.get('titulo', 'N/A')}")
        print(f"   💼 Cargo: {prova.get('cargo', 'N/A')}")
        print(f"   ❓ Questões: {prova.get('num_questoes', 0)}")
        print()
    
    return resultados

def buscar_por_ano(ano):
    """Busca provas por ano"""
    with open('provas_concursos.json', 'r', encoding='utf-8') as f:
        provas = json.load(f)
    
    resultados = [p for p in provas if str(ano) in p.get('ano', '')]
    
    print(f"\n📅 Encontradas {len(resultados)} provas de {ano}\n")
    
    for i, prova in enumerate(resultados, 1):
        print(f"{i}. {prova.get('titulo', 'N/A')}")
        print(f"   📅 Ano: {prova.get('ano', 'N/A')}")
        print(f"   🏢 Órgão: {prova.get('orgao', 'N/A')}")
        print()
    
    return resultados

def exportar_filtro_excel(banca, arquivo_saida='resultado_busca.xlsx'):
    """Exporta resultados para Excel"""
    df = pd.read_csv('provas_concursos.csv')
    
    resultado = df[df['banca'].str.contains(banca, case=False, na=False)]
    
    resultado.to_excel(arquivo_saida, index=False)
    
    print(f"\n✅ {len(resultado)} provas exportadas para {arquivo_saida}")
    
    return resultado

def menu_interativo():
    """Menu interativo para buscar"""
    print("\n" + "="*60)
    print("🔍 BUSCA DE PROVAS DE CONCURSOS")
    print("="*60 + "\n")
    
    print("[1] Buscar por banca")
    print("[2] Buscar por órgão")
    print("[3] Buscar por cargo")
    print("[4] Buscar por ano")
    print("[5] Exportar para Excel")
    print("[0] Sair")
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        banca = input("Digite o nome da banca: ").strip()
        buscar_por_banca(banca)
    
    elif opcao == '2':
        orgao = input("Digite o nome do órgão: ").strip()
        buscar_por_orgao(orgao)
    
    elif opcao == '3':
        cargo = input("Digite o nome do cargo: ").strip()
        buscar_por_cargo(cargo)
    
    elif opcao == '4':
        ano = input("Digite o ano (ex: 2024): ").strip()
        buscar_por_ano(ano)
    
    elif opcao == '5':
        banca = input("Digite a banca para exportar: ").strip()
        exportar_filtro_excel(banca)
    
    elif opcao == '0':
        print("Até logo!")
        return
    
    input("\nPressione Enter para continuar...")
    menu_interativo()

if __name__ == "__main__":
    # Exemplos de uso
    print("""
╔═══════════════════════════════════════════════════════════╗
║  EXEMPLOS DE USO:                                         ║
╚═══════════════════════════════════════════════════════════╝

# Buscar provas da FGV
provas_fgv = buscar_por_banca("FGV")

# Buscar provas do IBAMA
provas_ibama = buscar_por_orgao("IBAMA")

# Buscar provas para Analista
provas_analista = buscar_por_cargo("Analista")

# Buscar provas de 2024
provas_2024 = buscar_por_ano(2024)

# Exportar resultados para Excel
exportar_filtro_excel("FGV", "resultado_FGV.xlsx")

# Menu interativo
menu_interativo()
    """)
    
    # Executar menu interativo
    menu_interativo()
