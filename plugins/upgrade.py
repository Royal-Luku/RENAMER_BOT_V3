"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
      ✅ **VIP** 
	Daily  Upload  limit unlimited
	Price Rs 100  🇮🇳
	
	
	Pay Using Upi I'd ```adityakar052@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Send ScreenShot ",url = "https://t.me/Royaldwip")], 
        			[InlineKeyboardButton("Channel",url = "https://t.me/FoxPrimeBots"),
        			InlineKeyboardButton("Join",url = "https://t.me/WomBackup")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
      ✅ **VIP** 
	Daily  Upload  limit unlimited 
	Price Rs 100 🇮🇳 
	
	
	Pay Using Upi Id ```adityakar052@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Send ScreenShot ",url = "https://t.me/Royaldwip")], 
        			[InlineKeyboardButton("Channel",url = "https://t.me/FoxPrimeBots"),
        			InlineKeyboardButton("Join",url = "https://t.me/WomBackup")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
