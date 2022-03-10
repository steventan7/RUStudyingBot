import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests
import json
import os
import datetime
import time

load_dotenv()

client = commands.Bot(command_prefix="$")

rutgers = ["rutgers", "Rutgers", "RU"]


# function that returns the current weather forecast at Rutgers
def get_weather():
    res = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?zip=08854,"
        "US&units=imperial&appid=3e0a8b117a6d871bda4c50f55a612c73")
    json_data = res.json()
    temp = str(json_data['main']['temp'])
    high = str(json_data['main']['temp_max'])
    low = str(json_data['main']['temp_min'])
    weather = json_data['weather'][0]['description']
    current_weather = temp + "° with " + weather + "\n" + "High: " + high + "° \nLow: " + low + "°"
    return current_weather


# function that returns the current sunset and sunrise data
def get_sun():
    # sunset and sunrise data
    dt = datetime.datetime.today()
    unix_time = int(time.mktime(dt.timetuple()))
    res = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=40.5008&lon=-74.4474&dt={'
                       '0}&units=imperial&appid=f9e2bf84fd28f010aa98855ed3da4289'.format(unix_time))
    json_data = res.json()
    sunrise = json_data['city']['sunrise']
    sunset = json_data['city']['sunset']
    time1 = datetime.datetime.fromtimestamp(sunset)
    # print(time1)
    time2 = datetime.datetime.fromtimestamp(sunrise)
    sunset_time = time1.strftime(':%M:%S %p')
    sunrise_time = time2.strftime(':%M:%S %p')
    sunset_hour = int(time1.strftime('%I'))
    sunrise_hour = int(time2.strftime('%I'))
    location = json_data['city']['name']
    # print(sunrise_time)
    # print("Sunrise: " + str(sunrise_hour) + sunrise_time + "\n" + "Sunset: " + str(sunset_hour) + sunset_time)
    return "Sunrise: " + str(sunrise_hour) + sunrise_time + "\n" + "Sunset: " + str(sunset_hour) + sunset_time


# states that the bot is working
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# reacts whenever a user sends a message
client.lmao = 0
client.bruh = 0
client.kshitij = 0

@client.event
async def on_message(message):
    msg = message.content

    if any(word in msg for word in rutgers):
        emoji = '🎉'
        await message.add_reaction(emoji)

    if 'happy birthday' in str(msg.lower()) or 'hbd' in str(msg.lower()):
        celebration = '🎊'
        await message.add_reaction(celebration)

    if 'lmao' in msg.lower():
        client.lmao += 1
        await message.channel.send(f"𝓦𝓮𝓮𝓴𝓵𝔂 𝖑𝖒𝖆𝖔 count: {client.lmao}")

    if 'bruh' in msg.lower():
        client.bruh += 1
        await message.channel.send(f"𝓦𝓮𝓮𝓴𝓵𝔂 𝖇𝖗𝖚𝖍 count: {client.bruh}")

    if 'sexy' in str(msg.lower()) or 'hot' in str(msg.lower()):
        embed = discord.Embed()

        embed.set_image(
            url='https://media-exp1.licdn.com/dms/image/C4D03AQEvvZ5uTXuiVw/profile-displayphoto-shrink_400_400/0'
                '/1643401945691?e=1650499200&v=beta&t=nMz5FEdjzOhhRY3zZWvAvymjRyh24bzoVrJJ7AUteTI')

        user_id = '744224162259664926'
        await message.channel.send(f"<@{user_id}> is 𝓈𝑒𝓍𝓎")
        await message.channel.send(embed=embed)

    if 'cute' in str(msg.lower()):
        embed = discord.Embed()

        embed.set_image(
            url='https://media-exp1.licdn.com/dms/image/C4E03AQFG-PwSDv3-5g/profile-displayphoto-shrink_200_200/0'
                '/1604472726646?e=1648080000&v=beta&t=rFyWLM9pwedAHfGw5l_SJYlywOFRWh66Wr6T9huHkE4')

        user_id = '272884147218022402'
        cute = '😍'
        await message.add_reaction(cute)
        await message.channel.send(f"<@{user_id}> is 𝖈𝖚𝖙𝖊")
        await message.channel.send(embed=embed)

    if 'steven' in str(msg.lower()):
        user_id = '458458523114799119'
        embed = discord.Embed()

        embed.set_image(
            url='https://media-exp1.licdn.com/dms/image/C4E03AQHt6BMBqB5EAA/profile-displayphoto-shrink_200_200/0'
                '/1635625728239?e=1649894400&v=beta&t=Az25tgmLiPiWwQVwjd-SQ_xb2MB4M6Dugg3M6J3wIkU')
        await message.channel.send(f"<@{user_id}>")
        await message.channel.send(embed=embed)

    if 'david' in str(msg.lower()):
        user_id = '657311042417852418'
        embed = discord.Embed()

        embed.set_image(
            url='https://media-exp1.licdn.com/dms/image/C4E03AQHYy_UPqPtjHg/profile-displayphoto-shrink_800_800/0'
                '/1645638877467?e=1652313600&v=beta&t=6hOnZ5hIwyJAwqYHrboOz66zbkSae2ws-EIkU47SEa8')
        await message.channel.send(embed=embed)
        await message.channel.send(f"<@{user_id}>")

    if 'k' in str(msg.lower()):
        user_id = '328915056425173014'
        client.kshitij += 1
        await message.channel.send(f"<@{user_id}>")
        await message.channel.send(f"Times 𝓚 has been pinned this 𝓌𝑒𝑒𝓀: {client.kshitij}")

    if 'dante' in str(msg.lower()):
        user_id = '446150453449850881'
        await message.channel.send(f"<@{user_id}>")

    if 'ash' in str(msg.lower()) or 'ashwati' in str(msg.lower()):
        user_id = '882675266315517982'
        await message.channel.send(f"<@{user_id}>")

    if 'julia' in str(msg.lower()):
        user_id = '666836877365608458'
        await message.channel.send(f"<@{user_id}>")

    if 'max' in str(msg.lower()):
        user_id = '272884147218022402'
        embed = discord.Embed()

        embed.set_image(
            url='https://media-exp1.licdn.com/dms/image/C4E03AQFG-PwSDv3-5g/profile-displayphoto-shrink_400_400/0'
                '/1604472726646?e=1650499200&v=beta&t=v3L8qtxGgfH6Mhdi8Zl4JENmuFEUnlb136njlrML-Iw')
        await message.channel.send(f"<@{user_id}>")
        await message.channel.send(embed=embed)

    if 'ian' in str(msg.lower()):
        user_id = '422473704308473857'
        await message.channel.send(f"<@{user_id}>")

    if 'bartek' in str(msg.lower()):
        user_id = '194857211623636992'
        await message.channel.send(f"<@{user_id}>")

    if 'ron' in str(msg.lower()):
        user_id = '227883660919963648'
        await message.channel.send(f"<@{user_id}>")

    if 'lauren' in str(msg.lower()):
        user_id = '463028012561072128'
        await message.channel.send(f"<@{user_id}>")

    if 'sexy' in str(msg.lower()):
        sexy = '😩'
        await message.add_reaction(sexy)

    if 'pog' in str(msg.lower()) or 'god' in str(msg.lower()):
        embed = discord.Embed()

        embed.set_image(
            url='https://scontent-lga3-2.xx.fbcdn.net/v/t31.18172-8/13701256_166523753767274_170524675764156001_o.jpg'
                '?_nc_cat=111&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=1tW1mqAVIBsAX9zgvyH&_nc_ht=scontent-lga3-2.xx&oh'
                '=00_AT8jA7wK7sFGqKOeb36boUjXfDEs466YvI8JLs2WJsBtww&oe=6232F3FD')
        await message.channel.send(embed=embed)

    if 'centeno' in str(msg.lower()):
        embed = discord.Embed()

        embed.set_image(
            url='https://www.sashonors.rutgers.edu/images/stories/faculty_mentors/AnaPaulaCenteno_a9412.jpg')
        await message.channel.send(embed=embed)

    if 'guna' in str(msg.lower()):
        embed = discord.Embed()

        embed.set_image(
            url='https://www.cs.cmu.edu/~15110-s13/staff/guna.jpg')
        await message.channel.send(embed=embed)


    await client.process_commands(message)


# sends the RU chant
@client.command()
async def chant(ctx):
    await ctx.send("Hoo-Rah! Hoo-Rah! Rutgers, Rah! Upstream, Red Team!")


# sends the RU fight song
@client.command()
async def fightSong(ctx):
    await ctx.send(
        "Rutgers\n"
        "The Bells Must Ring\n"

        "March, men of Rutgers\n"
        "Down the field today,\n"
        "March to another score,\n"
        "Forward to the fray,\n"
        "Fight! men of Rutgers\n"
        "As in days gone by,\n"
        "Fight! for the Scarlet flag\n"
        "Over the rest must fly.\n"
        "Chorus:\n"
        "Keep Rutgers colors to the fore,\n"
        "For they must win so fight, fight, fight!\n"
        "And we'll advance some more to score,\n"
        "The Rutgers flag flies high tonight, alright, alright.\n"
        "We'll fling the Scarlet banner out,\n"
        "And Rutgers men will fight, fight, fight, fight, fight!\n"
        "The bells of Queens each victr'y shout,\n"
        "The bells of Queens must ring tonight.\n"
        "R! U! RAH! RAH! R! U! RAH! RAH! RAH!\n"
        "HOORAH! HOORAH! RUTGERS! RAH! RAH!\n"
        "FIGHT! TEAM! UP! STREAM!\n"
        "UP! STREAM! RED! TEAM! RAH! RAH! RUTGERS! RAH!\n")


# send the RU weather forecast
@client.command()
async def forecast(ctx):
    embed = discord.Embed(
        title="Rutgers Weather Forecast",
        color=discord.Color.red()
    )

    curr = get_weather()
    sun = get_sun()
    embed.add_field(name="Current forecast", value=curr, inline=False)
    embed.add_field(name="New Brunswick", value=sun, inline=False)

    await ctx.send(embed=embed)


# sends the list of commands
@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title="RU Studying Bot Commands",
        description="List of commands",
        color=discord.Color.blue()
    )

    embed.set_image(
        url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUnbE3U3147mDy9d9TmLeEOx-HF0ZgeCsDYg&usqp=CAU')
    embed.set_thumbnail(url='https://live.staticflickr.com/3798/10892597245_5159d99cdc_b.jpg')
    embed.add_field(name='$chant', value='RU chant', inline=False)
    embed.add_field(name='$fightSong', value='RU fight song', inline=False)
    embed.add_field(name='$forecast', value='RU weather forecast', inline=False)

    await ctx.send(embed=embed)


# fetches the Discord token and launches the bot
client.run(os.getenv("TOKEN"))
