import discord
from dotenv import load_dotenv
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import requests
import json
import os
import random
from pprint import pprint
import datetime
import time
import io
import aiohttp

# MongoDB password login
cluster = MongoClient("mongodb+srv://stantheman:kittendatabase@cluster0.pt8q9.mongodb.net/test")
db = cluster["UserData"]
collection = db["UserData"]

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
    sunset_hour = int(time1.strftime('%I')) - 5
    sunrise_hour = int(time2.strftime('%I')) - 5
    location = json_data['city']['name']
    # print(sunrise_time)
    # print("Sunrise: " + str(sunrise_hour) + sunrise_time + "\n" + "Sunset: " + str(sunset_hour) + sunset_time)
    return "Sunrise: " + str(sunrise_hour) + sunrise_time + "\n" + "Sunset: " + str(sunset_hour) + sunset_time

get_sun()
# states that the bot is working
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# reacts whenever a user sends a message
@client.event
async def on_message(message):
    msg = message.content

    if any(word in msg for word in rutgers):
        emoji = '🎉'
        await message.add_reaction(emoji)

    if 'happy birthday' in str(msg.lower()) or 'hbd' in str(msg.lower()):
        celebration = '🎊'
        await message.add_reaction(celebration)

    if 'hot' in str(msg.lower()) or 'sexy' in str(msg.lower()):
        user_id = '328915056425173014'
        await message.channel.send(f"<@{user_id}> is 𝓼𝓮𝔁𝔂")

    if '𝓼𝓮𝔁𝔂' in str(msg.lower()):
        sexy = '😩'
        await message.add_reaction(sexy)

    if 'potassium' in str(msg.lower()) or 'pog' in str(msg.lower()) or 'god' in str(msg.lower()):
        embed = discord.Embed()

        embed.set_image(
            url='https://scontent-lga3-1.xx.fbcdn.net/v/t31.18172-8/13701256_166523753767274_170524675764156001_o.jpg'
                '?_nc_cat=111&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=cKG5sheeOpMAX8fCK29&_nc_ht=scontent-lga3-1.xx&oh'
                '=00_AT9bpekDfzMeYV_qx_o_xwC0BbmCO2ffQr7lxld5L8CaUw&oe=620B66FD')
        await message.channel.send(embed=embed)

    # "lmao" counter
    # myquery1 = {"_id": '272884147218022402'}
    # if collection.count_documents(myquery1) == 0:
    #     if 'lmao' in str(msg.lower()):
    #         post = {"_id": '272884147218022402', "score": 1}
    #         collection.insert_one(post)
    #         await message.channel.send("Max\'s 𝖑𝖒𝖆𝖔 count: 1")
    # else:
    #     if 'lmao' in str(msg.lower()):
    #         query1 = {"_id": '272884147218022402'}
    #         user = collection.find(query1)
    #         for result in user:
    #             lmao_count = result["score"]
    #         lmao_count += 1
    #         collection.update_one({"_id": '272884147218022402'}, {"$set": {"score": lmao_count}})
    #         await message.channel.send('𝓛𝓶𝓪𝓸 count: ' + str(lmao_count))
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
