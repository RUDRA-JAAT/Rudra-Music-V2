import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from Rudra import app  

photo = [
    "https://telegra.ph/file/5a86a80721f7394ed8d73.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳\n\n"
                f"📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"🔐𝐂ʜᴀᴛ 𝐔.𝐍: @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"💖𝐔ʀ 𝐈d: {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"✍️𝐔ʀ 𝐔.𝐍: @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"🤔 𝐀ᴅᴅᴇᴅ 𝐁ʏ: {message.from_user.mention}\n🌺𝐓ʜᴀɴᴋs 𝐅ᴏʀ 𝐒ᴜᴘᴘᴏʀᴛ💕🌹\n➖➖➖➖➖➖➖➖➖➖➖\n"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"👀sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳\n\n"
                f"📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"🔐𝐂ʜᴀᴛ 𝐔.𝐍: @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"💖𝐔ʀ 𝐈d: {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"✍️𝐔ʀ 𝐔.𝐍: @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉\n➖➖➖➖➖➖➖➖➖➖➖\n"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🌺•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•🌺", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


