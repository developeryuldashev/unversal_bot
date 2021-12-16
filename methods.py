from keyboard import menu, ortga
from gtts import  gTTS
from googletrans import Translator

def start(update,context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"Salom @{user.username} . Unversal_bot ga hush kelibsiz!")
    context.bot.send_message(chat_id=update.effective_chat.id,text="Marxamat kerakli bo'limni tanlang...",reply_markup=menu)
    return 1

def text_to_audio(matn):
    speach=gTTS(text=matn)
    speach.save('audios/audio.mp3')
    audio=open('audios/audio.mp3', 'rb')
    return audio

def translate(matn):
    translater=Translator()
    natija=translater.translate(matn , src='auto', dest='ru')
    return  natija.text

def get_matn1(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Marxamat, Istalgan Ingliz tilidagi matnni kiriting, men uni o'qib beraman...")
    return 2

def send_audio(update,context):
    matn=update.message.text
    context.bot.send_audio(chat_id=update.effective_chat.id,audio=text_to_audio(matn), caption="Mars IT school",reply_markup=ortga)
    return 'back'



def get_matn2(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Marxamat, Istalgan  tilidagi matnni kiriting, men uni Ingliz tiliga tarjima qilib beraman...")
    return 3

def send_tarjima(update,context):
    matn=update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,text=translate(matn),reply_markup=ortga)
    return 'back'
def ortga_qaytish(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Marxamat kerakli bo'limni tanlang...",
                             reply_markup=menu)
    return 1