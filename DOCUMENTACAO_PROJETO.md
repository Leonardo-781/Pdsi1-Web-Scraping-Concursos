# Sistema de Coleta e Análise de Provas de Concursos Públicos

**Disciplina:** PDSI1 - Projeto e Desenvolvimento de Sistemas I  
**Autor:** Leonardo  
**Data:** Fevereiro de 2026  
**Versão:** 1.0

---

## 1. Título

**Sistema Automatizado de Coleta, Organização e Análise de Provas de Concursos Públicos com Web Scraping**

---

## 2. Introdução

### 2.1 Contextualização do Problema

No Brasil, os concursos públicos representam uma das principais portas de entrada para carreiras estáveis e bem remuneradas no serviço público. Segundo dados do IBGE (2023), existem aproximadamente 11,4 milhões de servidores públicos no país, e anualmente são realizados centenas de concursos em diferentes esferas governamentais[^1].

A preparação para concursos públicos é uma jornada complexa que exige dedicação, estratégia e acesso a materiais de qualidade. Os candidatos — concurseiros — precisam estudar diversos conteúdos, resolver milhares de questões e conhecer o perfil de cobrança das bancas examinadoras. **O problema ocorre principalmente no ambiente digital**, onde as informações sobre provas passadas estão dispersas em diversos sites, sem padronização ou organização sistemática.

**Quem é afetado:**
- **Estudantes e concurseiros:** Perdem tempo navegando por múltiplos sites para encontrar provas específicas
- **Professores e cursos preparatórios:** Têm dificuldade em organizar acervos de questões atualizadas
- **Instituições de ensino:** Necessitam de bancos de dados estruturados para análise pedagógica

### 2.2 Problema Central

Atualmente, os candidatos a concursos públicos enfrentam dificuldades significativas em:

1. **Localizar provas específicas** de forma rápida e eficiente
2. **Organizar materiais de estudo** de maneira estruturada
3. **Analisar padrões** de cobrança das bancas examinadoras
4. **Acompanhar novos concursos** e suas respectivas provas em tempo real

O site Aprova Concursos (aprovaconcursos.com.br) disponibiliza mais de **29.408 provas** de diversos órgãos públicos, mas a navegação manual página por página é ineficiente e não permite análises estatísticas ou comparativas[^2].

**Formulação clara do problema:**  
*"Atualmente, os concurseiros e professores têm dificuldade em acessar, organizar e analisar sistematicamente o vasto acervo de provas de concursos públicos disponíveis online, resultando em preparação menos eficiente e perda de oportunidades de aprendizado estratégico."*

### 2.3 Proposta de Solução

Para solucionar esse problema, propõe-se o **desenvolvimento de um sistema automatizado de web scraping** que:

1. **Coleta automaticamente** informações sobre provas de concursos públicos
2. **Organiza os dados** em formatos estruturados (CSV, JSON, Excel)
3. **Extrai metadados relevantes** como banca, órgão, cargo, nível, número de questões
4. **Disponibiliza links diretos** para provas em PDF e gabaritos
5. **Gera estatísticas** sobre tendências de concursos e bancas

O sistema permitirá que usuários:
- Busquem provas por filtros específicos (banca, órgão, ano, nível)
- Baixem conjuntos de provas de forma organizada
- Analisem padrões de cobrança através de dashboards
- Recebam notificações sobre novas provas via Telegram (funcionalidade futura)

---

## 3. Motivação

### 3.1 Importância do Problema

#### Dados Estatísticos

1. **Volume de concurseiros no Brasil:**  
   Segundo pesquisa da Associação Nacional de Proteção e Apoio aos Concursos (ANPAC), estima-se que **mais de 10 milhões de brasileiros** estão se preparando para concursos públicos atualmente[^3].

2. **Mercado de preparação:**  
   O mercado de cursos preparatórios movimenta aproximadamente **R$ 1,5 bilhão por ano** no Brasil, demonstrando a relevância econômica do setor (Valor Econômico, 2024)[^4].

3. **Taxa de aprovação:**  
   A taxa média de aprovação em concursos públicos é de apenas **2-5%**, evidenciando a alta competitividade e necessidade de preparação eficiente (Folha de São Paulo, 2023)[^5].

4. **Tempo de preparação:**  
   Candidatos aprovados estudam em média **8-12 meses** com dedicação diária de 4-6 horas, sendo a resolução de questões anteriores responsável por **40% da preparação efetiva**[^6].

#### Análise de Mercado

Plataformas como QConcursos, TEC Concursos e Aprova Concursos juntas acumulam **mais de 15 milhões de acessos mensais**, comprovando a demanda massiva por materiais de estudo organizados[^7].

### 3.2 Benefícios Esperados

#### Para Usuários Finais (Concurseiros)

- **Economia de tempo:** Redução de 70% no tempo gasto para localizar provas específicas
- **Organização:** Acesso a dados estruturados que facilitam a criação de planos de estudo
- **Análise estratégica:** Identificação de questões recorrentes e padrões das bancas
- **Gratuidade:** Democratização do acesso a informações que normalmente exigiriam assinaturas pagas

#### Para Professores e Instituições

- **Curadoria automatizada:** Base de dados atualizada automaticamente
- **Análise pedagógica:** Estatísticas sobre tendências de conteúdo cobrado
- **Economia operacional:** Redução de custos com equipes de organização manual de materiais

#### Para a Sociedade

- **Democratização do conhecimento:** Acesso igualitário a materiais de preparação
- **Transparência:** Melhoria na transparência dos processos seletivos públicos
- **Eficiência:** Servidores públicos mais bem preparados beneficiam toda a sociedade

---

## 4. Protótipo de Baixa Fidelidade

### 4.1 Interface de Linha de Comando (CLI) - Versão MVP

```
╔═══════════════════════════════════════════════════════════╗
║  SISTEMA DE COLETA DE PROVAS DE CONCURSOS PÚBLICOS       ║
╚═══════════════════════════════════════════════════════════╝

[1] Coletar provas automaticamente
[2] Filtrar por banca
[3] Filtrar por órgão
[4] Exportar dados (CSV/JSON/Excel)
[5] Estatísticas
[6] Configurações
[0] Sair

Escolha uma opção: _
```

### 4.2 Dashboard Web (Protótipo Futuro)

```
┌─────────────────────────────────────────────────────────┐
│  🎯 Dashboard - Provas de Concursos                     │
│  [Buscar]  [Filtros ▼]  [Notificações 🔔]  [Perfil]    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  📊 ESTATÍSTICAS GERAIS                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐               │
│  │  29.408  │ │  1.245   │ │  85.000  │               │
│  │  Provas  │ │  Órgãos  │ │ Questões │               │
│  └──────────┘ └──────────┘ └──────────┘               │
│                                                          │
│  📋 ÚLTIMAS PROVAS ADICIONADAS                          │
│  ┌──────────────────────────────────────────────┐      │
│  │ FCC - TRT 6ª Região - Técnico Judiciário     │      │
│  │ Data: 02/2025 | Questões: 50 | [PDF] [Gab]  │      │
│  ├──────────────────────────────────────────────┤      │
│  │ Cebraspe - ICMBIO - Analista Administrativo  │      │
│  │ Data: 03/2025 | Questões: 50 | [PDF] [Gab]  │      │
│  └──────────────────────────────────────────────┘      │
│                                                          │
│  🔍 BUSCA AVANÇADA                                      │
│  Banca: [Todas ▼]  Órgão: [Todos ▼]  Ano: [2025 ▼]   │
│  Nível: [Todos ▼]  [🔍 Buscar]                        │
└─────────────────────────────────────────────────────────┘
```

### 4.3 Fluxograma do Sistema

```
┌─────────────┐
│   INÍCIO    │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Acessar site-alvo  │
│  (aprovaconcursos)  │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Extrair HTML       │
│  (BeautifulSoup)    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Parsear dados:     │
│  • Título           │
│  • Banca            │
│  • Órgão            │
│  • Data             │
│  • Nível            │
│  • Nº Questões      │
│  • Links PDF        │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Armazenar em       │
│  estrutura de dados │
│  (JSON/CSV/Excel)   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Gerar estatísticas │
│  e relatórios       │
└──────┬──────────────┘
       │
       ▼
┌─────────────┐
│   FIM       │
└─────────────┘
```

### 4.4 Modelo de Dados

```
Prova {
  ├─ titulo: String
  ├─ link: URL
  ├─ banca: String
  ├─ orgao: String
  ├─ cargo: String
  ├─ ano: String
  ├─ nivel: String (Ensino Médio/Superior)
  ├─ data_aplicacao: String (MM/YYYY)
  ├─ num_questoes: Integer
  ├─ link_prova_pdf: URL
  ├─ link_gabarito_pdf: URL
  └─ data_coleta: DateTime
}
```

---

## 5. Estudo de Viabilidade

### 5.1 Web Scraping - Análise Técnica

#### Viabilidade Técnica: ✅ VIÁVEL

**Aspectos Positivos:**
- ✅ Site-alvo possui estrutura HTML bem definida
- ✅ Não há sistemas avançados de anti-scraping (CAPTCHA)
- ✅ Conteúdo é público e acessível sem login
- ✅ URLs seguem padrão previsível para paginação

**Tecnologias Utilizadas:**
```python
• Python 3.9+
• BeautifulSoup4 (parsing HTML)
• Requests (requisições HTTP)
• Pandas (manipulação de dados)
• Regex (extração de padrões)
```

**Desafios Identificados:**
1. **Paginação:** O site possui 981 páginas (29.408 provas ÷ 30 por página)
   - **Solução:** Implementar scraping incremental com delays
   
2. **Variação de layout:** Diferentes formatos de informação
   - **Solução:** Uso de regex flexíveis e tratamento de exceções
   
3. **Taxa de requisições:** Necessidade de respeitar o servidor
   - **Solução:** Delays de 2-3 segundos entre requisições
   
4. **Mudanças no site:** Estrutura HTML pode mudar
   - **Solução:** Sistema modular e logs de erro

**Taxa de Sucesso Estimada:** 85-90% de dados completos

#### Conformidade Legal

⚠️ **Considerações Importantes:**
- Os dados coletados são **públicos e acessíveis** sem restrições
- Uso deve respeitar **Termos de Uso** do site-alvo
- Implementar **robots.txt** compliance
- Não comercializar dados diretamente
- Respeitar direitos autorais das provas

**Status:** ✅ Viável para uso educacional e pessoal

### 5.2 PDF Scraping (Extensão Futura)

#### Viabilidade Técnica: ✅ VIÁVEL COM RESSALVAS

**Funcionalidades Propostas:**
- Extrair texto de PDFs de provas
- Identificar questões individuais
- Classificar por disciplina
- Extrair imagens de questões

**Tecnologias:**
```python
• PyPDF2 / PDFPlumber (extração de texto)
• Tesseract OCR (PDFs escaneados)
• OpenCV (processamento de imagens)
• spaCy / NLTK (classificação de disciplinas)
```

**Desafios:**
1. **Variação de formatos:** Cada banca usa layout diferente
2. **PDFs escaneados:** Necessitam OCR (maior taxa de erro)
3. **Questões com imagens:** Complexidade adicional
4. **Volume de processamento:** Milhares de PDFs para processar

**Taxa de Sucesso Estimada:** 60-70% (dependendo da qualidade dos PDFs)

**Status:** 🔶 Viável para MVP limitado, requer refinamento

### 5.3 Integração com Telegram

#### Viabilidade Técnica: ✅ ALTAMENTE VIÁVEL

**Funcionalidades Propostas:**

1. **Bot de Notificações:**
   - Alertar sobre novas provas de bancas favoritas
   - Enviar resumo diário de novas provas
   - Permitir busca por comandos

2. **Bot Interativo:**
   - `/buscar [banca] [órgão]` - Buscar provas específicas
   - `/estatisticas` - Mostrar estatísticas gerais
   - `/notificar [banca]` - Configurar alertas

**Tecnologias:**
```python
• python-telegram-bot (API oficial)
• SQLite / PostgreSQL (armazenamento de preferências)
• APScheduler (agendamento de notificações)
```

**Implementação Básica:**
```python
from telegram import Update
from telegram.ext import Application, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text(
        "🎯 Bem-vindo ao Bot de Concursos!\n"
        "Use /buscar para encontrar provas."
    )

async def buscar(update: Update, context):
    # Buscar provas no banco de dados
    # Enviar resultados formatados
    pass

app = Application.builder().token("TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buscar", buscar))
app.run_polling()
```

**Benefícios:**
- ✅ Facilita acesso móvel
- ✅ Notificações em tempo real
- ✅ Interface conversacional intuitiva
- ✅ Baixo custo de infraestrutura

**Status:** ✅ Altamente viável, baixa complexidade

### 5.4 Análise com Inteligência Artificial

#### Viabilidade Técnica: 🔶 VIÁVEL COM INVESTIMENTO

**Funcionalidades Propostas:**

1. **Classificação Automática de Questões**
   - Identificar disciplina e assunto
   - Classificar nível de dificuldade
   - Detectar questões similares

2. **Análise de Tendências**
   - Prever temas mais cobrados
   - Identificar padrões de bancas
   - Sugerir plano de estudos personalizado

3. **Geração de Conteúdo**
   - Resumir conteúdos de questões
   - Gerar explicações de gabaritos
   - Criar simulados personalizados

**Tecnologias:**

```python
# Modelos de ML/IA
• Scikit-learn (classificação básica)
• spaCy / BERT (processamento de linguagem)
• OpenAI API / Claude API (análise avançada)
• TensorFlow / PyTorch (modelos customizados)

# Dados
• NumPy, Pandas (manipulação)
• Matplotlib, Plotly (visualização)
```

**Caso de Uso: Classificação de Questões**

```python
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Carregar modelo de linguagem
nlp = spacy.load("pt_core_news_lg")

# Treinar classificador
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(questoes_texto)
y = disciplinas  # ['Matemática', 'Português', ...]

classificador = MultinomialNB()
classificador.fit(X, y)

# Classificar nova questão
nova_questao = "Calcule a derivada de f(x) = x²"
X_nova = vectorizer.transform([nova_questao])
disciplina = classificador.predict(X_nova)
# Output: 'Matemática'
```

**Caso de Uso: Análise com LLM (OpenAI/Claude)**

```python
import anthropic

client = anthropic.Anthropic(api_key="API_KEY")

def analisar_questao(texto_questao):
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Analise esta questão de concurso:
            
            {texto_questao}
            
            Identifique:
            1. Disciplina
            2. Assunto específico
            3. Nível de dificuldade
            4. Competências avaliadas"""
        }]
    )
    return message.content
```

**Desafios:**
1. **Custo computacional:** Processamento de milhares de questões
2. **Qualidade dos dados:** Necessidade de dataset rotulado
3. **APIs pagas:** OpenAI/Claude têm custos por token
4. **Acurácia:** Modelos podem errar em questões ambíguas

**Custos Estimados (APIs LLM):**
- OpenAI GPT-4: ~$0.03 por 1K tokens
- Anthropic Claude: ~$0.015 por 1K tokens
- Processar 10.000 questões: **$300-500** (estimativa)

**Alternativas de Baixo Custo:**
- Modelos locais (LLaMA, Mistral via Ollama)
- Classificadores tradicionais (sklearn)
- Regras baseadas em keywords

**Status:** 🔶 Viável para MVP com modelos simples, IA avançada requer investimento

---

## 6. Engenharia de Requisitos

Baseado nos princípios de Engenharia de Software Moderna[^8], os requisitos do sistema foram classificados em:

### 6.1 Requisitos Funcionais (RF)

#### RF01 - Coleta de Dados
- **RF01.1:** O sistema DEVE permitir a coleta automatizada de provas do site-alvo
- **RF01.2:** O sistema DEVE extrair: título, banca, órgão, cargo, ano, nível, data de aplicação, número de questões
- **RF01.3:** O sistema DEVE capturar links para PDFs de provas e gabaritos
- **RF01.4:** O sistema DEVE implementar paginação automática

#### RF02 - Armazenamento
- **RF02.1:** O sistema DEVE armazenar dados em formato JSON
- **RF02.2:** O sistema DEVE exportar dados para CSV
- **RF02.3:** O sistema DEVE exportar dados para Excel (.xlsx)
- **RF02.4:** O sistema DEVE registrar data/hora de coleta

#### RF03 - Busca e Filtros
- **RF03.1:** O sistema DEVE permitir filtrar provas por banca
- **RF03.2:** O sistema DEVE permitir filtrar provas por órgão
- **RF03.3:** O sistema DEVE permitir filtrar provas por ano
- **RF03.4:** O sistema DEVE permitir filtrar provas por nível de escolaridade

#### RF04 - Estatísticas
- **RF04.1:** O sistema DEVE gerar estatísticas sobre bancas mais frequentes
- **RF04.2:** O sistema DEVE calcular total de questões disponíveis
- **RF04.3:** O sistema DEVE exibir média de questões por prova
- **RF04.4:** O sistema DEVE listar órgãos mais recorrentes

#### RF05 - Notificações (Futuro)
- **RF05.1:** O sistema PODERÁ enviar notificações via Telegram
- **RF05.2:** O sistema PODERÁ permitir configuração de alertas personalizados

### 6.2 Requisitos Não-Funcionais (RNF)

#### RNF01 - Desempenho
- **RNF01.1:** O sistema DEVE processar no mínimo 20 provas por minuto
- **RNF01.2:** O sistema DEVE implementar delay de 2 segundos entre requisições
- **RNF01.3:** O sistema NÃO DEVE consumir mais de 500MB de RAM

#### RNF02 - Confiabilidade
- **RNF02.1:** O sistema DEVE ter taxa de sucesso mínima de 85% na coleta
- **RNF02.2:** O sistema DEVE registrar erros em arquivo de log
- **RNF02.3:** O sistema DEVE permitir retomada após falhas

#### RNF03 - Usabilidade
- **RNF03.1:** O sistema DEVE ter interface CLI intuitiva
- **RNF03.2:** O sistema DEVE exibir progresso da coleta em tempo real
- **RNF03.3:** O sistema DEVE fornecer mensagens de erro claras

#### RNF04 - Manutenibilidade
- **RNF04.1:** O código DEVE seguir padrões PEP 8 (Python)
- **RNF04.2:** O sistema DEVE ser modular (classes e funções separadas)
- **RNF04.3:** O sistema DEVE ter documentação inline (docstrings)

#### RNF05 - Portabilidade
- **RNF05.1:** O sistema DEVE funcionar em Windows, Linux e macOS
- **RNF05.2:** O sistema DEVE usar Python 3.9 ou superior
- **RNF05.3:** O sistema DEVE listar dependências em requirements.txt

#### RNF06 - Segurança
- **RNF06.1:** O sistema NÃO DEVE armazenar credenciais em código
- **RNF06.2:** O sistema DEVE respeitar robots.txt do site-alvo
- **RNF06.3:** O sistema DEVE implementar User-Agent apropriado

### 6.3 Regras de Negócio (RN)

- **RN01:** Dados coletados são apenas para uso educacional
- **RN02:** Sistema não deve comercializar dados diretamente
- **RN03:** Provas permanecem propriedade das bancas/órgãos originais
- **RN04:** Sistema deve respeitar limite de requisições do servidor

---

## 7. Histórias de Usuários

Seguindo a metodologia ágil descrita em Engenharia de Software Moderna[^8], Seção 3.3:

### História 1: Coletar Provas Automaticamente
**Como** concurseiro  
**Eu quero** coletar automaticamente provas de concursos  
**Para que** eu possa economizar tempo e ter acesso a um grande volume de materiais

**Critérios de Aceitação:**
- [ ] O sistema coleta no mínimo 50 provas por execução
- [ ] Os dados incluem título, banca, órgão e links para PDF
- [ ] O processo é completado em menos de 5 minutos
- [ ] Progresso é exibido em tempo real

**Prioridade:** ALTA  
**Estimativa:** 8 pontos

---

### História 2: Filtrar Provas por Banca
**Como** concurseiro  
**Eu quero** filtrar provas por banca examinadora específica  
**Para que** eu possa estudar o padrão de cobrança da minha banca-alvo

**Critérios de Aceitação:**
- [ ] Sistema lista todas as bancas disponíveis
- [ ] Filtro retorna apenas provas da banca selecionada
- [ ] Resultados são exportáveis em CSV
- [ ] Tempo de resposta menor que 2 segundos

**Prioridade:** ALTA  
**Estimativa:** 5 pontos

---

### História 3: Exportar Dados em Múltiplos Formatos
**Como** professor de curso preparatório  
**Eu quero** exportar dados em CSV, JSON e Excel  
**Para que** eu possa usar em diferentes ferramentas de análise

**Critérios de Aceitação:**
- [ ] Exportação em JSON preserva estrutura completa
- [ ] CSV é compatível com Excel (UTF-8 BOM)
- [ ] Excel tem colunas formatadas corretamente
- [ ] Arquivos são salvos no diretório atual

**Prioridade:** MÉDIA  
**Estimativa:** 3 pontos

---

### História 4: Visualizar Estatísticas
**Como** analista de dados educacionais  
**Eu quero** visualizar estatísticas sobre provas coletadas  
**Para que** eu possa identificar tendências de mercado

**Critérios de Aceitação:**
- [ ] Sistema exibe top 10 bancas mais frequentes
- [ ] Sistema calcula total de questões disponíveis
- [ ] Sistema mostra distribuição por nível de escolaridade
- [ ] Estatísticas são atualizadas automaticamente

**Prioridade:** MÉDIA  
**Estimativa:** 5 pontos

---

### História 5: Receber Notificações de Novas Provas (Futuro)
**Como** concurseiro  
**Eu quero** receber notificações no Telegram sobre novas provas  
**Para que** eu possa me manter atualizado sem precisar verificar manualmente

**Critérios de Aceitação:**
- [ ] Bot do Telegram responde a comandos básicos
- [ ] Usuário pode configurar bancas de interesse
- [ ] Notificações são enviadas em até 1 hora da publicação
- [ ] Mensagens incluem link direto para a prova

**Prioridade:** BAIXA (MVP+1)  
**Estimativa:** 13 pontos

---

### História 6: Buscar Provas por Palavras-Chave
**Como** concurseiro  
**Eu quero** buscar provas por palavras-chave (ex: "Analista TI")  
**Para que** eu possa encontrar provas relevantes rapidamente

**Critérios de Aceitação:**
- [ ] Busca funciona em títulos e cargos
- [ ] Busca é case-insensitive
- [ ] Resultados são ordenados por relevância
- [ ] Tempo de resposta menor que 3 segundos

**Prioridade:** MÉDIA  
**Estimativa:** 8 pontos

---

## 8. Minimum Viable Product (MVP)

### 8.1 Definição do MVP

O **MVP (Produto Mínimo Viável)** é a versão mais simples do sistema que entrega valor imediato aos usuários, permitindo validação da proposta e coleta de feedback para iterações futuras.

### 8.2 Funcionalidades do MVP

#### ✅ Incluídas no MVP

1. **Web Scraping Básico**
   - Coletar dados de 3-5 páginas do site (90-150 provas)
   - Extrair metadados essenciais: título, banca, órgão, nível, data, links PDF
   - Implementar tratamento básico de erros

2. **Exportação de Dados**
   - Formato JSON (estruturado)
   - Formato CSV (compatível Excel)
   - Formato Excel (.xlsx) - opcional se openpyxl estiver instalado

3. **Estatísticas Básicas**
   - Total de provas coletadas
   - Top 10 bancas
   - Top 10 órgãos
   - Distribuição por nível de escolaridade
   - Total de questões disponíveis

4. **Interface CLI Simples**
   - Execução via linha de comando
   - Feedback de progresso em tempo real
   - Mensagens de erro claras

#### ❌ Não Incluídas no MVP (Backlog Futuro)

1. **PDF Scraping** - Complexidade adicional
2. **Integração com Telegram** - Requer infraestrutura de bot
3. **Dashboard Web** - Requer frontend
4. **Análise com IA** - Requer modelos e dataset
5. **Banco de Dados Relacional** - MVP usa arquivos JSON/CSV
6. **Sistema de Busca Avançada** - MVP permite filtros manuais nos arquivos exportados
7. **Agendamento Automático** - MVP é executado manualmente

### 8.3 Tecnologias do MVP

```
Backend:
- Python 3.9+
- requests (HTTP)
- beautifulsoup4 (HTML parsing)
- pandas (manipulação dados)
- openpyxl (Excel - opcional)

Armazenamento:
- Arquivos JSON
- Arquivos CSV
- Arquivos Excel

Infraestrutura:
- Sistema operacional: Windows/Linux/macOS
- Sem servidor necessário (execução local)
- Sem banco de dados externo
```

### 8.4 Métricas de Sucesso do MVP

| Métrica | Meta |
|---------|------|
| Taxa de sucesso na coleta | ≥ 85% |
| Tempo de coleta (100 provas) | ≤ 5 minutos |
| Completude dos dados | ≥ 80% dos campos preenchidos |
| Satisfação dos usuários | ≥ 4/5 em pesquisa |
| Bugs críticos | 0 |

### 8.5 Cronograma do MVP

```
Semana 1-2: Desenvolvimento
├─ Dia 1-3: Implementação do scraper básico
├─ Dia 4-5: Sistema de exportação (JSON/CSV/Excel)
├─ Dia 6-7: Estatísticas e interface CLI
└─ Dia 8-9: Testes e correções

Semana 3: Validação
├─ Dia 10-12: Testes com usuários beta
├─ Dia 13-14: Ajustes baseados em feedback
└─ Dia 15: Lançamento do MVP

Semana 4+: Iterações
├─ Análise de métricas
├─ Priorização do backlog
└─ Planejamento MVP+1
```

### 8.6 Critérios de Aceitação do MVP

✅ **MVP está pronto quando:**

1. [ ] Sistema coleta dados de no mínimo 3 páginas sem falhas críticas
2. [ ] Todos os metadados essenciais são extraídos corretamente
3. [ ] Exportação em JSON e CSV funciona sem erros
4. [ ] Estatísticas básicas são calculadas e exibidas
5. [ ] Código segue padrões de qualidade (PEP 8)
6. [ ] Documentação básica está completa (README.md)
7. [ ] Sistema foi testado em Windows, Linux ou macOS
8. [ ] Dependências estão listadas em requirements.txt

### 8.7 Próximas Iterações (Roadmap)

**MVP+1 (Versão 1.1)** - Estimativa: 2-3 semanas
- Dashboard web básico (Flask/Streamlit)
- Banco de dados SQLite
- Sistema de busca por filtros

**MVP+2 (Versão 1.2)** - Estimativa: 3-4 semanas
- Bot do Telegram para notificações
- Agendamento automático de coletas
- API REST para acesso aos dados

**MVP+3 (Versão 2.0)** - Estimativa: 6-8 semanas
- PDF scraping básico
- Classificação de questões com ML
- Interface web completa com autenticação

---

## 9. Arquitetura do Sistema

### 9.1 Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────┐
│                  CAMADA DE INTERFACE                │
│  ┌──────────────┐  ┌──────────────┐                │
│  │  CLI (MVP)   │  │ Web (Futuro) │                │
│  └──────┬───────┘  └──────┬───────┘                │
└─────────┼──────────────────┼──────────────────────────┘
          │                  │
┌─────────┼──────────────────┼──────────────────────────┐
│         ▼                  ▼   CAMADA DE LÓGICA      │
│  ┌────────────────────────────────────┐              │
│  │      ConcursoScraper Class         │              │
│  ├────────────────────────────────────┤              │
│  │ • scrape_pagina()                  │              │
│  │ • scrape_multiplas_paginas()       │              │
│  │ • extrair_numero_questoes()        │              │
│  │ • salvar_json/csv/excel()          │              │
│  │ • exibir_estatisticas()            │              │
│  └────────────┬───────────────────────┘              │
└───────────────┼──────────────────────────────────────┘
                │
┌───────────────┼──────────────────────────────────────┐
│               ▼          CAMADA DE DADOS             │
│  ┌──────────────┐  ┌──────────────┐                 │
│  │ JSON Files   │  │  CSV Files   │                 │
│  └──────────────┘  └──────────────┘                 │
│  ┌──────────────┐                                    │
│  │ Excel Files  │                                    │
│  └──────────────┘                                    │
└─────────────────────────────────────────────────────┘
                │
┌───────────────┼──────────────────────────────────────┐
│               ▼       SERVIÇOS EXTERNOS              │
│  ┌────────────────────────────────────┐              │
│  │  aprovaconcursos.com.br (HTML)     │              │
│  └────────────────────────────────────┘              │
│  ┌────────────────────────────────────┐              │
│  │  S3 Amazon (PDFs) - Links          │              │
│  └────────────────────────────────────┘              │
└─────────────────────────────────────────────────────┘
```

### 9.2 Padrões de Projeto Utilizados

1. **Singleton (implícito):** Classe ConcursoScraper gerencia estado único
2. **Strategy:** Diferentes métodos de exportação (JSON, CSV, Excel)
3. **Template Method:** Fluxo de scraping padronizado com variações

---

## 10. Testes e Validação

### 10.1 Estratégia de Testes

```python
# Teste unitário exemplo
def test_extrair_numero_questoes():
    scraper = ConcursoScraper()
    assert scraper.extrair_numero_questoes("50 Questões") == 50
    assert scraper.extrair_numero_questoes("100 Questões") == 100
    assert scraper.extrair_numero_questoes("Sem questões") == 0

# Teste de integração exemplo
def test_scrape_pagina():
    scraper = ConcursoScraper()
    sucesso = scraper.scrape_pagina(1)
    assert sucesso == True
    assert len(scraper.provas) > 0
```

### 10.2 Casos de Teste

| ID | Caso de Teste | Entrada | Saída Esperada |
|----|---------------|---------|----------------|
| TC01 | Scraping página válida | Página 1 | Lista com 30 provas |
| TC02 | Extração de metadados | HTML de prova | Dicionário completo |
| TC03 | Exportação JSON | Lista de provas | Arquivo .json válido |
| TC04 | Exportação CSV | Lista de provas | Arquivo .csv válido |
| TC05 | Estatísticas | 100 provas | Contagens corretas |

---

## 11. Considerações Finais

### 11.1 Limitações do Sistema

1. **Dependência do site-alvo:** Mudanças no HTML quebram o scraper
2. **Sem dados históricos:** Apenas provas atualmente disponíveis
3. **Sem análise de conteúdo:** MVP não processa questões individuais
4. **Execução manual:** Não há agendamento automático

### 11.2 Trabalhos Futuros

1. Implementar monitoramento contínuo do site
2. Desenvolver sistema de versionamento de dados
3. Criar API pública para acesso aos dados
4. Expandir para outros sites de concursos
5. Implementar análise preditiva com machine learning

### 11.3 Contribuições Esperadas

Este projeto contribui para:

- **Democratização do acesso à educação** para concursos públicos
- **Transparência** nos processos seletivos públicos
- **Pesquisa acadêmica** sobre padrões de avaliação
- **Desenvolvimento de tecnologias educacionais** no Brasil

---

## 12. Referências

[^1]: IBGE - Instituto Brasileiro de Geografia e Estatística. Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua), 2023. Disponível em: https://www.ibge.gov.br/

[^2]: Aprova Concursos. Questões de Concurso - Provas. Disponível em: https://www.aprovaconcursos.com.br/questoes-de-concurso/provas. Acesso em: 03 fev. 2026.

[^3]: ANPAC - Associação Nacional de Proteção e Apoio aos Concursos. Pesquisa sobre Concurseiros no Brasil, 2024. Disponível em: https://www.anpac.org.br/

[^4]: Valor Econômico. Mercado de cursos preparatórios para concursos movimenta R$ 1,5 bilhão. São Paulo, 15 mar. 2024.

[^5]: Folha de São Paulo. Taxa de aprovação em concursos públicos é de 2% a 5%, diz estudo. São Paulo, 22 jul. 2023.

[^6]: QConcursos. Pesquisa: Como estudam os aprovados em concursos públicos. Rio de Janeiro, 2024. Disponível em: https://www.qconcursos.com/

[^7]: SimilarWeb. Análise de tráfego de sites de concursos públicos - Brasil, 2025. Disponível em: https://www.similarweb.com/

[^8]: VALENTE, Marco Tulio. Engenharia de Software Moderna: Princípios e Práticas para Desenvolvimento de Software com Produtividade. Disponível em: https://engsoftmoderna.info/cap3.html. Acesso em: 03 fev. 2026.

---

## Anexos

### Anexo A - Estrutura de Diretórios

```
PDSI1 Web Scraping/
├── scraper.py                    # Script principal
├── requirements.txt              # Dependências
├── DOCUMENTACAO_PROJETO.md       # Este documento
├── README.md                     # Instruções de uso
├── dados/                        # Diretório de dados (gerado)
│   ├── provas_concursos.json
│   ├── provas_concursos.csv
│   └── provas_concursos.xlsx
├── logs/                         # Logs de execução (futuro)
│   └── scraper.log
└── tests/                        # Testes automatizados (futuro)
    ├── test_scraper.py
    └── test_exportacao.py
```

### Anexo B - Exemplo de Dados Coletados

```json
{
  "titulo": "FCC - 2024 - TRT - 6ª Região (PE) - Técnico Judiciário",
  "link": "https://www.aprovaconcursos.com.br/questoes-de-concurso/prova/...",
  "banca": "FCC",
  "orgao": "TRT - 6ª Região (PE) - 2024",
  "cargo": "Técnico Judiciário - Administrativo",
  "ano": "2024",
  "nivel": "Superior Completo",
  "data_aplicacao": "02/2025",
  "num_questoes": 50,
  "link_prova_pdf": "https://s3.amazonaws.com/.../prova/49373.pdf",
  "link_gabarito_pdf": "https://s3.amazonaws.com/.../gabarito/49373.pdf",
  "data_coleta": "2026-02-03 14:30:00"
}
```

### Anexo C - Glossário

- **Web Scraping:** Técnica de extração automatizada de dados de websites
- **BeautifulSoup:** Biblioteca Python para parsing de HTML/XML
- **MVP:** Minimum Viable Product - Produto Mínimo Viável
- **CLI:** Command Line Interface - Interface de Linha de Comando
- **API:** Application Programming Interface
- **OCR:** Optical Character Recognition - Reconhecimento Óptico de Caracteres
- **LLM:** Large Language Model - Modelo de Linguagem Grande
- **Bot:** Programa automatizado que executa tarefas repetitivas
- **Dataset:** Conjunto de dados estruturados

---

**Documento gerado em:** 03 de Fevereiro de 2026  
**Versão:** 1.0  
**Autor:** Leonardo  
**Disciplina:** PDSI1 - Projeto e Desenvolvimento de Sistemas I
