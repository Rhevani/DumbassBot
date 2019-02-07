import discord
import asyncio
import configparser

client = discord.Client()
strikes_config = configparser.ConfigParser()
config = configparser.ConfigParser()

@client.event
async def on_ready():
    print('Logged in as' + client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith('!checkpoints'):
        strike_check = message.content.rsplit(' ', 1)[1]
        strike_check_user = discord.utils.find(lambda m: m.name == strike_check,message.server.members)
        string_strike_check_user = str(strike_check_user)
        strikes_config.read('strikes.ini')
        if string_strike_check_user not in strikes_config:
            strikes_config.add_section(string_strike_check_user)
            strikes_config.set(string_strike_check_user,'strikes','0')
        strikes = strikes_config.get(string_strike_check_user,'strikes')
        with open('strikes.ini','w') as configfile:
            strikes_config.write(configfile)
        await client.send_message(message.channel,strike_check_user.mention + ' has ' + str(strikes) + ' points.')
    if message.content.startswith('!givepoint'):
        strike = message.content.rsplit(' ', 1)[1]
        strike_user = discord.utils.find(lambda m: m.name == strike,message.server.members)
        strikes_config.read('strikes.ini')
        string_strike_user = str(strike_user)
        if string_strike_user not in strikes_config:
            strikes_config.add_section(string_strike_user)
            strikes_config.set(string_strike_user,'strikes', '0')
        strikes = strikes_config.get(string_strike_user,'strikes')
        strikes = int(strikes)+1
        strikes_config.set(string_strike_user,'strikes',str(strikes))
        with open('strikes.ini','w') as configfile:
            strikes_config.write(configfile)
        await client.send_message(message.channel, 'I cannot believe you did that, here is a point for you dumbass. ' + strike_user.mention + ' You now have ' + str(strikes) + ' points, good job.')
    if message.content.startswith('!removepoint'):
        r_strike = message.content.rsplit(' ', 1)[1]
        r_strike_user = discord.utils.find(lambda m: m.name == r_strike,message.server.members)
        strikes_config.read('strikes.ini')
        string_r_strike_user = str(r_strike_user)
        if string_r_strike_user not in strikes_config:
            strikes_config.add_section(string_r_strike_user)
            strikes_config.set(string_r_strike_user,'strikes', '0')
        r_strikes = strikes_config.get(string_r_strike_user,'strikes')
        r_strikes = int(r_strikes)-1
        strikes_config.set(string_r_strike_user,'strikes',str(r_strikes))
        with open('strikes.ini','w') as configfile:
            strikes_config.write(configfile)
        await client.send_message(message.channel, ' Yeet ' + r_strike_user.mention + ' You now have '  + str(r_strikes) + ' points.')

client.run('NTQyODQ2ODc1NDE4NzU1MDgy.Dzz-FA.FzkDJMz1xB7M12xMZn2sYczR71c')
