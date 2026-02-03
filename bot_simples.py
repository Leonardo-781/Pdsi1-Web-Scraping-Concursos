"""
Bot Telegram SUPER SIMPLES para Concursos
Versão com menu visual claro
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import json
import pandas as pd

class BotSimples:
    """Bot super simples com menu visual"""
    
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
        """Cria a aplicação do bot"""
        app = Application.builder().token(self.token).build()
        
        app.add_handler(CommandHandler("start", self.cmd_start))
        app.add_handler(CommandHandler("menu", self.cmd_menu))
        app.add_handler(CallbackQueryHandler(self.handle_button))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))
        
        return app
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start"""
        msg = """
╔══════════════════════════════════════╗
║   📚 BOT DE PROVAS DE CONCURSOS 📚   ║
╚══════════════════════════════════════╝

Olá! Aqui você encontra:
✅ 291 provas de concursos
✅ 12+ mil questões
✅ Buscas rápidas e fáceis

Use /menu para começar
"""
        await update.message.reply_text(msg)
    
    async def cmd_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Menu principal com botões simples"""
        keyboard = [
            [InlineKeyboardButton("🔍 Buscar por Banca", callback_data="buscar_banca")],
            [InlineKeyboardButton("🗂️ Ver Todas as Bancas", callback_data="listar_bancas")],
            [InlineKeyboardButton("📊 Ver Estatísticas", callback_data="stats")],
            [InlineKeyboardButton("📅 Provas por Ano", callback_data="anos")],
            [InlineKeyboardButton("🏢 Órgãos Públicos", callback_data="orgaos")],
            [InlineKeyboardButton("💼 Cargos", callback_data="cargos")],
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        msg = """
╔══════════════════════════════════════╗
║           📋 MENU PRINCIPAL           ║
╚══════════════════════════════════════╝

O que você quer fazer?
"""
        
        if update.callback_query:
            await update.callback_query.edit_message_text(msg, reply_markup=reply_markup)
        else:
            await update.message.reply_text(msg, reply_markup=reply_markup)
    
    async def handle_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Processa cliques nos botões"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "buscar_banca":
            bancas_top = self.df[self.df['num_questoes'] > 0]['banca'].value_counts().head(10)
            
            keyboard = []
            for banca, count in bancas_top.items():
                keyboard.append([InlineKeyboardButton(f"{banca} ({count})", callback_data=f"banca:{banca}")])
            keyboard.append([InlineKeyboardButton("⬅️ Voltar", callback_data="menu")])
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            msg = """
╔══════════════════════════════════════╗
║       🏛️ TOP 10 BANCAS COM PROVAS      ║
╚══════════════════════════════════════╝

Clique em uma banca para ver as provas:
"""
            await query.edit_message_text(msg, reply_markup=reply_markup)
        
        elif query.data == "listar_bancas":
            df_com_q = self.df[self.df['num_questoes'] > 0]
            msg = "🏛️ **BANCAS DISPONÍVEIS:**\n\n"
            
            for i, (banca, count) in enumerate(df_com_q['banca'].value_counts().items(), 1):
                msg += f"{i}. {banca}: {count} provas\n"
            
            keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="menu")]]
            await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        
        elif query.data == "stats":
            df_com_q = self.df[self.df['num_questoes'] > 0]
            total = len(df_com_q)
            total_q = df_com_q['num_questoes'].sum()
            media = total_q / total if total > 0 else 0
            
            msg = f"""
╔══════════════════════════════════════╗
║         📊 ESTATÍSTICAS GERAIS        ║
╚══════════════════════════════════════╝

📋 Total de Provas: **{total}**
❓ Total de Questões: **{total_q:,}**
📈 Média: **{media:.1f}** questões/prova

🏛️ TOP 5 Bancas:
"""
            for banca, count in df_com_q['banca'].value_counts().head(5).items():
                msg += f"  • {banca}: {count}\n"
            
            keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="menu")]]
            await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        
        elif query.data == "anos":
            df_com_q = self.df[self.df['num_questoes'] > 0]
            anos = sorted(df_com_q['ano'].unique(), reverse=True)
            
            keyboard = []
            for ano in anos:
                count = len(df_com_q[df_com_q['ano'] == ano])
                keyboard.append([InlineKeyboardButton(f"{ano} ({count})", callback_data=f"ano:{ano}")])
            keyboard.append([InlineKeyboardButton("⬅️ Voltar", callback_data="menu")])
            
            msg = "📅 **PROVAS POR ANO:**\n\nEscolha um ano:"
            await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        
        elif query.data == "orgaos":
            df_com_q = self.df[self.df['num_questoes'] > 0]
            msg = "🏢 **ÓRGÃOS PÚBLICOS:**\n\n"
            
            for i, (orgao, count) in enumerate(df_com_q['orgao'].value_counts().head(15).items(), 1):
                msg += f"{i}. {orgao}: {count} provas\n"
            
            keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="menu")]]
            await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        
        elif query.data == "cargos":
            df_com_q = self.df[self.df['num_questoes'] > 0]
            msg = "💼 **CARGOS MAIS COMUNS:**\n\n"
            
            for i, (cargo, count) in enumerate(df_com_q['cargo'].value_counts().head(15).items(), 1):
                msg += f"{i}. {cargo}: {count} provas\n"
            
            keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="menu")]]
            await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        
        elif query.data == "menu":
            await self.cmd_menu(update, context)
        
        elif query.data.startswith("banca:"):
            banca = query.data.replace("banca:", "")
            await self._mostrar_provas_banca(query, banca)
        
        elif query.data.startswith("ano:"):
            ano = query.data.replace("ano:", "")
            await self._mostrar_provas_ano(query, ano)
    
    async def _mostrar_provas_banca(self, query, banca: str):
        """Mostra provas de uma banca"""
        provas = [p for p in self.dados 
                 if p.get('banca') == banca and p.get('num_questoes', 0) > 0]
        
        if not provas:
            await query.edit_message_text("❌ Nenhuma prova encontrada")
            return
        
        msg = f"🏛️ **{banca}** - {len(provas)} provas\n\n"
        
        for i, prova in enumerate(provas[:10], 1):
            titulo = prova.get('titulo', 'N/A')[:35]
            questoes = prova.get('num_questoes', 0)
            ano = prova.get('ano', 'N/A')
            
            pdf_url = prova.get('url_pdf', '')
            if pdf_url:
                msg += f"{i}. [{titulo}...]({pdf_url})\n   ❓ {questoes} questões | 📅 {ano}\n\n"
            else:
                msg += f"{i}. {titulo}...\n   ❓ {questoes} questões | 📅 {ano}\n\n"
        
        if len(provas) > 10:
            msg += f"\n... e mais {len(provas) - 10} provas"
        
        keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="buscar_banca")]]
        await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    
    async def _mostrar_provas_ano(self, query, ano: str):
        """Mostra provas de um ano"""
        provas = [p for p in self.dados 
                 if p.get('ano') == ano and p.get('num_questoes', 0) > 0]
        
        if not provas:
            await query.edit_message_text("❌ Nenhuma prova encontrada")
            return
        
        msg = f"📅 **Provas de {ano}** - {len(provas)} provas\n\n"
        
        for i, prova in enumerate(provas[:10], 1):
            titulo = prova.get('titulo', 'N/A')[:35]
            questoes = prova.get('num_questoes', 0)
            banca = prova.get('banca', 'N/A')
            
            pdf_url = prova.get('url_pdf', '')
            if pdf_url:
                msg += f"{i}. [{titulo}...]({pdf_url})\n   🏛️ {banca} | ❓ {questoes} questões\n\n"
            else:
                msg += f"{i}. {titulo}...\n   🏛️ {banca} | ❓ {questoes} questões\n\n"
        
        if len(provas) > 10:
            msg += f"\n... e mais {len(provas) - 10} provas"
        
        keyboard = [[InlineKeyboardButton("⬅️ Voltar", callback_data="anos")]]
        await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Processa mensagens de texto"""
        await update.message.reply_text("Use /menu para começar 👇\n\nOu digite /start para instruções")


def main():
    # Token do bot
    TOKEN = "8395435303:AAHjp-Zp6Oid3uR4iscq29fFr_N9Tvg09eM"
    
    print("\n╔═══════════════════════════════════════════════════════════╗")
    print("║  BOT TELEGRAM - CONCURSOS (VERSÃO SIMPLES)              ║")
    print("╚═══════════════════════════════════════════════════════════╝\n")
    
    bot = BotSimples(TOKEN)
    app = bot.criar_app()
    
    app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == '__main__':
    main()
