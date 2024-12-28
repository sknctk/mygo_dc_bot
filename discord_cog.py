import discord
from discord.ext import commands
import random  # 確保導入 random 模組

class DiscordBot(commands.Cog):
    """Discord Bot 主邏輯"""

    def init(self, bot, keyword_responder, listen_channel_ids):  # 修正方法名稱為 init
        self.bot = bot
        self.keyword_responder = keyword_responder
        self.listen_channel_ids = listen_channel_ids  # 儲存要監聽的頻道 ID

    @commands.Cog.listener()
    async def on_ready(self):
        """當 Bot 準備就緒後執行的事件"""
        print(f"Logged in as {self.bot.user}")
        print("Connected to the following channels:")
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.id in self.listen_channel_ids:
                    print(f"- {channel.name} (ID: {channel.id}) in {guild.name}")

    @commands.Cog.listener()
    async def on_message(self, message):
        """監聽訊息並回應"""
        # 防止 Bot 回應自己的訊息
        if message.author == self.bot.user:
            return

        # 檢查訊息是否來自監聽的頻道
        if message.channel.id not in self.listen_channel_ids:
            return

        # 在控制台輸出收到的訊息
        print(f"Message received in {message.channel.name} (ID: {message.channel.id}): {message.content}")

        # 使用 KeywordResponder 檢查訊息內容
        image_path = self.keyword_responder.find_image(message.content)
        if image_path:
            # 在控制台輸出 Bot 使用的圖片
            print(f"Bot response: Sending image {image_path}")
            await message.channel.send(file=discord.File(image_path))
        else:
            print("No matching keyword found or cooldown active.")

    @commands.command(name="random")
    async def random_image(self, ctx):
        """
        隨機送出一張圖片
        """
        all_images = []
        for images in self.keyword_responder.keyword_to_images.values():
            all_images.extend(images)

        if all_images:
            random_image = random.choice(all_images)
            await ctx.send(file=discord.File(random_image))
        else:
            await ctx.send("沒有可用的圖片！")