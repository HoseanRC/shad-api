<p align="center">
    <a href="https://github.com/HoseanRC/shad-api">
        <img src="https://user-images.githubusercontent.com/68903522/213505965-348da778-36c3-42e0-a31b-7f8711cf18ef.png" alt="Shadpy" width="128">
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

**WebSocket Handler:**
``` python
from shadapi import Client

app = Client('my_account_auth')

@app.handler
async def my_bot(bot, message):
    await message.reply('``Hello`` __from__ **Shad Api**!')
```

**Messages Update Handler:**
``` python
from shadapi import Client

app = Client('my_account_auth')

@app.updateHandler
async def my_bot(bot, message):
    await message.reply('``Hello`` __from__ **Shad Api**!')
```
**OR**
``` python
from shadapi import Client

app = Client('my_account_auth')

update_delay = 5 # in seconds

@app.updateHandler(update_delay)
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

## Notes

### broken message handler

when using this library for fethcing messages from a chat, the library will start a WebSocket channel with the server, and because of the present lag in the server, some of the messages will not be sent by the server and wont be processed by the client (this is not an issue with the library, it's from the server! this problem also do exist in the Android and Web versions of Shad)
we can kindof fix this problem by loading every last message every once in a while to ensure that the client have recived every message, but this would make the bot use more internet (around 277MB per day for maden requests every 2 seconds). the problem with this bypass is that the server would consider that as "request spam" (aka DDOS) and will refuse to response to most of the requests, and this would make the bot pretty much slower! i did implement this functionality in the library and with the addition of "request delay", but until shad devs fix the main issue inside the server or until i find an actuall bypass solution, this are the only ways to handle messages in this library.

| Request method         | advantages                | disadvantage          |
|------------------------|---------------------------|-----------------------|
| WebSocket syncing      | instant trigger           | ignores most messages |
| getChatUpdates request | triggers on every message | slow trigger          |

## Thanks to:

### shayanheidari01

he did an awesome job at making a rubika library which helped alot to make this project!
https://github.com/shayanheidari01/rubika
