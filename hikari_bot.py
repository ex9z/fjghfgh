import hikari
import lightbulb
import random

bot = lightbulb.BotApp(
    token='your token'
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('lolxd')


@bot.command
@lightbulb.command('just a command', 'description')
@lightbulb.implements(lightbulb.SlashCommand)
async def gsfsf(ctx):
    await ctx.respond('222222')


@bot.command
@lightbulb.option('num2', 'to', type=int)
@lightbulb.option('num1', 'from', type=int)
@lightbulb.command('random', 'random "from" "to"')
@lightbulb.implements(lightbulb.SlashCommand)
async def rand(ctx):
    result = random.randint(ctx.options.num1, ctx.options.num2)
    await ctx.respond(result)


@bot.command
@lightbulb.option('text', 'example : apple , banana , awopawaw , ...')
@lightbulb.command('random-words', 'hehe')
@lightbulb.implements(lightbulb.SlashCommand)
async def ball(ctx):
    res = ctx.options.text.split(' , ' and ', ' and ',' and ' ,')
    await ctx.respond(random.choice(res))


@bot.command
@lightbulb.command('ping', ' ')
@lightbulb.implements(lightbulb.SlashCommand)
async def asd(ctx):
    await ctx.respond(f"latency: {bot.heartbeat_latency*1000:.2f}ms")

bot.run()
