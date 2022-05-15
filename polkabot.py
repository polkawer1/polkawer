import discord
from discord.utils import get
a = '~'


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await client.change_presence(status = discord.Status.online, activity = discord.Game( 'game'))
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        msg = message.content.lower()








client = MyClient()
client.run('ODQxNTY1MjkwNjQ2NDcwNjY2.GnGLq9.k019uTchDokz57xkb8ighQwxKfxc2wYq75All4')
