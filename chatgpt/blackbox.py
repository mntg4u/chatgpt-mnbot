from HorridAPI import Mango
from pyrogram import filters, Client 

@Client.on_message(filters.command("blackbox"))
async def blackbox(client, message):   
    if len(message.command) < 2:
        await message.reply_text("Give An Input!")
        return
    
    query = " ".join(message.command[1:])
    k = await message.reply_text("🔍")
    mango = Mango()  
    response = mango.chat.completions.create(
        model="blackbox",
        messages=[{"role": "user", "content": query}]
    )

    await k.edit(response.text)
