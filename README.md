<p align="center">
    <a href="github.address">
        <img src="https://github.com/HoseanRC/shad-api/blob/master/Shad-Bot.png?raw=true" alt="Shadpy" width="128">
    </a>
    <br>
    <b>Shad API Framework for Python</b>
    <br>
    <a href="https://github.com/HoseanRC/shad-api">
        Homepage
    </a>
    •
    <a href="https://github.com/HoseanRC/shad-api/raw/master/docs">
        Documentation
    </a>
    •
    <a href="https://pypi.org/project/shadapi/#history">
        Releases
    </a>
</p>

## Shad Api

> Elegant, modern and asynchronous Shad API framework in Python for users and bots
### Accounts
``` python
from shadapi import Client

app = Client('my_account_auth')

@app.handler
async def my_bot(bot, message):
    await message.reply('``Hello`` __from__ **Shad Api**!')

```

**Another example:**
``` python
from shadapi import Client

app = Client("my_account_auth")

async def my_bot(bot):
    await bot.sendText('object_guid', '``Hello`` __from__ **Shad Api**!')

app.run(my_bot)
```

### Bots Examples (ONLY FOR SPECIAL MEMBERS) (NOT TESTED)
```python
from shadapi import Bot

app = Bot('token')

async def my_bot(bot):
    me = await bot.getMe()
    print(me)

app.run(my_bot)
```
**OR**
```python
from shadapi import Bot

app = Bot('token')

async def my_bot(bot):
    me = await bot.sendMessage('chat_id', 'text')
    print(me)

app.run(my_bot)
```

**Shad-Api** is a modern, elegant and asynchronous framework. It enables you to easily interact with the main Shad API through a user account (custom client) or a bot
identity (bot API alternative) using Python.


### Key Features

- **Ready**: Install Shad-Api with pip and start building your applications right away.
- **Easy**: Makes the Shad API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by pycryptodome, a high-performance cryptography library written in C.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Shad's API to execute any official client action and more.

### Installing

``` bash
pip3 install shadapi
```

### Thanks to:

## shayanheidari01

he did an awesome job at making a rubika library which helped alot to make this project!
https://github.com/shayanheidari01/rubika
