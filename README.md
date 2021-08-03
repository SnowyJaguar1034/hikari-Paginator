# dinteractions-Paginator
Unofficial discord-interactions multi-page embed handler

## Installation
```
pip install dinteractions-Paginator
```

### Dependencies
- [discord.py](https://pypi.org/project/discord.py/)
- [discord-interactions](https://pypi.org/project/discord-interactions/)

## Example GIF:
<div align="left">
    Paginator with select:<br>
    <img src="https://cdn.discordapp.com/attachments/871853650568417310/871902648243216384/8B3ol6wW0q.gif" height="400">
<div>

## Examples:
These simple examples show how to easily create interactive, multiple page embeds that annyone can interact with.

### Slash command:
```py
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dinteractions_Paginator import Paginator

bot = commands.Bot(command_prefix="/")
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="embeds")
async def embeds(ctx: SlashContext):
    one = discord.Embed(title="1st Embed", description="General Kenobi!", color=discord.Color.red())
    two = discord.Embed(title="2nd Embed", description="General Kenobi!", color=discord.Color.orange())
    three = discord.Embed(title="3rd Embed", description="General Kenobi!", color=discord.Color.gold())
    four = discord.Embed(title="4th Embed", description="General Kenobi!", color=discord.Color.green())
    five = discord.Embed(title="5th Embed", description="General Kenobi!", color=discord.Color.blue())
    pages = [one, two, three, four, five]

    await Paginator(bot=bot, ctx=ctx, pages=pages, content="Hello there")
 
bot.run("token")
```

### Normal command:
```py
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from dinteractions_Paginator import Paginator

bot = commands.Bot(command_prefix="t")
slash = SlashCommand(bot)

@bot.command()
async def embeds(ctx):
    one = discord.Embed(title="1st Embed", description="General Kenobi!", color=discord.Color.red())
    two = discord.Embed(title="2nd Embed", description="General Kenobi!", color=discord.Color.orange())
    three = discord.Embed(title="3rd Embed", description="General Kenobi!", color=discord.Color.gold())
    four = discord.Embed(title="4th Embed", description="General Kenobi!", color=discord.Color.green())
    five = discord.Embed(title="5th Embed", description="General Kenobi!", color=discord.Color.blue())
    pages = [one, two, three, four, five]

    await Paginator(bot=bot, ctx=ctx, pages=pages, content="Hello there")
 
bot.run("token")
```
NOTE: `slash = SlashCommand(bot)` required

## Arguments

### Required:
- `bot` - The bot variable, `commands.Bot()` is required
- `ctx` - The context of a command; `SlashContext`
- `pages` - `List[discord.Embed]`: A list of embeds to be paginated
----------------------------------------
### Optional:
- `content` - `Optional[str]`: the content of the message to send, defaults to `None`

#### Time:
- `timeout` - `Optional[int]`: if you want the paginator to work for a limited number of seconds, you can specify it here, defaults to `None` (meaning no timeout)
- `disableAfterTimeout` - `Optional[bool]`: disable components after `timeout`, default `True`
- `deleteAfterTimeout` - `Optional[bool]`: delete components after `timeout`, default `False`

#### What to use:
- `useSelect` - `Optional[bool]`: if you want the paginator to use a select, default is `True`
- `useIndexButton` - `Optional[bool]`: if you want the paginator to use the index button, default is `False`

#### Labels:
- `firstLabel` - `Optional[str]`: The label of the button used to go to the first page, defaults to `""`
- `prevLabel` - `Optional[str]`: The label of the button used to go to the previous page, defaults to `""`
- `nextLabel` - `Optional[str]`: The label of the button used to go to the next page, defaults to `""`
- `lastLabel` - `Optional[str]`: The label of the button used to go to the last page, defaults to `""`

#### Emojis:
- `firstEmoji` - `Optional[Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, dict]`: emoji of the button used to go to the first page, defaults to `"⏮️"`
- `prevEmoji` - `Optional[Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, dict]`: emoji of the button used to go to the previous page, defaults to `"◀"`
- `nextEmoji` - `Optional[Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, dict]`: emoji of the button used to go to the next page, defaults to `"▶"`
- `lastEmoji` - `Optional[Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, dict]`: emoji of the button used to go to the last page, defaults to `"⏭️"`

#### Styles (the colo[u]r of the buttons):
- `indexStyle` - `Optional[Union[ButtonStyle, int]]`: the type of button (`ButtonStyle` or `int`) for the index button, defaults to `3` (`ButtonStyle.green`)
- `firstStyle` - `Optional[Union[ButtonStyle, int]]`: the type of button (`ButtonStyle` or `int`) for the first button, defaults to `1` (`ButtonStyle.blue`)
- `prevStyle` - `Optional[Union[ButtonStyle, int]]`: the type of button (`ButtonStyle` or `int`) for the previous button, defaults to `1` (`ButtonStyle.blue`)
- `nextStyle` - `Optional[Union[ButtonStyle, int]]`: the type of button (`ButtonStyle` or `int`) for the next button, defaults to `1` (`ButtonStyle.blue`)
- `lastStyle` - `Optional[Union[ButtonStyle, int]]`: the type of button (`ButtonStyle` or `int`) for the last button, defaults to `1` (`ButtonStyle.blue`)

#### Miscellaneous:
- `authorOnly` - `Optional[bool]`: if you want the paginator to work for the author only, default is `False`
---------------------------------

## Credits
- Contributors of [discord-interactions](https://pypi.org/project/discord-py-slash-command/)
    - [GitHub](https://github.com/discord-py-slash-commands/discord-py-interactions)
    - [Discord server](https://discord.gg/KkgMBVuEkx)
