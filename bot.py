import discord
import sys

# トークン読み込み
with open("token.txt", "r") as f:
    TOKEN = f.readline()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_message(message):
    if message.author.bot:
        pass
    cmd = message.content.split(" ")
    notexists = False
    # 試験運用中はコメントアウトしてください
    await message.channel.send("(ただいま試験運用中です。期待通りに動かない場合があります。)")
    if cmd[0] == "!admin":
        if len(cmd) == 1:
            await message.channel.send('このコマンドはこのbotを操作するためのコマンドです。使用可能コマンドは"!admin stop"です。')
        elif cmd[1] == "stop":
            await message.channel.send("botプログラムを終了します。")
            await bot.close()
        else:
            notexists = True
    elif cmd[0] == "!ping":
        await message.reply("pong")
    else:
        notexists = True

    if notexists:
        await message.channel.send("存在しないコマンドです。")

bot.run(TOKEN)