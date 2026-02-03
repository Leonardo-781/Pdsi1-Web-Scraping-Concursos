# 📚 Sistema de Coleta de Provas de Concursos Públicos

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Web scraper automatizado + Bot Telegram para coletar e consultar provas de concursos públicos.

## 🎯 Sobre o Projeto

Sistema completo de coleta, organização e consulta de dados de provas de concursos públicos, desenvolvido como projeto da disciplina PDSI1. Facilita o acesso a materiais de estudo para concurseiros através de web scraping e integração com Telegram.

## ⚙️ Funcionalidades

### 🕷️ Web Scraper
- ✅ Coleta automatizada de 291 provas de múltiplas páginas
- ✅ Extração de metadados: banca, órgão, cargo, nível, data, número de questões
- ✅ Captura de links diretos para PDFs (provas e gabaritos)
- ✅ Exportação em múltiplos formatos (JSON, CSV, Excel)
- ✅ Total de 12.876+ questões catalogadas

### 🤖 Bot Telegram
- ✅ Busca interativa por banca, órgão, cargo, ano
- ✅ Interface com botões (menu visual)
- ✅ Estatísticas em tempo real
- ✅ Links diretos para PDFs das provas
- ✅ Filtros automáticos (apenas provas com questões)

## 📋 Requisitos

- Python 3.9 ou superior
- Conexão com internet

## 🚀 Instalação

### 1. Clone ou baixe o projeto

```bash
cd "c:\Users\Leonardo\OneDrive\Documentos\VS Code\PDSI1 Web Scraping"
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o scraper

```bash
python scraper.py
```

### 4. Execute o Bot Telegram (Opcional)

```bash
python bot_simples.py
```

**⚠️ Importante:** Antes de executar o bot, configure seu token no arquivo `bot_simples.py` (linha 248)

## 📦 Dependências

- **requests**: Requisições HTTP
- **beautifulsoup4**: Parsing de HTML
- **pandas**: Manipulação e análise de dados
- **openpyxl**: Exportação para Excel
- **lxml**: Parser XML/HTML de alta performance
- **python-telegram-bot**: Integração com Telegram Bot API

## 💻 Uso

### 🕷️ Web Scraper

```bash
python scraper.py
```

O scraper irá:
1. Coletar provas de múltiplas páginas
2. Extrair metadados completos
3. Exportar para JSON, CSV e Excel
4. Exibir estatísticas

### 🤖 Bot Telegram

1. **Inicie o bot:**
```bash
python bot_simples.py
```

2. **No Telegram, envie:**
```
/menu
```

3. **Use os botões interativos:**
- 🔍 Buscar por Banca (TOP 10)
- 🗂️ Ver Todas as Bancas
- 📊 Ver Estatísticas
- 📅 Provas por Ano
- 🏢 Órgãos Públicos
- 💼 Cargos

## 📊 Formatos de Saída

### JSON
```json
{
  "titulo": "FCC - 2024 - TRT - Técnico Judiciário",
  "banca": "FCC",
  "orgao": "TRT - 6ª Região (PE)",
  "cargo": "Técnico Judiciário - Administrativo",
  "ano": "2024",
  "nivel": "Superior Completo",
  "data_aplicacao": "02/2025",
  "num_questoes": 50,
  "link_prova_pdf": "https://...",
  "link_gabarito_pdf": "https://...",
  "data_coleta": "2026-02-03 14:30:00"
}
```

### CSV
| titulo | banca | orgao | cargo | ano | nivel | num_questoes | link_prova_pdf |
|--------|-------|-------|-------|-----|-------|--------------|----------------|
| FCC - 2024... | FCC | TRT... | Técnico... | 2024 | Superior | 50 | https://... |

### Excel
Planilha formatada com todas as colunas, pronta para análise.

## 📈 Estatísticas Geradas

- Total de provas coletadas
- Top 10 bancas mais frequentes
- Top 10 órgãos mais frequentes
- Distribuição por nível de escolaridade
- Total de questões disponíveis
- Média de questões por prova

## 🛠️ Estrutura do Projeto

```
PDSI1 Web Scraping/
├── scraper.py                    # Script principal
├── requirements.txt              # Dependências
├── DOCUMENTACAO_PROJETO.md       # Documentação completa
├── README.md                     # Este arquivo
├── provas_concursos.json         # Dados em JSON (gerado)
├── provas_concursos.csv          # Dados em CSV (gerado)
└── provas_concursos.xlsx         # Dados em Excel (gerado)
```

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte da disciplina **PDSI1 - Projeto e Desenvolvimento de Sistemas I**, abordando:

- Web Scraping com Python
- Engenharia de Requisitos
- Histórias de Usuários
- MVP (Minimum Viable Product)
- Protótipos de Baixa Fidelidade
- Estudo de Viabilidade

## 📖 Documentação Completa

Para documentação detalhada incluindo:
- Introdução e contextualização
- Motivação com referências acadêmicas
- Protótipos de baixa fidelidade
- Estudo de viabilidade técnica
- Requisitos funcionais e não-funcionais
- Histórias de usuários
- Definição do MVP

Consulte: [DOCUMENTACAO_PROJETO.md](DOCUMENTACAO_PROJETO.md)

## ⚖️ Considerações Legais

- ⚠️ Este projeto é apenas para fins **educacionais**
- ⚠️ Os dados coletados são **públicos** e acessíveis sem login
- ⚠️ Respeita delays entre requisições para não sobrecarregar servidores
- ⚠️ Não comercialize os dados coletados
- ⚠️ Provas permanecem propriedade das bancas/órgãos originais

## 🔮 Roadmap Futuro

### Versão 1.1 (MVP+1)
- [ ] Dashboard web interativo (Streamlit/Flask)
- [ ] Banco de dados SQLite
- [ ] Sistema de busca avançada

### Versão 1.2 (MVP+2)
- [ ] Bot do Telegram para notificações
- [ ] Agendamento automático de coletas
- [ ] API REST para acesso aos dados

### Versão 2.0 (MVP+3)
- [ ] PDF scraping (extração de questões)
- [ ] Classificação de questões com Machine Learning
- [ ] Interface web completa com autenticação

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📧 Contato

**Autor:** Leonardo  
**Disciplina:** PDSI1 - Web Scraping  
**Data:** Fevereiro 2026

## 📝 Licença

Este projeto é de código aberto para fins educacionais. Use com responsabilidade e respeite os termos de uso dos sites de origem.

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**📚 Bons estudos e boa sorte nos concursos!**
