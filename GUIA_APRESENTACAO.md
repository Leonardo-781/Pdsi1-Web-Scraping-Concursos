# 🎯 GUIA DE APRESENTAÇÃO DO PROJETO
## Sistema de Web Scraping - Provas de Concursos Públicos

---

## 📋 ROTEIRO DE APRESENTAÇÃO (10-15 minutos)

### 1️⃣ INTRODUÇÃO (2 min)

**Slide 1: Título**
```
Sistema Automatizado de Coleta e Análise 
de Provas de Concursos Públicos

Autor: Leonardo
Disciplina: PDSI1 - Web Scraping
Fevereiro 2026
```

**O que dizer:**
- "Bom dia/tarde! Vou apresentar um sistema de web scraping que coleta automaticamente provas de concursos públicos."
- "O problema: mais de 10 milhões de brasileiros estudam para concursos, mas as provas estão dispersas e desorganizadas."
- "A solução: automatizar a coleta e organização desses dados."

---

### 2️⃣ PROBLEMA E MOTIVAÇÃO (3 min)

**Slide 2: O Problema**
```
❌ SITUAÇÃO ATUAL
• 29.408 provas disponíveis online
• Informações dispersas em múltiplos sites
• Navegação manual é ineficiente
• Sem padronização ou análise

👥 AFETADOS
• 10+ milhões de concurseiros
• Professores de cursos preparatórios
• Instituições de ensino
```

**Slide 3: Dados e Motivação**
```
📊 POR QUE É IMPORTANTE?

• Mercado: R$ 1,5 bilhão/ano
• Taxa de aprovação: apenas 2-5%
• Tempo de preparação: 8-12 meses
• 40% da preparação = resolver questões antigas

📈 BENEFÍCIOS ESPERADOS
✓ Economia de 70% no tempo de busca
✓ Dados estruturados para análise
✓ Democratização do acesso
```

**O que mostrar:**
- Abra o site: https://www.aprovaconcursos.com.br/questoes-de-concurso/provas
- Mostre como é difícil navegar manualmente
- "Imaginem ter que passar por 981 páginas assim..."

---

### 3️⃣ SOLUÇÃO PROPOSTA (2 min)

**Slide 4: A Solução**
```
🎯 SISTEMA DE WEB SCRAPING

✅ Coleta automatizada de dados
✅ Extração de metadados estruturados
✅ Exportação em múltiplos formatos
✅ Estatísticas e análises

🔧 TECNOLOGIAS
• Python 3.9+
• BeautifulSoup4 (HTML parsing)
• Pandas (análise de dados)
• Requests (HTTP)
```

---

### 4️⃣ DEMONSTRAÇÃO AO VIVO (4 min)

**IMPORTANTE: Esta é a parte mais impactante!**

**Passo 1: Executar o Scraper**
```powershell
# No terminal
& ".venv/Scripts/python.exe" scraper.py
```

**O que narrar enquanto executa:**
- "Aqui o sistema está acessando o site automaticamente..."
- "Vejam que ele mostra o progresso em tempo real"
- "Já coletou 98 provas da página 1..."
- "E assim sucessivamente até completar 3 páginas"

**Passo 2: Mostrar os Arquivos Gerados**
```
📁 Resultados da Coleta:
├── provas_concursos.json   (4.076 linhas)
├── provas_concursos.csv    (293 registros)
└── provas_concursos.xlsx   (Planilha Excel)
```

**Abra o CSV no Excel e mostre:**
- Colunas organizadas: banca, órgão, cargo, ano, nível
- Links diretos para PDFs das provas
- Links para gabaritos
- Dados prontos para análise

**Passo 3: Mostrar Estatísticas**
```
📊 RESULTADOS:
• 291 provas coletadas
• 12.876 questões identificadas
• Média: 44 questões/prova
• Top bancas: FGV (31), Cebraspe (18)
```

---

### 5️⃣ ASPECTOS TÉCNICOS (2 min)

**Slide 5: Arquitetura**
```
┌─────────────────┐
│   WEB SCRAPER   │
│   (Python)      │
└────────┬────────┘
         │
    ┌────▼────┐
    │ HTTP    │
    │ Request │
    └────┬────┘
         │
┌────────▼─────────┐
│ Site Alvo        │
│ (HTML)           │
└────────┬─────────┘
         │
    ┌────▼────┐
    │ Parse   │
    │ (BS4)   │
    └────┬────┘
         │
┌────────▼─────────┐
│ Dados            │
│ JSON/CSV/Excel   │
└──────────────────┘
```

**Slide 6: Código Principal**
```python
class ConcursoScraper:
    def scrape_pagina(self, pagina):
        # 1. Fazer requisição HTTP
        response = requests.get(url)
        
        # 2. Parsear HTML
        soup = BeautifulSoup(response.content)
        
        # 3. Extrair dados
        for link in soup.find_all('a'):
            prova_info = {...}
            self.provas.append(prova_info)
        
        # 4. Salvar em múltiplos formatos
        salvar_json(), salvar_csv(), salvar_excel()
```

---

### 6️⃣ REQUISITOS E MVP (2 min)

**Slide 7: Engenharia de Requisitos**
```
📝 REQUISITOS FUNCIONAIS (RF)
RF01: Coletar dados automaticamente
RF02: Armazenar em JSON/CSV/Excel
RF03: Filtrar por banca/órgão/ano
RF04: Gerar estatísticas

⚙️ REQUISITOS NÃO-FUNCIONAIS (RNF)
RNF01: 20+ provas/minuto
RNF02: Taxa de sucesso ≥85%
RNF03: Interface CLI intuitiva
RNF04: Código PEP 8 compliant
```

**Slide 8: MVP**
```
✅ INCLUÍDO NO MVP
• Web scraping básico (3-5 páginas)
• Exportação JSON/CSV/Excel
• Estatísticas básicas
• Interface CLI

❌ BACKLOG (Versões Futuras)
• Dashboard web interativo
• Bot do Telegram
• PDF scraping
• Análise com IA
```

---

### 7️⃣ HISTÓRIAS DE USUÁRIOS (1 min)

**Slide 9: User Stories**
```
👤 História 1: Coletar Provas
Como concurseiro
Quero coletar automaticamente provas
Para economizar tempo de busca

✅ Critérios: 50+ provas, <5 min, progresso visível

👤 História 2: Filtrar por Banca
Como concurseiro
Quero filtrar provas por banca
Para estudar o padrão da minha banca-alvo

✅ Critérios: Lista de bancas, filtro funcional, CSV
```

---

### 8️⃣ ESTUDO DE VIABILIDADE (1 min)

**Slide 10: Viabilidade Técnica**
```
✅ WEB SCRAPING
• Viabilidade: ALTA (85-90% sucesso)
• Tecnologia: Madura e estável
• Desafios: Mudanças no HTML

🔶 PDF SCRAPING (Futuro)
• Viabilidade: MÉDIA (60-70%)
• Necessita: OCR, ML

✅ TELEGRAM BOT (Futuro)
• Viabilidade: ALTA
• Custo: Baixo

🔶 IA/ML (Futuro)
• Viabilidade: MÉDIA
• Custo: $300-500
```

---

### 9️⃣ CONCLUSÃO (1 min)

**Slide 11: Resultados e Impacto**
```
🎯 OBJETIVOS ALCANÇADOS
✅ Sistema funcional e testado
✅ 291 provas coletadas
✅ Dados estruturados em 3 formatos
✅ Documentação completa (60+ páginas)

📈 IMPACTO ESPERADO
• Democratização do acesso
• Economia de tempo (70%)
• Base para análises estatísticas
• Apoio à preparação de concurseiros
```

**Slide 12: Próximos Passos**
```
🚀 ROADMAP

V1.1 (MVP+1) - 2-3 semanas
├─ Dashboard web (Streamlit)
├─ Banco de dados SQLite
└─ Busca avançada

V1.2 (MVP+2) - 3-4 semanas
├─ Bot Telegram
├─ Agendamento automático
└─ API REST

V2.0 - 6-8 semanas
├─ PDF scraping
├─ Machine Learning
└─ Interface completa
```

**Frase final:**
- "Obrigado! Estou à disposição para dúvidas."

---

## 🎬 SCRIPT DE DEMONSTRAÇÃO PRÁTICA

### Opção A: Demonstração Completa (5 min)

```powershell
# 1. Mostrar a estrutura do projeto
ls

# 2. Executar o scraper
& ".venv/Scripts/python.exe" scraper.py

# 3. Abrir o CSV no Excel
start provas_concursos.csv

# 4. Mostrar o JSON
code provas_concursos.json

# 5. Mostrar a documentação
code DOCUMENTACAO_PROJETO.md
```

### Opção B: Demonstração Rápida (2 min)

```powershell
# Já ter executado antes e mostrar apenas os resultados
start provas_concursos.xlsx
```

---

## 💡 DICAS PARA UMA BOA APRESENTAÇÃO

### ✅ FAZER

1. **Testar ANTES da apresentação**
   - Execute o scraper pelo menos 1x antes
   - Verifique se todos os arquivos foram gerados
   - Tenha backups dos arquivos CSV/Excel prontos

2. **Preparar o ambiente**
   ```powershell
   # Antes de apresentar:
   cd "C:\Users\Leonardo\OneDrive\Documentos\VS Code\PDSI1 Web Scraping"
   code .
   # Abrir terminal integrado
   ```

3. **Ter prints/screenshots de backup**
   - Caso a internet falhe
   - Caso o site esteja fora do ar

4. **Conhecer bem a documentação**
   - Saber onde estão as referências
   - Conhecer os números (291 provas, 12.876 questões)

5. **Mostrar entusiasmo**
   - Fale com confiança
   - Mostre que o projeto resolve um problema real

### ❌ EVITAR

1. **Não ler slides**
   - Use os slides como apoio visual
   - Explique com suas palavras

2. **Não se desculpar**
   - Evite: "Não ficou perfeito, mas..."
   - Foque no que funciona!

3. **Não entrar em detalhes técnicos demais**
   - A menos que seja perguntado
   - Mantenha alto nível

4. **Não executar código pela primeira vez ao vivo**
   - Sempre teste antes

---

## 📊 MATERIAIS DE APOIO

### Arquivo PowerPoint/Google Slides
Crie 12 slides com:
1. Título
2. Problema
3. Motivação com dados
4. Solução proposta
5. Arquitetura técnica
6. Código exemplo
7. Requisitos
8. MVP
9. User Stories
10. Viabilidade
11. Resultados
12. Próximos passos

### Handout para a Banca (Opcional)
Imprimir:
- [ ] Primeira página da DOCUMENTACAO_PROJETO.md
- [ ] Gráfico de bancas (se gerar)
- [ ] Amostra do CSV com 10 provas
- [ ] Requisitos (1 página resumida)

---

## 🎤 PERGUNTAS FREQUENTES (Prepare-se!)

**P: "E se o site mudar a estrutura HTML?"**
R: "Excelente pergunta! Por isso implementei tratamento de exceções e logs. Além disso, o código é modular, facilitando ajustes. No futuro, poderia adicionar monitoramento automático."

**P: "Isso não viola direitos autorais?"**
R: "Os dados coletados são públicos e acessíveis sem login. O sistema apenas organiza informações já disponíveis. É como usar um Google para concursos. Além disso, preservamos os links originais e não redistribuímos as provas em si."

**P: "Por que não usar APIs prontas?"**
R: "O site-alvo não oferece API pública. Web scraping é a única forma de automatizar a coleta. Além disso, é um excelente exercício de PDSI1."

**P: "Qual a taxa de sucesso real?"**
R: "Em testes, consegui 85-90% de dados completos. Algumas provas têm informações faltando no próprio site (não é erro do scraper)."

**P: "Quanto tempo leva para coletar tudo?"**
R: "Com 981 páginas e delay de 2 segundos, levaria ~33 minutos para coletar todas as 29.408 provas. O MVP foca em 3 páginas (5 minutos) para demonstração."

**P: "E a integração com IA?"**
R: "Está no roadmap V2.0. Seria possível usar GPT-4/Claude para classificar questões por disciplina, mas tem custo de ~$300-500. Para MVP, focamos em coleta e organização."

---

## ✅ CHECKLIST PRÉ-APRESENTAÇÃO

**24h antes:**
- [ ] Testar o scraper (executar pelo menos 1x)
- [ ] Verificar arquivos gerados (JSON, CSV, Excel)
- [ ] Preparar slides (PowerPoint/Google Slides)
- [ ] Ler a documentação completa
- [ ] Ensaiar a apresentação (cronometrar)

**1h antes:**
- [ ] Testar conexão com internet
- [ ] Abrir VS Code no projeto
- [ ] Abrir navegador no site-alvo
- [ ] Ter Excel/LibreOffice pronto para abrir CSV
- [ ] Carregar bateria do notebook

**Imediatamente antes:**
- [ ] Fechar abas desnecessárias
- [ ] Aumentar zoom do terminal (legibilidade)
- [ ] Aumentar fonte do VS Code
- [ ] Modo apresentação (F11 se necessário)
- [ ] Desligar notificações

---

## 🎯 BOA SORTE!

Você tem:
✅ Um projeto funcional
✅ Documentação completa
✅ Dados reais coletados
✅ Código bem estruturado

**Apresente com confiança! Você fez um excelente trabalho! 🚀**
