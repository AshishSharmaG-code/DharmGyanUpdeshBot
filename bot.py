import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# List of spiritual messages
gyan_list = [
    "🌿 जीवन में सच्चा सुख दूसरों की सेवा में है।",
    "🕉️ सत्य ही परम धर्म है।",
    "🌸 आत्मा अमर है, शरीर नश्वर।",
    "🙏 विनम्रता सबसे बड़ी शक्ति है।",
    "🌞 हर दिन एक नई शुरुआत है।"
]

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = f"""🙏 जय श्रीराम, {user.first_name} जी!

आपका स्वागत है *DharmGyanUpdesh* में।
यह Chatbot बनाया गया है *Ashish Sharma* द्वारा, एक महान शिक्षक और आध्यात्मिक मार्गदर्शक।

आप /gyan टाइप करके एक दिव्य उपदेश प्राप्त कर सकते हैं।"""
    await update.message.reply_markdown(msg)

# Gyan command
async def gyan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(gyan_list))

# Main function
async def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("❌ BOT_TOKEN environment variable not found.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gyan", gyan))

    print("✅ Bot is running...")
    await app.run_polling()

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
