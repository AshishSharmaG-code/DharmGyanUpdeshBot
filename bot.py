from telegram.ext import Updater, CommandHandler
import random
import os  # To access environment variables

# Read the token from environment variable
TOKEN = os.environ.get('BOT_TOKEN')  # Make sure you set BOT_TOKEN in your deployment settings

gyan_list = [
    "🌿 जीवन में सच्चा सुख दूसरों की सेवा में है।",
    "🕉️ सत्य ही परम धर्म है।",
    "🌸 आत्मा अमर है, शरीर नश्वर।",
    "🙏 विनम्रता सबसे बड़ी शक्ति है।",
    "🌞 हर दिन एक नई शुरुआत है।"
]

def start(update, context):
    user = update.effective_user
    msg = f"""🙏 जय श्रीराम, {user.first_name} जी!

आपका स्वागत है *DharmGyanUpdesh* में।
यह Chatbot बनाया गया है *Ashish Sharma* द्वारा, एक महान शिक्षक और आध्यात्मिक मार्गदर्शक।

आप /gyan टाइप करके एक दिव्य उपदेश प्राप्त कर सकते हैं।"""
    update.message.reply_markdown(msg)

def gyan(update, context):
    update.message.reply_text(random.choice(gyan_list))

def main():
    if not TOKEN:
        print("❌ BOT_TOKEN environment variable not found.")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("gyan", gyan))

    print("✅ Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
