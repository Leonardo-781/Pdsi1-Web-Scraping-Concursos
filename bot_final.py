"""
Bot Telegram Simples e Funcional para Concursos
Versão otimizada e estável
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters, CallbackQueryHandler
import json
import pandas as pd

# Estados da conversa
ESPERANDO_BANCA, ESPERANDO_ORGAO, ESPERANDO_CARGO, ESPERANDO_ANO = range(4)

class BotConcursos:
    """Bot do Telegram para buscar provas"""
    
    def __init__(self, token):
        self.token = token
        self.dados = []
        self.df = None
        self._carregar_dados()
    
    def _carregar_dados(self):
        """Carrega os dados das provas"""
        try:
            with open('provas_concursos.json', 'r', encoding='utf-8') as f:
                self.dados = json.load(f)
            self.df = pd.DataFrame(self.dados)
            print(f"✓ {len(self.dados)} provas carregadas")
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")
    
    def criar_app(self):
        """Cria e configura o aplicação do bot"""
        app = Application.builder().token(self.token).build()
        
        # Comandos simples
        app.add_handler(CommandHandler("start", self.cmd_start))
        app.add_handler(CommandHandler("ajuda", self.cmd_ajuda))
        app.add_handler(CommandHandler("menu", self.cmd_menu))
        app.add_handler(CommandHandler("estatisticas", self.cmd_stats))
        app.add_handler(CommandHandler("bancas", self.cmd_bancas))
        app.add_handler(CommandHandler("orgaos", self.cmd_orgaos))
        app.add_handler(CommandHandler("cargos", self.cmd_cargos))
        app.add_handler(CommandHandler("anos", self.cmd_anos))
        app.add_handler(CommandHandler("buscar", self.cmd_buscar))
        
        # Callbacks dos botões
        app.add_handler(CallbackQueryHandler(self.handle_button))
        
        # Mensagens de texto
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        return app
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start"""
        msg = """🎯 **BEM-VINDO!**

Este bot ajuda você a buscar provas de concursos públicos.

**Como começar:**
👉 Use /menu para uma navegação fácil com botões
📖 Use /ajuda para ver todos os comandos

**Comandos principais:**
• /buscar FGV - busca provas da FGV
• /estatisticas - dados gerais
• /bancas - ver todas as bancas
• /menu - menu interativo"""
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def cmd_ajuda(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /ajuda"""
        msg = """📚 **COMANDOS DISPONÍVEIS**

🔍 **BUSCAR:**
/buscar [termo] - busca por banca (ex: /buscar FGV)
/orgaos - buscar por órgão
/cargos - buscar por cargo
/anos - buscar por ano

📊 **VER:**
/estatisticas - estatísticas gerais
/bancas - todas as bancas
/orgaos - todos os órgãos
/cargos - top cargos
/anos - anos disponíveis

🎮 **INTERFACE:**
/menu - menu com botões (RECOMENDADO!)
/ajuda - esta mensagem"""
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def cmd_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /menu - Menu interativo"""
        keyboard = [
            [InlineKeyboardButton("🔍 Buscar Banca", callback_data="buscar_banca")],
            [InlineKeyboardButton("🏢 Buscar Órgão", callback_data="buscar_orgao")],
            [InlineKeyboardButton("💼 Buscar Cargo", callback_data="buscar_cargo")],
            [InlineKeyboardButton("📅 Buscar Ano", callback_data="buscar_ano")],
            [InlineKeyboardButton("📊 Estatísticas", callback_data="stats")],
            [InlineKeyboardButton("🏛️ Ver Bancas", callback_data="bancas_list")]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "🎯 **MENU PRINCIPAL**\n\nEscolha uma opção:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    async def handle_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Processa cliques nos botões"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "buscar_banca":
            await query.edit_message_text("📝 Digite o nome da banca (ex: FGV)")
            context.user_data['mode'] = 'banca'
        
        elif query.data == "buscar_orgao":
            await query.edit_message_text("📝 Digite o nome do órgão (ex: IBAMA)")
            context.user_data['mode'] = 'orgao'
        
        elif query.data == "buscar_cargo":
            await query.edit_message_text("📝 Digite o nome do cargo (ex: Analista)")
            context.user_data['mode'] = 'cargo'
        
        elif query.data == "buscar_ano":
            await query.edit_message_text("📝 Digite o ano (ex: 2024)")
            context.user_data['mode'] = 'ano'
        
        elif query.data == "stats":
            df_com_questoes = self.df[self.df['num_questoes'] > 0]
            
            total = len(df_com_questoes)
            total_q = df_com_questoes['num_questoes'].sum()
            media = df_com_questoes['num_questoes'].mean()
            
            msg = f"""📊 **ESTATÍSTICAS (Apenas com Questões)**

📋 Total de provas: **{total}**
❓ Total de questões: **{total_q}**
📈 Média: **{media:.1f}** questões/prova

🏛️ **Top 5 Bancas:**
"""
            for banca, count in df_com_questoes['banca'].value_counts().head(5).items():
                msg += f"  • {banca}: {count}\n"
            
            await query.edit_message_text(msg, parse_mode='Markdown')
        
        elif query.data == "bancas_list":
            df_com_questoes = self.df[self.df['num_questoes'] > 0]
            
            msg = "🏛️ **BANCAS (com Questões)**\n\n"
            for i, (banca, count) in enumerate(df_com_questoes['banca'].value_counts().items(), 1):
                msg += f"{i}. {banca}: **{count}** provas\n"
            
            await query.edit_message_text(msg, parse_mode='Markdown')
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Processa mensagens de texto"""
        if 'mode' not in context.user_data:
            return
        
        mode = context.user_data.pop('mode')
        termo = update.message.text.strip()
        
        if mode == 'banca':
            await self._buscar_banca(update, termo)
        elif mode == 'orgao':
            await self._buscar_orgao(update, termo)
        elif mode == 'cargo':
            await self._buscar_cargo(update, termo)
        elif mode == 'ano':
            await self._buscar_ano(update, termo)
    
    async def cmd_buscar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /buscar"""
        if not context.args:
            await update.message.reply_text("Use: /buscar [termo]\n\nExemplos:\n• /buscar FGV\n• /buscar Cebraspe\n• /buscar FCC")
            return
        
        termo = ' '.join(context.args)
        await self._buscar_banca(update, termo)
    
    async def _buscar_banca(self, update: Update, termo: str):
        """Busca por banca"""
        resultados = [p for p in self.dados 
                     if termo.upper() in p.get('banca', '').upper() 
                     and p.get('num_questoes', 0) > 0]
        await self._enviar_resultados(update, resultados, f"🏛️ Banca: {termo}")
    
    async def _buscar_orgao(self, update: Update, termo: str):
        """Busca por órgão"""
        resultados = [p for p in self.dados 
                     if termo.upper() in p.get('orgao', '').upper()
                     and p.get('num_questoes', 0) > 0]
        await self._enviar_resultados(update, resultados, f"🏢 Órgão: {termo}")
    
    async def _buscar_cargo(self, update: Update, termo: str):
        """Busca por cargo"""
        resultados = [p for p in self.dados 
                     if termo.upper() in p.get('cargo', '').upper()
                     and p.get('num_questoes', 0) > 0]
        await self._enviar_resultados(update, resultados, f"💼 Cargo: {termo}")
    
    async def _buscar_ano(self, update: Update, termo: str):
        """Busca por ano"""
        resultados = [p for p in self.dados 
                     if termo in p.get('ano', '')
                     and p.get('num_questoes', 0) > 0]
        await self._enviar_resultados(update, resultados, f"📅 Ano: {termo}")
    
    async def _enviar_resultados(self, update: Update, resultados: list, titulo: str):
        """Envia resultados da busca"""
        if not resultados:
            # Extrai o termo de busca do título
            termo = titulo.split(':')[1].strip() if ':' in titulo else titulo
            
            # Verifica se há provas sem questões para este termo
            tipo = titulo.split(':')[0].strip()  # Ex: "🏛️ Banca"
            
            if "Banca" in tipo:
                provas_sem_q = [p for p in self.dados if termo.upper() in p.get('banca', '').upper()]
            elif "Órgão" in tipo:
                provas_sem_q = [p for p in self.dados if termo.upper() in p.get('orgao', '').upper()]
            elif "Cargo" in tipo:
                provas_sem_q = [p for p in self.dados if termo.upper() in p.get('cargo', '').upper()]
            elif "Ano" in tipo:
                provas_sem_q = [p for p in self.dados if termo in p.get('ano', '')]
            else:
                provas_sem_q = []
            
            if provas_sem_q:
                msg = f"⚠️ Encontrei {len(provas_sem_q)} prova(s) para '{termo}', mas sem questões cadastradas no site.\n\n"
                msg += "Provas disponíveis:\n"
                for p in provas_sem_q[:5]:
                    msg += f"• {p.get('titulo', 'N/A')[:40]}\n"
                if len(provas_sem_q) > 5:
                    msg += f"\n... e mais {len(provas_sem_q) - 5}"
            else:
                msg = f"❌ Nenhuma prova encontrada para: {termo}"
            
            await update.message.reply_text(msg)
            return
        
        msg = f"🎯 **{titulo}**\n📊 **{len(resultados)} provas com questões encontradas**\n\n"
        
        for i, prova in enumerate(resultados[:15], 1):
            titulo_prova = prova.get('titulo', 'N/A')[:50]
            num_q = prova.get('num_questoes', 0)
            banca = prova.get('banca', 'N/A')
            orgao = prova.get('orgao', 'N/A')
            ano = prova.get('ano', 'N/A')
            
            msg += f"**{i}. {titulo_prova}**\n"
            msg += f"   🏛️ {banca} | 📅 {ano}\n"
            msg += f"   🏢 {orgao}\n"
            msg += f"   ❓ **{num_q} questões**\n"
            
            if prova.get('link_prova_pdf'):
                msg += f"   [📄 Ver Prova]({prova.get('link_prova_pdf')})"
            if prova.get('link_gabarito_pdf'):
                msg += f" | [✅ Ver Gabarito]({prova.get('link_gabarito_pdf')})"
            
            msg += "\n\n"
        
        if len(resultados) > 15:
            msg += f"_...e mais **{len(resultados) - 15}** provas_"
        
        await update.message.reply_text(msg, parse_mode='Markdown', disable_web_page_preview=True)
    
    async def _enviar_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Envia estatísticas"""
        if self.df is None or len(self.df) == 0:
            await update.message.reply_text("⚠ Sem dados")
            return
        
        # Filtrar apenas provas com questões
        df_com_questoes = self.df[self.df['num_questoes'] > 0]
        
        total = len(df_com_questoes)
        total_q = df_com_questoes['num_questoes'].sum()
        media = df_com_questoes['num_questoes'].mean()
        
        msg = f"""📊 **ESTATÍSTICAS (Apenas com Questões)**

📋 Total de provas: **{total}**
❓ Total de questões: **{total_q}**
📈 Média: **{media:.1f}** questões/prova

🏛️ **Top 5 Bancas:**
"""
        for banca, count in df_com_questoes['banca'].value_counts().head(5).items():
            msg += f"  • {banca}: {count}\n"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def _enviar_bancas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Envia lista de bancas"""
        df_com_questoes = self.df[self.df['num_questoes'] > 0]
        
        msg = "🏛️ **BANCAS (com Questões)**\n\n"
        for i, (banca, count) in enumerate(df_com_questoes['banca'].value_counts().items(), 1):
            msg += f"{i}. {banca}: **{count}** provas\n"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def cmd_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /estatisticas"""
        await self._enviar_stats(update, context)
    
    async def cmd_bancas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /bancas"""
        await self._enviar_bancas(update, context)
    
    async def cmd_orgaos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /orgaos"""
        df_com_questoes = self.df[self.df['num_questoes'] > 0]
        
        msg = "🏢 **ÓRGÃOS (com Questões)**\n\n"
        for i, (orgao, count) in enumerate(df_com_questoes['orgao'].value_counts().head(20).items(), 1):
            msg += f"{i}. {orgao}: **{count}** provas\n"
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def cmd_cargos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /cargos"""
        df_com_questoes = self.df[self.df['num_questoes'] > 0]
        
        msg = "💼 **CARGOS (com Questões)**\n\n"
        for i, (cargo, count) in enumerate(df_com_questoes['cargo'].value_counts().head(20).items(), 1):
            msg += f"{i}. {cargo}: **{count}** provas\n"
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def cmd_anos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /anos"""
        df_com_questoes = self.df[self.df['num_questoes'] > 0]
        
        msg = "📅 **ANOS (com Questões)**\n\n"
        for ano, count in df_com_questoes['ano'].value_counts().sort_index(ascending=False).items():
            if ano:
                msg += f"• {ano}: **{count}** provas\n"
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    def rodar(self):
        """Inicia o bot"""
        app = self.criar_app()
        print("🤖 Bot iniciado! Pressione Ctrl+C para parar.")
        app.run_polling()


# Main
if __name__ == "__main__":
    TOKEN = "8395435303:AAHjp-Zp6Oid3uR4iscq29fFr_N9Tvg09eM"
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║  BOT TELEGRAM - CONCURSOS (VERSÃO ESTÁVEL)               ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    bot = BotConcursos(TOKEN)
    bot.rodar()
