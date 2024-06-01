import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Ensure the bot can fetch members
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def bjoin(ctx, server_id: str):
    embed = discord.Embed(
        title="Discord Members",
        description=f"Adding 10 members to {server_id}",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def massdm(ctx, server_link: str):
    # Creating the embed message
    embed = discord.Embed(
        title="Mass DM",
        description=f"DMing over 11 Members with the message: {server_link}",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

    # Fetching the members and sending DMs
    members = ctx.guild.members
    dmed_count = 0
    for member in members:
        try:
            if not member.bot:  # Do not DM bots
                await member.send(f"Join our server: {server_link}")
                dmed_count += 1
                if dmed_count >= 11:
                    break
        except Exception as e:
            print(f"Failed to DM {member.name}: {e}")

    print(f"Successfully DMed {dmed_count} members.")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTI0NjU5OTQ5NDU5NDk4NjA5NA.GbhYFO.BX3EtHLiiTxAjTElzOjU25byUbYpace5ZNheis')
