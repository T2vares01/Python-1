import discord
from discord import app_commands
from discord.ext import commands

id_do_servidor = 1191884516265033798

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados
            await tree.sync(guild = discord.Object(id = id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print("Entramos como {}.".format(self.user))

intents = discord.Intents.default()
intents.message_content = True
aclient = discord.Client(intents = intents)

# Comandos do Bot
tree = app_commands.CommandTree(aclient)
bot = commands.Bot(command_prefix='.', description='Um bot simples para interação no Discord.',intents=intents)

# Evento de inicialização
@bot.event
async def on_ready():
    print('Bot conectado como {}'.format('Xandão'))

# Comando simples
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Olá!')

# Testar o Bot
@tree.command(guild = discord.Object(id = id_do_servidor), name = 'teste', description='Testando') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message("Estou funcionando!".format(), ephemeral = True)

# Rodar o bot
aclient.run('token')
bot.run('SEU_TOKEN_AQUI')
