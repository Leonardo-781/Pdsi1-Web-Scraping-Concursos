"""
Bot Telegram Completo para Busca de Provas de Concursos
Funcionalidades: Busca por banca, órgão, cargo, ano, estatísticas
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
import json
import pandas as pd
from datetime import datetime

class ConcursosBot:
    """Bot do Telegram para notificações de provas de concursos"""
    
    def __init__(self, token: str):
        self.token = token
        self.app = Application.builder().token(token).build()
        self.dados_provas = []
        self._carregar_dados()
        self._registrar_comandos()
    
    def _carregar_dados(self):
        """Carrega dados das provas coletadas"""
        try:
            with open('provas_concursos.json', 'r', encoding='utf-8') as f:
                self.dados_provas = json.load(f)
            print(f"✓ {len(self.dados_provas)} provas carregadas")
        except FileNotFoundError:
            print("⚠ Arquivo de dados não encontrado. Execute o scraper primeiro.")
    
    def _registrar_comandos(self):
        """Registra todos os comandos do bot"""
        self.app.add_handler(CommandHandler("start", self.comando_start))
        self.app.add_handler(CommandHandler("ajuda", self.comando_ajuda))
        self.app.add_handler(CommandHandler("menu", self.comando_menu))
        self.app.add_handler(CommandHandler("estatisticas", self.comando_estatisticas))
        self.app.add_handler(CommandHandler("buscar", self.comando_buscar))
        self.app.add_handler(CommandHandler("filtro", self.comando_filtro))
        self.app.add_handler(CommandHandler("bancas", self.comando_bancas))
        self.app.add_handler(CommandHandler("orgaos", self.comando_orgaos))
        self.app.add_handler(CommandHandler("cargos", self.comando_cargos))
        self.app.add_handler(CommandHandler("anos", self.comando_anos))
        self.app.add_handler(CommandHandler("provas_recentes", self.comando_recentes))
        self.app.add_handler(CallbackQueryHandler(self.botao_callback))
    
    async def comando_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start - Mensagem de boas-vindas"""
        mensagem = """
🎯 **Bem-vindo ao Bot de Concursos Públicos!**

Este bot ajuda você a encontrar provas de concursos públicos de forma rápida e fácil.

📚 **O que você pode fazer:**

🔍 **Buscar Provas** - /buscar [banca]
   Exemplo: /buscar FGV

📊 **Ver Estatísticas** - /estatisticas
   Total de provas, bancas, órgãos, questões

🏛️ **Listar Bancas** - /bancas
   Ver todas as bancas disponíveis

🏢 **Listar Órgãos** - /orgaos
   Ver todos os órgãos públicos

💼 **Listar Cargos** - /cargos
   Ver todos os cargos disponíveis

📅 **Listar Anos** - /anos
   Ver todos os anos de provas

🆕 **Provas Recentes** - /provas_recentes
   Últimas provas adicionadas

🔧 **Menu Filtros** - /menu
   Usar botões para buscar

❓ **Ajuda** - /ajuda
   Ver lista completa de comandos

👉 Use /menu para começar!
        """
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_ajuda(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /ajuda - Exibe ajuda"""
        mensagem = """
📚 **LISTA COMPLETA DE COMANDOS**

🔍 **BUSCA DE PROVAS:**
/buscar [banca] - Buscar por banca
  Exemplo: /buscar FGV
  
/filtro - Filtro avançado (múltiplos critérios)
  
/cargos - Buscar por cargo
  
/anos - Buscar por ano
  
/provas_recentes - Últimas provas adicionadas

📊 **INFORMAÇÕES:**
/estatisticas - Estatísticas gerais (total, top bancas, etc)

/bancas - Lista todas as bancas

/orgaos - Lista todos os órgãos públicos

/anos - Lista todos os anos disponíveis

🎮 **INTERFACE:**
/menu - Menu interativo com botões

/ajuda - Esta mensagem

❓ **EXEMPLOS:**
• /buscar FCC - encontra provas da banca FCC
• /filtro orgao IBAMA - provas do IBAMA
• /provas_recentes - últimas 10 provas coletadas

💡 **DICA:** Use /menu para uma navegação mais fácil!
        """
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_estatisticas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /estatisticas - Mostra estatísticas gerais"""
        if not self.dados_provas:
            await update.message.reply_text("⚠ Nenhuma prova disponível no momento.")
            return
        
        df = pd.DataFrame(self.dados_provas)
        
        total_provas = len(self.dados_provas)
        total_questoes = df['num_questoes'].sum()
        media_questoes = df['num_questoes'].mean()
        
        bancas_top = df['banca'].value_counts().head(5)
        orgaos_top = df['orgao'].value_counts().head(5)
        
        mensagem = f"""
📊 **ESTATÍSTICAS GERAIS**

📋 Total de provas: **{total_provas}**
❓ Total de questões: **{total_questoes}**
📈 Média de questões/prova: **{media_questoes:.1f}**

🏛️ **Top 5 Bancas:**
{self._formatar_lista(bancas_top)}

🏢 **Top 5 Órgãos:**
{self._formatar_lista(orgaos_top)}

📅 Última atualização: {df['data_coleta'].iloc[0] if len(df) > 0 else 'N/A'}
        """
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_buscar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /buscar - Busca provas por banca"""
        if not context.args:
            await update.message.reply_text(
                "ℹ️ Uso: /buscar [nome_da_banca]\n"
                "Exemplo: /buscar FCC\n\n"
                "Use /buscar [banca] [número] para ver detalhes completos\n"
                "Exemplo: /buscar FCC 1"
            )
            return
        
        banca_busca = context.args[0].upper()
        numero_detalhes = None
        
        # Verificar se quer detalhes de uma prova específica
        if len(context.args) > 1:
            try:
                numero_detalhes = int(context.args[1]) - 1
            except ValueError:
                pass
        
        provas_filtradas = [
            p for p in self.dados_provas 
            if banca_busca in p.get('banca', '').upper()
        ]
        
        if not provas_filtradas:
            await update.message.reply_text(
                f"❌ Nenhuma prova encontrada para a banca '{banca_busca}'"
            )
            return
        
        # Se pediu detalhes de uma prova específica
        if numero_detalhes is not None and 0 <= numero_detalhes < len(provas_filtradas):
            prova = provas_filtradas[numero_detalhes]
            mensagem = f"""
📋 **DETALHES COMPLETOS DA PROVA**

**Título:** {prova.get('titulo', 'N/A')}
**Banca:** {prova.get('banca', 'N/A')}
**Órgão:** {prova.get('orgao', 'N/A')}
**Cargo:** {prova.get('cargo', 'N/A')}
**Ano:** {prova.get('ano', 'N/A')}
**Nível:** {prova.get('nivel', 'N/A') or 'Não informado'}
**Data de Aplicação:** {prova.get('data_aplicacao', 'N/A') or 'Não informada'}
**Número de Questões:** {prova.get('num_questoes', 0)}

📥 **DOWNLOADS:**
📄 [Ver Prova (PDF)]({prova.get('link_prova_pdf', 'Indisponível')})
✅ [Ver Gabarito (PDF)]({prova.get('link_gabarito_pdf', 'Indisponível')})

🔗 [Ver no site]({prova.get('link', 'N/A')})

📅 Coletado em: {prova.get('data_coleta', 'N/A')}
            """
            await update.message.reply_text(mensagem, parse_mode='Markdown')
            return
        
        # Mostrar lista de resultados
        provas_mostrar = provas_filtradas[:10]
        
        mensagem = f"🔍 **Resultados para '{banca_busca}' ({len(provas_filtradas)} encontradas)**\n\n"
        
        for i, prova in enumerate(provas_mostrar, 1):
            mensagem += f"""
**{i}. {prova.get('titulo', 'Sem título')[:60]}...**
🏢 Órgão: {prova.get('orgao', 'N/A')[:30]}
📅 Data: {prova.get('data_aplicacao', 'N/A')}
❓ Questões: {prova.get('num_questoes', 0)}

_Digite: /buscar {banca_busca} {i} para ver detalhes_

---
            """
        
        if len(provas_filtradas) > 10:
            mensagem += f"\n_...e mais {len(provas_filtradas) - 10} provas_"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_bancas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /bancas - Lista todas as bancas"""
        if not self.dados_provas:
            await update.message.reply_text("⚠ Nenhuma prova disponível.")
            return
        
        df = pd.DataFrame(self.dados_provas)
        bancas = df['banca'].value_counts()
        
        mensagem = "🏛️ **BANCAS DISPONÍVEIS**\n\n"
        for banca, count in bancas.head(20).items():
            mensagem += f"• {banca}: **{count}** provas\n"
        
        if len(bancas) > 20:
            mensagem += f"\n_...e mais {len(bancas) - 20} bancas_"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_orgaos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /orgaos - Lista todos os órgãos"""
        if not self.dados_provas:
            await update.message.reply_text("⚠ Nenhuma prova disponível.")
            return
        
        df = pd.DataFrame(self.dados_provas)
        orgaos = df['orgao'].value_counts()
        
        mensagem = "🏢 **ÓRGÃOS DISPONÍVEIS**\n\n"
        for orgao, count in orgaos.head(20).items():
            mensagem += f"• {orgao}: **{count}** provas\n"
        
        if len(orgaos) > 20:
            mensagem += f"\n_...e mais {len(orgaos) - 20} órgãos_"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    def _formatar_lista(self, series):
        """Formata uma Series do pandas como lista"""
        return '\n'.join([f"{i}. {nome}: **{count}**" 
                         for i, (nome, count) in enumerate(series.items(), 1)])
    
    def iniciar(self):
        """Inicia o bot"""
        print("🤖 Bot iniciado! Pressione Ctrl+C para parar.")
        self.app.run_polling()


def main():
    """Função principal"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║  BOT TELEGRAM - CONCURSOS PÚBLICOS (PROTÓTIPO)           ║
╚═══════════════════════════════════════════════════════════╝

⚠️  ATENÇÃO: Este é um protótipo conceitual!

Para usar este bot, você precisa:

1. Criar um bot no Telegram via @BotFather
2. Obter o token do bot
3. Instalar dependências:
   pip install python-telegram-bot

4. Configurar o token no código:
   TOKEN = "seu_token_aqui"

5. Executar o scraper primeiro:
   python scraper.py

6. Executar este bot:
   python bot_telegram.py

Para mais informações, consulte:
https://github.com/python-telegram-bot/python-telegram-bot

╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Token do bot
    TOKEN = "8395435303:AAHjp-Zp6Oid3uR4iscq29fFr_N9Tvg09eM"
    
    print("\n✅ Token configurado! Iniciando bot...")
    
    # Iniciar o bot
    bot = ConcursosBot(TOKEN)
    bot.iniciar()


if __name__ == "__main__":
    main()
