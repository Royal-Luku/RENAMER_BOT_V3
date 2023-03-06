import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["help"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**Institutions For How To use Bot 😃\n\nStep 1 - Send Any File Or Document To Bot For Rename It Easily \n\nStep 2 - Don't Send Any Task After Previous Was Completed Successfully\n\nEnjoy Our Bot... \n\nFor More Query @RoyalDwip 🚩**\n\n ✅ Total Renamed File :-{total_rename}\n✅ Total Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
