"""
Web Scraper para Provas de Concursos Públicos
Site: https://www.aprovaconcursos.com.br/questoes-de-concurso/provas
Autor: Leonardo
Data: Fevereiro 2026
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime
import time
import re

class ConcursoScraper:
    """Classe para realizar web scraping de provas de concursos públicos"""
    
    def __init__(self):
        self.base_url = "https://www.aprovaconcursos.com.br/questoes-de-concurso/provas"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.provas = []
    
    def extrair_numero_questoes(self, text):
        """Extrai o número de questões de uma string"""
        if not text:
            return 0
        match = re.search(r'(\d+)\s+Quest', text)
        if match:
            return int(match.group(1))
        return 0
    
    def scrape_pagina(self, pagina=1):
        """Faz scraping de uma página específica"""
        url = f"{self.base_url}/filtro/auto/pagina/{pagina}/quantidade-por-pagina/30"
        
        try:
            print(f"Acessando página {pagina}...")
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Procurar por cards de provas
            provas_encontradas = 0
            
            # Buscar links de provas
            links_prova = soup.find_all('a', href=re.compile(r'/questoes-de-concurso/prova/'))
            
            for link in links_prova:
                href = link.get('href', '')
                
                # Evitar duplicatas e links de informações
                if 'prova/' in href and href not in [p.get('link') for p in self.provas]:
                    # Buscar informações próximas ao link
                    parent = link.find_parent(['div', 'article', 'section'])
                    
                    if parent:
                        prova_info = {
                            'titulo': link.get_text(strip=True),
                            'link': f"https://www.aprovaconcursos.com.br{href}" if href.startswith('/') else href,
                            'banca': '',
                            'orgao': '',
                            'cargo': '',
                            'ano': '',
                            'nivel': '',
                            'data_aplicacao': '',
                            'num_questoes': 0,
                            'link_prova_pdf': '',
                            'link_gabarito_pdf': '',
                            'data_coleta': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }
                        
                        # Extrair informações do texto
                        texto_completo = parent.get_text(separator=' ', strip=True)
                        
                        # Buscar concurso público
                        concurso_match = re.search(r'Concurso Público:\s*([^P]+)', texto_completo)
                        if concurso_match:
                            prova_info['orgao'] = concurso_match.group(1).strip()
                        
                        # Buscar data de aplicação
                        data_match = re.search(r'Prova aplicada em:\s*(\d+/\d+)', texto_completo)
                        if data_match:
                            prova_info['data_aplicacao'] = data_match.group(1).strip()
                        
                        # Buscar nível
                        nivel_match = re.search(r'Nível:\s*([^I]+)', texto_completo)
                        if nivel_match:
                            prova_info['nivel'] = nivel_match.group(1).strip()
                        
                        # Buscar número de questões
                        questoes_match = re.search(r'(\d+)\s+Quest', texto_completo)
                        if questoes_match:
                            prova_info['num_questoes'] = int(questoes_match.group(1))
                        
                        # Buscar links PDF
                        links_pdf = parent.find_all('a', href=re.compile(r'\.pdf$'))
                        for pdf_link in links_pdf:
                            pdf_href = pdf_link.get('href', '')
                            pdf_text = pdf_link.get_text(strip=True).lower()
                            
                            if 'prova' in pdf_text and not prova_info['link_prova_pdf']:
                                prova_info['link_prova_pdf'] = pdf_href
                            elif 'gabarito' in pdf_text and not prova_info['link_gabarito_pdf']:
                                prova_info['link_gabarito_pdf'] = pdf_href
                        
                        # Extrair banca, órgão e cargo do título
                        partes_titulo = prova_info['titulo'].split(' - ')
                        if len(partes_titulo) >= 3:
                            prova_info['banca'] = partes_titulo[0].strip()
                            prova_info['ano'] = partes_titulo[1].strip()
                            if not prova_info['orgao']:
                                prova_info['orgao'] = partes_titulo[2].strip()
                            if len(partes_titulo) > 3:
                                prova_info['cargo'] = ' - '.join(partes_titulo[3:]).strip()
                        
                        self.provas.append(prova_info)
                        provas_encontradas += 1
            
            print(f"  ✓ {provas_encontradas} provas encontradas na página {pagina}")
            return provas_encontradas > 0
            
        except Exception as e:
            print(f"  ✗ Erro ao acessar página {pagina}: {str(e)}")
            return False
    
    def scrape_multiplas_paginas(self, num_paginas=3):
        """Faz scraping de múltiplas páginas"""
        print(f"\n{'='*60}")
        print(f"Iniciando scraping de {num_paginas} página(s)...")
        print(f"{'='*60}\n")
        
        for pagina in range(1, num_paginas + 1):
            sucesso = self.scrape_pagina(pagina)
            if not sucesso:
                print(f"Parando na página {pagina}")
                break
            
            # Delay para não sobrecarregar o servidor
            if pagina < num_paginas:
                time.sleep(2)
        
        print(f"\n{'='*60}")
        print(f"Total de provas coletadas: {len(self.provas)}")
        print(f"{'='*60}\n")
    
    def salvar_json(self, arquivo='provas_concursos.json'):
        """Salva os dados em formato JSON"""
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.provas, f, ensure_ascii=False, indent=2)
        print(f"✓ Dados salvos em {arquivo}")
    
    def salvar_csv(self, arquivo='provas_concursos.csv'):
        """Salva os dados em formato CSV"""
        if self.provas:
            df = pd.DataFrame(self.provas)
            df.to_csv(arquivo, index=False, encoding='utf-8-sig')
            print(f"✓ Dados salvos em {arquivo}")
    
    def salvar_excel(self, arquivo='provas_concursos.xlsx'):
        """Salva os dados em formato Excel"""
        if self.provas:
            df = pd.DataFrame(self.provas)
            df.to_excel(arquivo, index=False, engine='openpyxl')
            print(f"✓ Dados salvos em {arquivo}")
    
    def exibir_estatisticas(self):
        """Exibe estatísticas dos dados coletados"""
        if not self.provas:
            print("Nenhuma prova coletada ainda.")
            return
        
        df = pd.DataFrame(self.provas)
        
        print(f"\n{'='*60}")
        print("ESTATÍSTICAS DOS DADOS COLETADOS")
        print(f"{'='*60}\n")
        
        print(f"Total de provas: {len(self.provas)}")
        print(f"\nBancas mais frequentes:")
        print(df['banca'].value_counts().head(10))
        
        print(f"\nÓrgãos mais frequentes:")
        print(df['orgao'].value_counts().head(10))
        
        print(f"\nNíveis de escolaridade:")
        print(df['nivel'].value_counts())
        
        total_questoes = df['num_questoes'].sum()
        print(f"\nTotal de questões disponíveis: {total_questoes}")
        print(f"Média de questões por prova: {df['num_questoes'].mean():.1f}")
        
        print(f"\n{'='*60}\n")


def main():
    """Função principal"""
    scraper = ConcursoScraper()
    
    # Fazer scraping de 3 páginas (90 provas aproximadamente)
    scraper.scrape_multiplas_paginas(num_paginas=3)
    
    # Exibir estatísticas
    scraper.exibir_estatisticas()
    
    # Salvar em diferentes formatos
    print("Salvando dados...")
    scraper.salvar_json()
    scraper.salvar_csv()
    
    try:
        scraper.salvar_excel()
    except Exception as e:
        print(f"⚠ Não foi possível salvar Excel: {e}")
        print("  Instale openpyxl: pip install openpyxl")
    
    print("\n✓ Scraping concluído com sucesso!")


if __name__ == "__main__":
    main()
