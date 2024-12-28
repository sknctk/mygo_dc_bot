import asyncio
from config import TOKEN, KEYWORD_TO_IMAGES, LISTEN_CHANNEL_IDS
from keyword_responder import KeywordResponder
from discord_cog import DiscordBot
from status_manager import StatusManager
from discord.ext import commands
import discord

# 初始化 Bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 初始化功能模組
keyword_responder = KeywordResponder(KEYWORD_TO_IMAGES)
status_manager = StatusManager(bot)

@bot.event
async def on_ready():
    """當 Bot 準備就緒後執行的事件"""
    print(f"Logged in as {bot.user}")
    print("Bot 已上線並啟動狀態管理器")
    bot.loop.create_task(status_manager.start_status_loop())  # 啟動狀態切換

async def main():
    """主異步函數，用於啟動 Bot"""
    await bot.add_cog(DiscordBot(bot, keyword_responder, LISTEN_CHANNEL_IDS))
    await bot.start(TOKEN)

# 使用 asyncio.run 啟動
asyncio.run(main())
