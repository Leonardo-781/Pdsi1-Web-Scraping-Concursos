"""
Análise de dados com visualizações (protótipo futuro)
Requer: matplotlib, seaborn, plotly
"""

import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class AnalisadorConcursos:
    """Classe para análise e visualização de dados de concursos"""
    
    def __init__(self, arquivo_json='provas_concursos.json'):
        self.arquivo = arquivo_json
        self.df = None
        self._carregar_dados()
    
    def _carregar_dados(self):
        """Carrega dados do arquivo JSON"""
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            self.df = pd.DataFrame(dados)
            print(f"✓ {len(self.df)} provas carregadas para análise")
        except FileNotFoundError:
            print(f"⚠ Arquivo '{self.arquivo}' não encontrado.")
            print("Execute o scraper primeiro: python scraper.py")
    
    def grafico_bancas(self, top=10, salvar=False):
        """Gráfico de barras das bancas mais frequentes"""
        if self.df is None:
            return
        
        bancas_top = self.df['banca'].value_counts().head(top)
        
        plt.figure(figsize=(12, 6))
        bancas_top.plot(kind='bar', color='steelblue')
        plt.title(f'Top {top} Bancas Examinadoras', fontsize=16, fontweight='bold')
        plt.xlabel('Banca', fontsize=12)
        plt.ylabel('Número de Provas', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        if salvar:
            plt.savefig('graficos_bancas.png', dpi=300, bbox_inches='tight')
            print("✓ Gráfico salvo: graficos_bancas.png")
        
        plt.show()
    
    def grafico_nivel(self, salvar=False):
        """Gráfico de pizza da distribuição por nível"""
        if self.df is None:
            return
        
        niveis = self.df['nivel'].value_counts()
        
        plt.figure(figsize=(10, 8))
        colors = plt.cm.Set3(range(len(niveis)))
        
        plt.pie(niveis, labels=niveis.index, autopct='%1.1f%%', 
                colors=colors, startangle=90, textprops={'fontsize': 11})
        plt.title('Distribuição por Nível de Escolaridade', 
                  fontsize=16, fontweight='bold')
        plt.axis('equal')
        
        if salvar:
            plt.savefig('graficos_nivel.png', dpi=300, bbox_inches='tight')
            print("✓ Gráfico salvo: graficos_nivel.png")
        
        plt.show()
    
    def grafico_questoes_por_banca(self, top=10, salvar=False):
        """Gráfico de média de questões por banca"""
        if self.df is None:
            return
        
        bancas_top = self.df['banca'].value_counts().head(top).index
        df_top = self.df[self.df['banca'].isin(bancas_top)]
        
        media_questoes = df_top.groupby('banca')['num_questoes'].mean().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        media_questoes.plot(kind='barh', color='coral')
        plt.title(f'Média de Questões por Prova - Top {top} Bancas', 
                  fontsize=16, fontweight='bold')
        plt.xlabel('Média de Questões', fontsize=12)
        plt.ylabel('Banca', fontsize=12)
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        
        if salvar:
            plt.savefig('graficos_questoes_banca.png', dpi=300, bbox_inches='tight')
            print("✓ Gráfico salvo: graficos_questoes_banca.png")
        
        plt.show()
    
    def grafico_timeline_provas(self, salvar=False):
        """Gráfico de linha mostrando provas ao longo do tempo"""
        if self.df is None:
            return
        
        # Filtrar apenas provas com data válida
        df_datas = self.df[self.df['data_aplicacao'] != ''].copy()
        
        if len(df_datas) == 0:
            print("⚠ Nenhuma prova com data de aplicação disponível.")
            return
        
        # Contar provas por data
        contagem = df_datas['data_aplicacao'].value_counts().sort_index()
        
        plt.figure(figsize=(14, 6))
        plt.plot(contagem.index, contagem.values, marker='o', 
                linewidth=2, markersize=6, color='green')
        plt.title('Número de Provas por Período de Aplicação', 
                  fontsize=16, fontweight='bold')
        plt.xlabel('Período (MM/YYYY)', fontsize=12)
        plt.ylabel('Número de Provas', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if salvar:
            plt.savefig('graficos_timeline.png', dpi=300, bbox_inches='tight')
            print("✓ Gráfico salvo: graficos_timeline.png")
        
        plt.show()
    
    def heatmap_banca_nivel(self, salvar=False):
        """Heatmap de bancas vs níveis de escolaridade"""
        if self.df is None:
            return
        
        # Criar tabela de contingência
        crosstab = pd.crosstab(self.df['banca'], self.df['nivel'])
        
        # Filtrar apenas top 15 bancas
        top_bancas = self.df['banca'].value_counts().head(15).index
        crosstab_top = crosstab.loc[top_bancas]
        
        plt.figure(figsize=(12, 10))
        sns.heatmap(crosstab_top, annot=True, fmt='d', cmap='YlOrRd', 
                    cbar_kws={'label': 'Número de Provas'})
        plt.title('Distribuição Banca vs Nível de Escolaridade', 
                  fontsize=16, fontweight='bold')
        plt.xlabel('Nível de Escolaridade', fontsize=12)
        plt.ylabel('Banca Examinadora', fontsize=12)
        plt.tight_layout()
        
        if salvar:
            plt.savefig('graficos_heatmap.png', dpi=300, bbox_inches='tight')
            print("✓ Gráfico salvo: graficos_heatmap.png")
        
        plt.show()
    
    def relatorio_completo(self):
        """Gera relatório estatístico completo"""
        if self.df is None:
            return
        
        print("\n" + "="*60)
        print("RELATÓRIO COMPLETO DE ANÁLISE")
        print("="*60 + "\n")
        
        print(f"📊 Total de provas analisadas: {len(self.df)}")
        print(f"📅 Período de coleta: {self.df['data_coleta'].iloc[0]}")
        
        print("\n" + "-"*60)
        print("🏛️ BANCAS EXAMINADORAS")
        print("-"*60)
        print(self.df['banca'].value_counts().head(10))
        
        print("\n" + "-"*60)
        print("🏢 ÓRGÃOS PÚBLICOS")
        print("-"*60)
        print(self.df['orgao'].value_counts().head(10))
        
        print("\n" + "-"*60)
        print("📚 NÍVEIS DE ESCOLARIDADE")
        print("-"*60)
        print(self.df['nivel'].value_counts())
        
        print("\n" + "-"*60)
        print("❓ QUESTÕES")
        print("-"*60)
        print(f"Total de questões: {self.df['num_questoes'].sum()}")
        print(f"Média por prova: {self.df['num_questoes'].mean():.1f}")
        print(f"Mediana: {self.df['num_questoes'].median():.0f}")
        print(f"Mínimo: {self.df['num_questoes'].min()}")
        print(f"Máximo: {self.df['num_questoes'].max()}")
        
        print("\n" + "-"*60)
        print("📄 DISPONIBILIDADE DE PDFs")
        print("-"*60)
        provas_com_pdf = self.df['link_prova_pdf'].notna().sum()
        gabaritos_com_pdf = self.df['link_gabarito_pdf'].notna().sum()
        print(f"Provas com PDF: {provas_com_pdf} ({provas_com_pdf/len(self.df)*100:.1f}%)")
        print(f"Gabaritos com PDF: {gabaritos_com_pdf} ({gabaritos_com_pdf/len(self.df)*100:.1f}%)")
        
        print("\n" + "="*60 + "\n")
    
    def gerar_todos_graficos(self, salvar=True):
        """Gera todos os gráficos de uma vez"""
        print("\n📊 Gerando todos os gráficos...\n")
        
        self.grafico_bancas(salvar=salvar)
        self.grafico_nivel(salvar=salvar)
        self.grafico_questoes_por_banca(salvar=salvar)
        self.grafico_timeline_provas(salvar=salvar)
        self.heatmap_banca_nivel(salvar=salvar)
        
        print("\n✓ Todos os gráficos foram gerados!")
        if salvar:
            print("✓ Gráficos salvos na pasta do projeto")


def main():
    """Função principal"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║  ANÁLISE DE DADOS - CONCURSOS PÚBLICOS                   ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Criar analisador
    analisador = AnalisadorConcursos()
    
    if analisador.df is not None:
        # Gerar relatório completo
        analisador.relatorio_completo()
        
        # Menu interativo
        while True:
            print("\n" + "="*60)
            print("MENU DE VISUALIZAÇÕES")
            print("="*60)
            print("[1] Gráfico de Bancas")
            print("[2] Gráfico de Níveis de Escolaridade")
            print("[3] Média de Questões por Banca")
            print("[4] Timeline de Provas")
            print("[5] Heatmap Banca vs Nível")
            print("[6] Gerar TODOS os gráficos")
            print("[7] Relatório Completo")
            print("[0] Sair")
            print("="*60)
            
            try:
                opcao = input("\nEscolha uma opção: ").strip()
                
                if opcao == '1':
                    analisador.grafico_bancas(salvar=True)
                elif opcao == '2':
                    analisador.grafico_nivel(salvar=True)
                elif opcao == '3':
                    analisador.grafico_questoes_por_banca(salvar=True)
                elif opcao == '4':
                    analisador.grafico_timeline_provas(salvar=True)
                elif opcao == '5':
                    analisador.heatmap_banca_nivel(salvar=True)
                elif opcao == '6':
                    analisador.gerar_todos_graficos(salvar=True)
                elif opcao == '7':
                    analisador.relatorio_completo()
                elif opcao == '0':
                    print("\n✓ Encerrando análise. Até logo!")
                    break
                else:
                    print("⚠ Opção inválida. Tente novamente.")
            
            except KeyboardInterrupt:
                print("\n\n✓ Análise interrompida. Até logo!")
                break
            except Exception as e:
                print(f"\n⚠ Erro: {e}")


if __name__ == "__main__":
    # Verificar dependências
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        main()
    except ImportError as e:
        print(f"""
⚠️  ERRO: Dependências de visualização não encontradas!

Para usar este módulo, instale:

pip install matplotlib seaborn

Dependência faltando: {e}
        """)
