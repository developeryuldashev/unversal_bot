from telegram.ext import Updater, CommandHandler, ConversationHandler
from telegram.ext import MessageHandler, Filters
from methods import start, get_matn1, send_audio, get_matn2, send_tarjima, ortga_qaytish
updater=Updater(token='5055557925:AAEuG0pt3us7JeYe8p5CrM4QO2TMZF-5cu8',use_context=True)
dispatcher=updater.dispatcher
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.regex('^(Text To Audio)$'),get_matn1),
                MessageHandler(Filters.regex('^(Translate)$'),get_matn2)],
            2:[MessageHandler(Filters.text, send_audio)],
            3:[MessageHandler(Filters.text,send_tarjima)],
            'back':[MessageHandler(Filters.text,ortga_qaytish)]
        },
    fallbacks=[MessageHandler(Filters.text, start)]
)

dispatcher.add_handler(conv_handler)


updater.start_polling()
print("ok, ulanish amalga oshirildi")
