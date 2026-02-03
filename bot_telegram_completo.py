"""
Bot Telegram Completo para Busca de Provas de Concursos Públicos
Com todos os filtros integrados
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import json
import pandas as pd
from datetime import datetime

class ConcursosBotCompleto:
    """Bot completo do Telegram para concursos"""
    
    def __init__(self, token: str):
        self.token = token
        self.app = Application.builder().token(token).build()
        self.dados_provas = []
        self.df = None
        self._carregar_dados()
        self._registrar_comandos()
    
    def _carregar_dados(self):
        """Carrega dados das provas coletadas"""
        try:
            with open('provas_concursos.json', 'r', encoding='utf-8') as f:
                self.dados_provas = json.load(f)
            self.df = pd.DataFrame(self.dados_provas)
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
        self.app.add_handler(CommandHandler("bancas", self.comando_bancas))
        self.app.add_handler(CommandHandler("orgaos", self.comando_orgaos))
        self.app.add_handler(CommandHandler("cargos", self.comando_cargos))
        self.app.add_handler(CommandHandler("anos", self.comando_anos))
        self.app.add_handler(CommandHandler("provas_recentes", self.comando_recentes))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.processar_mensagem))
        self.app.add_handler(CallbackQueryHandler(self.botao_callback))
    
    async def comando_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start"""
        mensagem = """
🎯 **Bem-vindo ao Bot de Concursos Públicos!**

Este bot ajuda você a encontrar provas de concursos públicos de forma rápida.

📚 **Principais Funcionalidades:**

✅ Busca por Banca (FGV, FCC, Cebraspe, etc)
✅ Busca por Órgão (IBAMA, SEFAZ, TJ, etc)
✅ Busca por Cargo (Analista, Técnico, etc)
✅ Busca por Ano (2024, 2025, etc)
✅ Ver Estatísticas Gerais
✅ Listar Provas Recentes

🎮 **Como Usar:**

👉 **/menu** - Interface com botões (mais fácil!)
📖 **/ajuda** - Ver todos os comandos
🔍 **/buscar FGV** - Buscar provas da FGV

👇 Comece clicando em /menu!
        """
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_ajuda(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /ajuda"""
        mensagem = """
📚 **LISTA COMPLETA DE COMANDOS**

🔍 **BUSCAR PROVAS:**
• /buscar [banca] - Busca por banca (ex: /buscar FGV)
• /orgaos - Lista órgãos (depois busca)
• /cargos - Lista cargos (depois busca)
• /anos - Lista anos (depois busca)

📊 **INFORMAÇÕES:**
• /estatisticas - Estatísticas gerais
• /bancas - Ver todas as bancas
• /provas_recentes - Últimas 10 provas

🎮 **INTERFACE:**
• /menu - Menu com botões (RECOMENDADO)
• /ajuda - Esta mensagem

💡 **EXEMPLOS DE USO:**
/buscar FCC → provas da FCC
/buscar Cebraspe → provas do Cebraspe
/estatisticas → ver dados gerais

🌟 **DICA:** Use /menu para navegação mais fácil!
        """
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /menu - Menu interativo"""
        keyboard = [
            [
                InlineKeyboardButton("🔍 Buscar por Banca", callback_data="buscar_banca"),
                InlineKeyboardButton("🏢 Buscar por Órgão", callback_data="buscar_orgao"),
            ],
            [
                InlineKeyboardButton("💼 Buscar por Cargo", callback_data="buscar_cargo"),
                InlineKeyboardButton("📅 Buscar por Ano", callback_data="buscar_ano"),
            ],
            [
                InlineKeyboardButton("📊 Estatísticas", callback_data="ver_stats"),
                InlineKeyboardButton("🆕 Provas Recentes", callback_data="ver_recentes"),
            ],
            [
                InlineKeyboardButton("🏛️ Ver Bancas", callback_data="listar_bancas"),
                InlineKeyboardButton("🏭 Ver Órgãos", callback_data="listar_orgaos"),
            ]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "🎯 **MENU PRINCIPAL**\n\nEscolha uma opção:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    async def botao_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler para cliques nos botões"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "ver_stats":
            await self.comando_estatisticas(update, context)
        elif query.data == "ver_recentes":
            await self.comando_recentes(update, context)
        elif query.data == "listar_bancas":
            await self.comando_bancas(update, context)
        elif query.data == "listar_orgaos":
            await self.comando_orgaos(update, context)
        elif query.data == "buscar_banca":
            await query.edit_message_text(text="📝 Digite o nome da banca (ex: FGV, FCC, Cebraspe)")
            context.user_data['esperando'] = 'banca'
        elif query.data == "buscar_orgao":
            await query.edit_message_text(text="📝 Digite o nome do órgão (ex: IBAMA, SEFAZ, TJ)")
            context.user_data['esperando'] = 'orgao'
        elif query.data == "buscar_cargo":
            await query.edit_message_text(text="📝 Digite o nome do cargo (ex: Analista, Técnico)")
            context.user_data['esperando'] = 'cargo'
        elif query.data == "buscar_ano":
            await query.edit_message_text(text="📝 Digite o ano (ex: 2024, 2025)")
            context.user_data['esperando'] = 'ano'
    
    async def processar_mensagem(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Processa mensagens de texto do usuário"""
        if 'esperando' not in context.user_data:
            return
        
        tipo = context.user_data.pop('esperando')
        termo = update.message.text.strip()
        
        if tipo == 'banca':
            await self._buscar_e_enviar(update, termo, 'banca')
        elif tipo == 'orgao':
            await self._buscar_e_enviar(update, termo, 'orgao')
        elif tipo == 'cargo':
            await self._buscar_e_enviar(update, termo, 'cargo')
        elif tipo == 'ano':
            await self._buscar_e_enviar(update, termo, 'ano')
    
    async def comando_buscar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /buscar"""
        if not context.args:
            await update.message.reply_text(
                "📝 **Como usar:**\n\n"
                "/buscar [termo]\n\n"
                "Exemplos:\n"
                "• /buscar FGV\n"
                "• /buscar Cebraspe\n"
                "• /buscar FCC",
                parse_mode='Markdown'
            )
            return
        
        termo = ' '.join(context.args)
        await self._buscar_e_enviar(update, termo, 'banca')
    
    async def _buscar_e_enviar(self, update: Update, termo: str, tipo: str):
        """Busca provas e envia resultado"""
        if tipo == 'banca':
            resultados = [p for p in self.dados_provas if termo.upper() in p.get('banca', '').upper()]
            emoji = "🏛️"
            titulo = f"Banca: {termo}"
        elif tipo == 'orgao':
            resultados = [p for p in self.dados_provas if termo.upper() in p.get('orgao', '').upper()]
            emoji = "🏢"
            titulo = f"Órgão: {termo}"
        elif tipo == 'cargo':
            resultados = [p for p in self.dados_provas if termo.upper() in p.get('cargo', '').upper()]
            emoji = "💼"
            titulo = f"Cargo: {termo}"
        elif tipo == 'ano':
            resultados = [p for p in self.dados_provas if termo in p.get('ano', '')]
            emoji = "📅"
            titulo = f"Ano: {termo}"
        
        if not resultados:
            await update.message.reply_text(
                f"❌ Nenhuma prova encontrada para: {termo}\n\n"
                "Tente /menu para ver opções de busca."
            )
            return
        
        mensagem = f"{emoji} **{titulo}**\n\n"
        mensagem += f"📊 Total encontrado: {len(resultados)} provas\n\n"
        
        for i, prova in enumerate(resultados[:15], 1):
            mensagem += f"**{i}. {prova.get('titulo', 'N/A')[:50]}...**\n"
            mensagem += f"   🏢 {prova.get('orgao', 'N/A')[:30]}\n"
            mensagem += f"   ❓ {prova.get('num_questoes', 0)} questões\n"
            if prova.get('link_prova_pdf'):
                mensagem += f"   [📄 PDF]({prova.get('link_prova_pdf', '#')})\n"
            mensagem += "\n"
        
        if len(resultados) > 15:
            mensagem += f"\n_...e mais {len(resultados) - 15} provas_"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown', disable_web_page_preview=True)
    
    async def comando_estatisticas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /estatisticas"""
        if self.df is None or len(self.df) == 0:
            await update.message.reply_text("⚠ Nenhuma prova carregada.")
            return
        
        total = len(self.dados_provas)
        total_questoes = self.df['num_questoes'].sum()
        media_questoes = self.df['num_questoes'].mean()
        
        bancas = self.df['banca'].value_counts().head(10)
        orgaos = self.df['orgao'].value_counts().head(10)
        niveis = self.df['nivel'].value_counts()
        
        mensagem = f"""
📊 **ESTATÍSTICAS GERAIS**

📋 Total de provas: **{total}**
❓ Total de questões: **{total_questoes}**
📈 Média de questões/prova: **{media_questoes:.1f}**

🏛️ **Top 5 Bancas:**
"""
        for banca, count in bancas.head(5).items():
            mensagem += f"  • {banca}: {count} provas\n"
        
        mensagem += "\n🏢 **Top 5 Órgãos:**\n"
        for orgao, count in orgaos.head(5).items():
            mensagem += f"  • {orgao}: {count} provas\n"
        
        if not niveis.empty:
            mensagem += "\n📚 **Níveis de Escolaridade:**\n"
            for nivel, count in niveis.items():
                mensagem += f"  • {nivel or 'N/A'}: {count} provas\n"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_bancas(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /bancas"""
        if self.df is None:
            return
        
        bancas = self.df['banca'].value_counts()
        
        mensagem = "🏛️ **TODAS AS BANCAS DISPONÍVEIS**\n\n"
        for i, (banca, count) in enumerate(bancas.items(), 1):
            mensagem += f"{i}. {banca}: **{count}** provas\n"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_orgaos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /orgaos"""
        if self.df is None:
            return
        
        orgaos = self.df['orgao'].value_counts()
        
        mensagem = "🏢 **TODOS OS ÓRGÃOS DISPONÍVEIS**\n\n"
        for i, (orgao, count) in enumerate(orgaos.items(), 1):
            mensagem += f"{i}. {orgao}: **{count}** provas\n"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_cargos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /cargos"""
        if self.df is None:
            return
        
        cargos = self.df['cargo'].value_counts().head(20)
        
        mensagem = "💼 **TOP CARGOS MAIS COBRADOS**\n\n"
        for i, (cargo, count) in enumerate(cargos.items(), 1):
            mensagem += f"{i}. {cargo}: **{count}** provas\n"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_anos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /anos"""
        if self.df is None:
            return
        
        anos = self.df['ano'].value_counts().sort_index(ascending=False)
        
        mensagem = "📅 **PROVAS POR ANO**\n\n"
        for ano, count in anos.items():
            if ano:
                mensagem += f"• {ano}: **{count}** provas\n"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    async def comando_recentes(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /provas_recentes"""
        if self.df is None:
            return
        
        recentes = self.dados_provas[-10:]
        
        mensagem = "🆕 **ÚLTIMAS 10 PROVAS COLETADAS**\n\n"
        for i, prova in enumerate(recentes, 1):
            mensagem += f"**{i}. {prova.get('titulo', 'N/A')[:50]}...**\n"
            mensagem += f"   🏛️ {prova.get('banca', 'N/A')}\n"
            mensagem += f"   ❓ {prova.get('num_questoes', 0)} questões\n\n"
        
        await update.message.reply_text(mensagem, parse_mode='Markdown')
    
    def iniciar(self):
        """Inicia o bot"""
        print("🤖 Bot completo iniciado! Pressione Ctrl+C para parar.")
        self.app.run_polling()


def main():
    """Função principal"""
    TOKEN = "8395435303:AAHjp-Zp6Oid3uR4iscq29fFr_N9Tvg09eM"
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║  BOT TELEGRAM - CONCURSOS PÚBLICOS (VERSÃO COMPLETA)     ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    bot = ConcursosBotCompleto(TOKEN)
    bot.iniciar()


if __name__ == "__main__":
    main()
