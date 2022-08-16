import discord

client = discord.Client()


#@client.event
#async def on_ready():
#    print('We have logged in as {0.user}'.format(client))
#
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('$hello'):
#    	await message.channel.send('Hello!')
#    if message.content.startswith("$search"):
#        channel = client.get_channel(916068691953729609)
#        all_messages = await channel.history().flatten()
#
#        hits = searchMessages(all_messages,['wurtz','hello'])
#        for hit in hits:
#            await message.channel.send(hit.content)
#
#
#def searchMessages(messages,keywords):
#    hits = []
#    for keyword in keywords:
#        for message in messages:
#            if keyword in message.content:
#                hits.append(message)
#            else:
#                pass
#    return hits


def performSearch():
    channel = client.get_channel(916068691953729609)
    all_messages = channel.history().flatten()
    hits = searchMessages(all_messages,['wurtz','hello'])
    for hit in hits:
        message.channel.send(hit.content)


def searchMessages(messages,keywords):
    hits = []
    for keyword in keywords:
        for message in messages:
            if keyword in message.content:
                hits.append(message)
            else:
                pass
    return hits

client.run('OTU2MzY3MzIxNTMyODc0NzUy.YjvMeQ.BMaBpPWde5j85bnrq3lK3pg-k4g')