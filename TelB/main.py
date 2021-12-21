import telebot
from telebot import types

token = '5085779870:AAFmg_PCGR-w78DdFpMll_0WIIR4tkvrvRI'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Погнали дальше", "/help")
    bot.send_message(message.chat.id, 'Доброго время суток! Нажми /help чтобы ознакомиться с командами бота.', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Команды могут быть добавлены со временеи. Пока могу вот это:'
                                      '/help — вызов описания команд'
                                      '/socials — скину ссылки на аккаунты нашего отряда в соц. сетях '
                                      '/about — кратко расскажу, что такое снежный десант'
                                      '/otr — перечислю состав нашего отряда на данный момент')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "погнали дальше":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("О СД", "Наш отряд", "Ссылки")
        bot.send_message(message.chat.id, 'О чём поговорим?', reply_markup=keyboard)

@bot.message_handler(commands=['socials'])
def start_message(message):
    bot.send_message(message.chat.id, 'Наш инстаграм: https://instagram.com/osd_way?utm_medium=copy_link'
                                      'Наша группа вк: https://vk.com/osd_mtuci'
                                      'Наш тикток: https://vm.tiktok.com/ZSeyDFsAs/'
                                      'Мы часто проводим всякие интересности, подпишись, чтобы ничего не пропустить!')

@bot.message_handler(commands=['about'])
def start_message(message):
    bot.send_message(message.chat.id, 'Снежный десант — молодежная добровольческая (волонтерская) акция, которая включает'
                                      ' в себя комплекс мероприятий, направленных на развитие добровольчества в молодежной среде,'
                                      ' профориентацию и содействие трудоустройству молодежи, создание условий'
                                      ' для реализации потенциала молодежи в социально-экономической сфере,'
                                      ' патриотическое воспитание, просветительскую деятельность населения'
                                      ' и формирование ценностей здорового образа жизни.' )

@bot.message_handler(commands=['otr'])
def start_message(message):
    bot.send_message(message.chat.id, 'Состав нашего отряда "Путь":'
                                      'Командир — Ксюша Яковлева'
                                      'Коммисар — Катя Сапожникова'
                                      'Бойцы — Влад Шелковин и Леша Докучаев'
                                      'Кол-во кандидатов на этот момент — 14')