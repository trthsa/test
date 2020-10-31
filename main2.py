import time

from telethon import TelegramClient, events

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = 1459740
api_hash = '9ec877538b0bb31acd53e31b8c1de9ba'

# fill in your own details here
phone = '+84355692421'
session_file = '@dogepios'  # use your username if unsure
password = 'Hoilamgi'  # if you have two-step verification enabled

# content of the automatic reply
message = "Sorry, I maybe **Offline** for now! Will support ASAP!\nThanks for choosing us!"

if __name__ == '__main__':      
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            print(time.asctime(), '-', event.message)  # optionally log time and message
            time.sleep(1)
            await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')