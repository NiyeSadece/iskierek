import asyncio
import discord
import json
import locale
import math
import os
import requests
from datetime import datetime, timedelta
from discord import app_commands
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.errors import MemberNotFound
from dotenv import load_dotenv

project_folder = os.path.expanduser('/home/NiyeSadece/iskierek/iskierek/iskierek')
load_dotenv(os.path.join(project_folder, '.env'))
DOMAIN = os.getenv('DOMAIN')
GUILD = int(os.getenv('GUILD'))
LVL_CHANNEL = int(os.getenv('LVL_CHANNEL'))
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
FORECAST_CHANNEL = int(os.getenv('FORECAST_CHANNEL'))
FORECAST_URL = os.getenv('FORECAST_URL')
NOT_EXP_CHANNELS = [1259656541980721334]
""" [1259526915341946880, 1259527266845851750, 1259527296658837534,
    1259590688262328382, 1259590747091636265, 1259591587202076673,
    1259516954394234961, 1259527395992535120, 1259527422416650331,
    1259527444067782787, 1259527460974755910, 1259527479631286363,
    1259527501122899969, 1259527528197132389, 1259527556131061833,
    1259527583037657159, 1259527603954651259, 1259527620631068832,
    1259527647646580787, 1259516954394234962, 1259527842346045562,
    1259527863095394304, 1259527886818377809, 1259527909421482236,
    1259527925284212807, 1259527941457711217, 1259527964715122760,
    1259527981936939019, 1259528007576453261, 1259528026585174098,
    1259528099570389083, 1259528120042786926, 1259528141723013271,
    1259528163487125515, 1259528180616794193, 1259583597514588261,
    1259528198631194775, 1259528266558079137, 1259528301538574356,
    1259528283691810816, 1259528321167786104, 1259529770501279766,
    1259529746824564779, 1259529798531944632, 1259529819700596749,
    1259529861127606323, 1259529969118220402, 1259529996674793524,
    1259529913099223113, 1259529940462731294, 1259530033144266793,
    1259530057416704070, 1259530074584256513, 1259530091818651720,
    1259530115457749093, 1259530139948158987, 1259530163721601047,
    1259530180326719599, 1259530201940099133, 1259530226942345338,
    1259530263533195286, 1259530290490114069, 1259530310836551691,
    1261377686891139184, ]"""

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=discord.Object(id=GUILD))
        print(f"Synced slash command for {self.user}")

intents = discord.Intents.all()
client = Bot(command_prefix="==", intents=intents, help_command=None)

def update_exp(name, dcid, exp):
    url = f"{DOMAIN}api/exp/update/"
    new_exp = {'name': name, 'discord_id': dcid, 'exp': exp}
    requests.post(url, data=new_exp)

def sub_exp(name, dcid, exp):
    url = f"{DOMAIN}api/exp/sub/"
    new_exp = {'name': name, 'discord_id': dcid, 'exp': exp}
    requests.post(url, data=new_exp)

def update_lvl(dcid):
    url = f"{DOMAIN}api/lvl/update/"
    new_lvl = {'discord_id': dcid}
    requests.post(url, data=new_lvl)

def get_user(dsid):
    response = requests.get(f"{DOMAIN}api/{dsid}/")
    return response.json()

def get_student(student):
    response = requests.get(f"{DOMAIN}api/s/{student}/")
    return response.json()

def get_prof(prof):
    response = requests.get(f"{DOMAIN}api/p/{prof}/")
    return response.json()

def get_ranking():
    response = requests.get(f"{DOMAIN}api/ranking/")
    return response.json()

def set_user_active(dcid):
    url = f"{DOMAIN}api/user/active/"
    now_active = {'discord_id': dcid}
    requests.post(url, data=now_active)

def set_user_inactive(dcid):
    url = f"{DOMAIN}api/user/inactive/"
    now_inactive = {'discord_id': dcid}
    requests.post(url, data=now_inactive)

def exp_for_level(level):
    """ Calculating exp needed for one level """
    A = 73.52
    B = 1.088
    exp = A * (B ** level)
    return math.ceil(exp / 10) * 10

def lvl_up(author_id):
    """ Leveling up system """
    user = get_user(author_id)
    cur_xp = user["exp"]
    cur_lvl = user["lvl"]

    req_exp = 0
    for lvl in range (1, cur_lvl + 1):
        req_exp += exp_for_level(lvl)

    if cur_xp >= req_exp:
        update_lvl(author_id)
        return True
    else:
        return False

def calculate_daily_averages(data):
    daily_averages = {}
    daily_times = data['daily']['time']
    hourly_times = data['hourly']['time']

    for day in daily_times:
        start_time = day + "T00:00"
        end_time = day + "T23:00"
        start_index = hourly_times.index(start_time)
        end_index = hourly_times.index(end_time) + 1

        humidity = data['hourly']['relative_humidity_2m'][start_index:end_index]
        pressure = data['hourly']['surface_pressure'][start_index:end_index]
        visibility = data['hourly']['visibility'][start_index:end_index]

        daily_averages[day] = {
            'avg_humidity': sum(humidity) / len(humidity),
            'avg_pressure': sum(pressure) / len(pressure),
            'avg_visibility': sum(visibility) / len(visibility)
        }

    return daily_averages

def format_weather_forecast(data, daily_averages):
    locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
    forecasts = []
    for i, day in enumerate(data['daily']['time']):
        date_obj = datetime.strptime(day, "%Y-%m-%d")
        day_of_week = date_obj.strftime("%A")

        avg_humidity = daily_averages[day]['avg_humidity']
        avg_pressure = daily_averages[day]['avg_pressure']
        avg_visibility = daily_averages[day]['avg_visibility']

        temp_min = data['daily']['temperature_2m_min'][i]
        temp_max = data['daily']['temperature_2m_max'][i]
        sunrise = datetime.strptime(data['daily']['sunrise'][i], "%Y-%m-%dT%H:%M").strftime("%H:%M")
        sunset = datetime.strptime(data['daily']['sunset'][i], "%Y-%m-%dT%H:%M").strftime("%H:%M")
        uv_index = data['daily']['uv_index_max'][i]
        precip_prob = data['daily']['precipitation_probability_max'][i]

        weather_forecast = (
            f"{day_of_week}, {date_obj.day}. {date_obj.strftime('%B')}\n"
            f"Wilgotność: {avg_humidity:.2f}%\n"
            f"Ciśnienie: {avg_pressure:.2f} hPa\n"
            f"Widoczność: {avg_visibility / 1000:.2f} km\n"
            f"Temperatura: {temp_min}°C - {temp_max}°C\n"
            f"Wschód słońca: {sunrise}, zachód słońca: {sunset}\n"
            f"Indeks UV: {uv_index}\n"
            f"Prawdopodobieństwo opadów: {precip_prob}%"
        )

        forecasts.append(weather_forecast)
    return forecasts

async def get_weather_forecast(channel):
    url = FORECAST_URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        daily_averages = calculate_daily_averages(data)
        forecasts = format_weather_forecast(data, daily_averages)
        for forecast in forecasts:
            await channel.send(forecast)
            await channel.send("-" * 40)
    else:
        await channel.send("Unable to fetch weather data.")

def time_until_target(hour: int, minute: int):
    """ Calculate the time until the next target day and time """
    now = datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target < now:
        target += timedelta(days=7)  # Move to the next week
    return (target - now).total_seconds()

@tasks.loop(seconds=60)
async def weekly_message():
    print("Weekly message task is running...")
    target_day = 0
    target_hour = 8
    target_minute = 1

    now = datetime.now()
    if now.weekday() == target_day and now.hour == target_hour and now.minute == target_minute:
        channel = client.get_channel(FORECAST_CHANNEL)
        if channel:
            print("Sending weather forecast...")
            await get_weather_forecast(channel)
            await asyncio.sleep(7 * 24 * 3600)
        else:
            print("Channel not found.")


@client.hybrid_command(
    name="id",
    with_app_command=True,
    description="Sprawdź wizytówkę postaci",
    pass_context=True,
    help="Sprawdź wizytówkę postaci",
    aliases=["Id", "ID", "iD"])
@app_commands.guilds(discord.Object(id=GUILD))
async def id(ctx: commands.Context, name: str):
    await ctx.defer()
    try:
        name = name.title()
        student = get_student(name)
        prof = get_prof(name)
        if student and student.get('name'):
            person = student
        elif prof and prof.get('name'):
            person = prof
        else:
            await ctx.send("Postać nie została znaleziona.")
            return
        embed = discord.Embed(
                title=f"{person['name']} {person['last_name']}",
                description="Wizytówka postaci",
                colour=0xF78A8C,
                timestamp=datetime.now()
            )
        embed.add_field(name="Urodziny", value=person['dob'])
        embed.add_field(name="Wiek", value=person['age'])
        embed.add_field(name="Iskra", value=person['spark_display']['name_display'])
        embed.add_field(name="Żywioł", value=person['element_display'])
        embed.add_field(name="Zamieszkanie", value=person['living_display'])

        if person == student:
            if student['major2_display']:
                embed.add_field(name="Kierunki", value=f"{student['major_display']}, {student['year_display']},\nWydział {student['faculty_display']}\n{student['major2_display']}, {student['year2_display']},\nWydział {student['faculty2_display']}")
            else:
                embed.add_field(name="Kierunek", value=f"{student['major_display']}, {student['year_display']},\nWydział {student['faculty_display']}")

            sport = student['sport_display']
            if sport:
                sport_value = sport['name_display']
                if sport['special_display']:
                    sport_value += f", {sport['special_display']}"
            else:
                sport_value = "brak"
            embed.add_field(name="Sport", value=sport_value)

            extracurricular = student['extracurricular_display']
            if extracurricular:
                extra_value = extracurricular['name_display']
                if extracurricular['special_display']:
                    extra_value += f", {extracurricular['special_display']}"
            else:
                extra_value = "brak"
            embed.add_field(name="Zajęcia dodatkowe", value=extra_value)

            club = student['club_display']
            if club:
                club_value = club['name_display']
                if club['special_display']:
                    club_value += f", {club['special_display']}"
            else:
                club_value = "brak"
            embed.add_field(name="Klub", value=club_value)

        if person == prof:
            if prof['major2_display']:
                embed.add_field(name="Naucza", value=f"{prof['major_display']}, od {prof['how_long']} ({prof['teaching_duration_1']})\nWydział {prof['faculty_display']}\n{prof['major2_display']}, od {prof['how_long2']} ({prof['teaching_duration_2']})\nWydział {prof['faculty2_display']}")
            else:
                embed.add_field(name="Naucza", value=f"{prof['major_display']}, od {prof['how_long']} ({prof['teaching_duration_1']})\nWydział {prof['faculty_display']}")

            sport = prof['sport_display']
            extracurricular = prof['extracurricular_display']
            club = prof['club_display']
            dorm = prof['dorm_display']
            if sport:
                sport_value = f"{sport['name_display']}, {sport['special_display']}"
                embed.add_field(name="Dodatkowe", value=sport_value)
            elif extracurricular:
                extra_value = f"{extracurricular['name_display']}, {extracurricular['special_display']}"
                embed.add_field(name="Dodatkowe", value=extra_value)
            elif club:
                club_value = f"{club['name_display']}, {club['special_display']}"
                embed.add_field(name="Dodatkowe", value=club_value)
            elif dorm:
                dorm_value = f"{prof['dorm_display']}, {prof['_dorm_special_display']}"
                embed.add_field(name="Dodatkowe", value=dorm_value)
            else:
                embed.add_field(name="Dodatkowe", value="brak")

        if ctx.guild.icon:
                icon_url = str(ctx.guild.icon.url)
                embed.set_author(name="Brightway | Avaritis University", icon_url=icon_url)

        embed.set_thumbnail(url=f"{person['photo']}")

        await ctx.send(embed=embed)

    except commands.MissingRequiredArgument:
        await ctx.send("Musisz podać imię postaci.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")

# showing level
@client.hybrid_command(
    name="lvl",
    with_app_command=True,
    description="Sprawdź poziom kreatywności",
    pass_context=True,
    help="Sprawdź poziom kreatywności",
    aliases=["Lvl", "LVL", "lVL", "lvL", "LvL", "lVl", "LVl", "lV"])
@app_commands.guilds(discord.Object(id=GUILD))
async def lvl(ctx: commands.Context, member: discord.Member = None):
    await ctx.defer()
    try:
        member = ctx.author if not member else member
        member_id = str(member.id)
        user = get_user(member_id)
        if ctx.channel.id != LVL_CHANNEL:
            await ctx.send("Użyj odpowiedniego kanału.")
        else:
            # Create the embed
            embed = discord.Embed(
                title=f"{member.display_name}",
                colour=0xF78A8C,
                timestamp=datetime.now()
            )
            embed.add_field(name="Poziom kreatywności:", value=user['lvl'])
            embed.add_field(name="Exp:", value=user['exp'])

            # Check if guild has an icon and set it if valid
            if ctx.guild.icon:
                icon_url = str(ctx.guild.icon.url)
                embed.set_author(name="Brightway | Avaritis University", icon_url=icon_url)

            if member.avatar:
                embed.set_thumbnail(url=str(member.avatar))

            await ctx.send(embed=embed)
    except KeyError:
        await ctx.send("Nie masz zdobytych żadnych punktów kreatywności. Spróbuj ponownie po dodaniu pierwszego odpisu.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")

# showing ranking
@client.hybrid_command(
    name="rank",
    with_app_command=True,
    description="Sprawdź ranking kreatywności",
    pass_context=True,
    help="Sprawdź ranking kreatywności",
    aliases=["Rank", "RANK", "rANK"])
@app_commands.guilds(discord.Object(id=GUILD))
async def rank(ctx: commands.Context):
    await ctx.defer()
    if ctx.channel.id != LVL_CHANNEL:
        await ctx.send("Użyj odpowiedniego kanału.")
    else:
        rank = 1
        button = discord.ui.Button(label="Sprawdź cały ranking!", style=discord.ButtonStyle.url, url="https://niyesadece.eu.pythonanywhere.com/ranking/", emoji="🏆")
        view = discord.ui.View()
        view.add_item(button)
        embed = discord.Embed(
            title='Ranking kreatywności *Brightway | Avaritis University*',
            description="",
            colour=0xF78A8C
        )
        ranking = get_ranking()
        for item in ranking:
            try:
                embed.add_field(name=f"{rank}.", value=f"<@{item['discord_id']}>")
                rank += 1
            except MemberNotFound:
                continue
        await ctx.send(embed=embed, view=view)

# manually adding exp
@client.command(pass_context=True, help="Komenda dla administracji, łapki precz", aliases=["add", "add_xp"])
@has_permissions(mention_everyone=True)
@app_commands.guilds(discord.Object(id=GUILD))
async def addxp(ctx: commands.Context, xp: int, member: discord.Member = None):
    if ctx.channel.id != LOG_CHANNEL:
        await ctx.send("Użyj odpowiedniego kanału. Poza tym łapki precz.")
    else:
        member = ctx.author if not member else member
        update_exp(member.display_name, member.id, xp)
        await ctx.send(f"Użytkownik {member} dostał {xp} punktów kreatywności!")

    if lvl_up(member.id):
        user = get_user(member.id)
        channel_lvl = client.get_channel(LVL_CHANNEL)
        await channel_lvl.send(
            f"Witaj, Iskierko {member.mention}! Udało ci się wypełnić {user['lvl']}. słoiczek gwiazdeczek z expem. Oby tak dalej!")

# manually subtracting exp
@client.command(pass_context=True, help="Komenda dla administracji, łapki precz", aliases=["sub", "sub_xp"])
@has_permissions(mention_everyone=True)
@app_commands.guilds(discord.Object(id=GUILD))
async def subxp(ctx: commands.Context, xp: int, member: discord.Member = None):
    if ctx.channel.id != LOG_CHANNEL:
        await ctx.send("Użyj odpowiedniego kanału. Poza tym łapki precz.")
    else:
        member = ctx.author if not member else member
        sub_exp(member.display_name, member.id, xp)
        await ctx.send(f"Użytkownik {member} utracił {xp} punktów kreatywności!")

# setting user active, so they do show up in the ranking
@client.command(pass_context=True, help="Komenda dla administracji, łapki precz")
@has_permissions(mention_everyone=True)
@app_commands.guilds(discord.Object(id=GUILD))
async def active(ctx: commands.Context, member: discord.Member = None):
    if ctx.channel.id != LOG_CHANNEL:
        await ctx.send("Użyj odpowiedniego kanału. Poza tym łapki precz.")
    else:
        member = ctx.author if not member else member
        set_user_active(member.id)
        await ctx.send(f"Użytkownik {member} został ustawiony jako aktywny i będzie pokazywać się w rankingu!")

# setting user inactive, so they don't show up in the ranking
@client.command(pass_context=True, help="Komenda dla administracji, łapki precz")
@has_permissions(mention_everyone=True)
@app_commands.guilds(discord.Object(id=GUILD))
async def inactive(ctx: commands.Context, member: discord.Member = None):
    if ctx.channel.id != LOG_CHANNEL:
        await ctx.send("Użyj odpowiedniego kanału. Poza tym łapki precz.")
    else:
        member = ctx.author if not member else member
        set_user_inactive(member.id)
        await ctx.send(f"Użytkownik {member} został ustawiony jako nieaktywny i nie będzie pokazywać się w rankingu!")

@addxp.error
@subxp.error
@active.error
@inactive.error
async def permission_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Nie masz uprawnień do używania tej komendy.")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    channel_log = client.get_channel(LOG_CHANNEL)
    await channel_log.send("Iskierek jest online!")
    weekly_message.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.author.bot:
        if message.channel.id not in NOT_EXP_CHANNELS:
            # adding exp system
            channel_log = client.get_channel(LOG_CHANNEL)
            msg = len(message.content)
            if msg > 99:
                msg_exp = msg // 100
                update_exp(message.author.display_name, message.author.id, msg_exp)
                set_user_active(message.author.id)
                await channel_log.send(
                    f"Dodano {msg_exp} exp {message.author.display_name} za odpis na <#{message.channel.id}>")

                if lvl_up(message.author.id):
                    user = get_user(message.author.id)
                    channel_lvl = client.get_channel(LVL_CHANNEL)
                    await channel_lvl.send(
                        f"Witaj, Iskierko {message.author.mention}! Udało ci się wypełnić {user['lvl']}. słoiczek gwiazdeczek z expem. Oby tak dalej!")
        await client.process_commands(message)


@client.command(name='help', help='Pokazuje tę wiadomość')
async def help_command(ctx):
    embed = discord.Embed(
        title="Help",
        description="Lista dostępnych komend:",
        color=0xF78A8C
    )

    for command in client.commands:
        embed.add_field(name=f"=={command.name}", value=command.help, inline=False)

    await ctx.send(embed=embed)

TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
