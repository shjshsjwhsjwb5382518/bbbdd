from telegram.ext import *




def upf(u,c):
     a = str(c.bot.get_file(u.message.document))
     u.message.reply_text(a)


u = Updater("5800654169:AAFtvFrWnBel2EU8UDslHneLmtpBaGmZZFI",use_context=True)


u.dispatcher.add_handler(MessageHandler(Filters.document,upf))

u.start_polling()
u.idle()
