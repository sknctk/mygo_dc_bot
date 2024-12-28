import asyncio
import discord

class StatusManager:
    """
    管理 Discord Bot 狀態的類別
    """
    def __init__(self, bot):
        self.bot = bot
        self.activities = [
            discord.Activity(type=discord.ActivityType.listening, name="春日影!"),
            discord.Activity(type=discord.ActivityType.watching, name="MyGO!!!!!")
        ]

    async def start_status_loop(self):
        """
        啟動狀態切換的循環任務
        """
        while True:
            for activity in self.activities:
                await self.bot.change_presence(activity=activity)
                await asyncio.sleep(60)  # 每次切換間隔 60 秒
