import zipfile
import os
from pyrogram import Client, filters

@Client.on_message(filters.command("send_zip"))
async def send_zip(client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply_text("Please reply to a ZIP file.")
    
    # Get the ZIP file from the user's reply
    zip_file = message.reply_to_message.document
    
    # Download the ZIP file to the server
    zip_file_path = await client.download_media(zip_file)
    
    # Create a directory to extract the ZIP contents
    extract_dir = f"./extracted_files/{zip_file.file_id}"
    os.makedirs(extract_dir, exist_ok=True)
    
    # Extract the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    # Send the extracted files to the user
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            file_path = os.path.join(root, file)
            await message.reply_document(file_path)
    
    # Optionally, clean up by deleting the extracted files and the original ZIP file
    os.remove(zip_file_path)
    for root, dirs, files in os.walk(extract_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        os.rmdir(root)
