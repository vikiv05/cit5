# -*- coding: utf-8 -*-
import telebot
from telebot.types import Message
import random

COMMENT = random.randint(1, 9999)
QIWI = '+79661672443'
OPER = '@Narkoshop_online'
VISA = '4890494703008474'
API_TOKEN = '904127253:AAGm39nvQ0BT5g7pRzcaH2BdayxDXBTZyPk'
LINK = 'http://kz.dja548onion.site/forum'
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\nПривет, '  + '<b>' + message.chat.first_name+ '</b>' + '.\nВсе продажи работают в автоматическом режиме, следуйте инструкции в боте, для совершения покупок.\n➖➖➖➖➖➖➖➖➖➖➖➖\nВыберите город 👇\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇰🇿<b>Казахстан</b>\n🏘Уральск - /uralsk\n🏘Петропавловск - /petropavlovsk\n🏘Актау - /aktay\n➖➖➖➖➖➖➖➖➖➖➖➖\n <a href="'+str(LINK)+'">ОТЗЫВЫ О НАШЕЙ РАБОТЕ</a> \n Спорные ситуации : @1111', disable_web_page_preview=True, parse_mode="Html")

# Города
@bot.message_handler(commands=['uralsk'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы выбрали город <b>Уральск</b>\n❕ Выберите район\n➖➖➖➖➖➖➖➖➖➖➖➖\n🏘Уральск \n📍<b>Пригород</b> - /city1\n📍<b>Город</b> - /city2\n', parse_mode="Html")

@bot.message_handler(commands=['petropavlovsk'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы выбрали город <b>Петропавловск</b>\n❕ Выберите район\n➖➖➖➖➖➖➖➖➖➖➖➖\n🏘Петропавловск \n📍<b>Пригород</b> - /city1\n📍<b>Город</b> - /city2\n', parse_mode="Html")

@bot.message_handler(commands=['aktay'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы выбрали город <b>Актау</b>\n❕ Выберите район\n➖➖➖➖➖➖➖➖➖➖➖➖\n🏘Актау \n📍<b>Пригород</b> - /city1\n📍<b>Город</b> - /city2\n', parse_mode="Html")

# СТРАНИЦЫ ПОКУПОК
@bot.message_handler(commands=['city1'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы выбрали <b>Пригород</b>.\n❕ Выберите интересующий товар\n➖➖➖➖➖➖➖➖➖➖➖➖\n💎СК 0.5гр-7500тг-/buy125\n💎СК 1гр-12000тг-/buy126\n💎СК 2гр-20000тг-/buy127\n🕺Меф 1гр-14000тг-/buy134\n🕺Меф 2гр-22000тг-/buy135\n☘️Шишки 1гр-7500тг-/buy142\n☘️Шишки 2гр-15000тг-/buy143\n☘️Шишки 4гр-28000гр-/buy144\n📦Гашиш 2гр-14000тг-/buy151\n📦Гашиш 4гр-26000тг-/buy152\n💊Экстази 1шт-12000тг-/buy163\n💊Экстази 5шт-23000тг-/buy164\n💊Экстази 10шт-34000тг-/buy165', parse_mode="Html")

@bot.message_handler(commands=['city2'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы выбрали <b>Город</b>.\n❕ Выберите интересующий товар\n➖➖➖➖➖➖➖➖➖➖➖➖\n💎СК 0.5гр-7500тг-/buy125\n💎СК 1гр-12000тг-/buy126\n💎СК 2гр-20000тг-/buy127\n🕺Меф 0.5гр-9500тг-/buy133\n🕺Меф 1гр-14000тг-/buy134\n🕺Меф 2гр-22000тг-/buy135\n☘️Шишки 1гр-7500тг-/buy142\n☘️Шишки 2гр-15000тг-/buy143\n☘️Шишки 4гр-28000гр-/buy144\n📦Гашиш 1г-6200тг-/buy150\n📦Гашиш 2гр-14000тг-/buy151\n📦Гашиш 4гр-26000тг-/buy152\n💊Экстази 1шт-12000тг-/buy163\n💊Экстази 5шт-23000тг-/buy164\n💊Экстази 10шт-34000тг-/buy165\n💸Кокаин  0.5гр-30000тг-/buy170\n💸Кокаин 1гр-50000тг-/buy171\n💸Кокаин 2гр-90000тг-/buy172\n🎆Марки 2шт-15000тг-/buy180\n🎆Марки 5шт-30000тг-/buy182\n🎆Марки 10шт-50000тг-/buy183\n🏃‍♂️Амфетамин 1г-6500тг-/buy191\n🏃‍♂️Амфетамин 2гр-12500тг-/buy192\n🏃‍♂️Амфетамин 5гр-30000тг-/buy193\n🔲Героин 0.5г-11500тг-/buy200\n🔲Героин 1гр-22500тг-/buy201\n🔲Героин 3гр-60000тг-/buy202\n🍃План 4г-5500тг-/buy211\n🍃План 10гр-10500тг-/buy212', parse_mode="Html")

# VISA CHECK


@bot.message_handler(commands=['buy125'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💎Скорость <b>0.5гр</b>\n❕ Сумма: <b>7500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy126'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💎Скорость <b>1гр</b>\n❕ Сумма: <b>12000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy127'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💎Скорость <b>2гр</b>\n❕ Сумма: <b>20000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy133'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🕺Мефедрон <b>0.5гр</b>\n❕ Сумма: <b>9500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy134'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🕺Мефедрон <b>1гр</b>\n❕ Сумма: <b>14000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy135'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🕺Мефедрон <b>2гр</b>\n❕ Сумма: <b>22000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy142'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n☘️Шишки <b>1гр</b>\n❕ Сумма: <b>7500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy143'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n☘️Шишки <b>2гр</b>\n❕ Сумма: <b>15000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy144'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n☘️Шишки <b>4гр</b>\n❕ Сумма: <b>28000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy150'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n📦Гашиш <b>1гр</b>\n❕ Сумма: <b>6200</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy151'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n📦Гашиш <b>2гр</b>\n❕ Сумма: <b>14000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\nКомментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy152'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n📦Гашиш <b>4гр</b>\n❕ Сумма: <b>26000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy163'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💊Экстази <b>1шт</b>\n❕ Сумма: <b>12000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy164'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💊Экстази <b>5шт</b>\n❕ Сумма: <b>23000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy165'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💊Экстази <b>10шт</b>\n❕ Сумма: <b>34000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy170'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💸Кокаин <b>0.5гр</b>\n❕ Сумма: <b>30000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy171'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💸Кокаин <b>1гр</b>\n❕ Сумма: <b>50000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy172'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💸Кокаин <b>2гр</b>\n❕ Сумма: <b>90000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy180'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🎆Марки <b>2шт</b>\n❕ Сумма: <b>15000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy182'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🎆Марки <b>5шт</b>\n❕ Сумма: <b>30000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy183'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🎆Марки <b>10шт</b>\n❕ Сумма: <b>50000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy191'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🏃‍♂️Амфетамин <b>1гр</b>\n❕ Сумма: <b>6500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\nКомментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy192'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🏃‍♂️Амфетамин <b>2гр</b>\n❕ Сумма: <b>12500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy193'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🏃‍♂️Амфетамин <b>5гр</b>\n❕ Сумма: <b>30000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy200'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💸Кокаин <b>0.5гр</b>\n❕ Сумма: <b>30000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy201'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💸Кокаин <b>1гр</b>\n❕ Сумма: <b>50000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy202'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n💸Кокаин <b>2гр</b>\n❕ Сумма: <b>90000</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy211'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🍃План <b>4гр</b>\n❕ Сумма: <b>5500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['buy212'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу покупки.\n❕ Для продолжения покупки, следуйте инструкции\n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Для завершения покупки, <b>пополните</b> QIWI!\n🍃План <b>10гр</b>\n❕ Сумма: <b>10500</b> ТГ\n❕ QIWI кошелек: <b>'+str(QIWI)+'</b>\n❕ Комментарий платежа: ' '<b>' + str(random.randint(1, 9999)) + '</b>' + '\n➖➖➖➖➖➖➖➖➖➖➖➖\n💳Также для этого товара доступна оплата Kaspi, нажмите перейти к оплате по карте - /kaspi_card\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")

@bot.message_handler(commands=['kaspi_card'])
def start_message(message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу оплаты.\n❕ Для того, чтобы пополнить карту перейдите во вкладку «Карта другого банка». \n➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Реквизиты карты для <b>пополнения</b> Kaspi!\n❕ Имя и фамилия получателя :  <b>Azat Tasaev</b>\n❕ Kaspi: <b>'+str(VISA)+'</b>\n➖➖➖➖➖➖➖➖➖➖➖➖\n🔍 После оплаты, проверьте платёж командой : /check_payment', parse_mode="Html")


# ПРОВЕРКА ОПЛАТЫ
@bot.message_handler(commands=['check_payment'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу проверки платежа.\n'  + '<b>' + message.chat.first_name+ '</b>' + ', в данный момент платёж не найден. Повторите попытку через 5 минут.\n➖➖➖➖➖➖➖➖➖➖➖➖\n⚠️ Внимание! Платеж обрабатывается автоматически, товар выдается автоматически в данном диалоге.\nНе проверяйте платёж чаще чем в 5минут!\n➖➖➖➖➖➖➖➖➖➖➖➖\n♻️ Для перезапуска бота, введите /start\n➖➖➖➖➖➖➖➖➖➖➖➖\n', parse_mode="Html")

@bot.message_handler(commands=['check_ident'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, '➖➖➖➖➖➖➖➖➖➖➖➖\n❕ Вы перешли на страницу проверки платежа.\n'  + '<b>' + message.chat.first_name+ '</b>' + ', в данный момент платёж не найден. Повторите попытку через 5 минут.\n➖➖➖➖➖➖➖➖➖➖➖➖\n⚠️ Внимание! Платеж обрабатывается автоматически, контакты оператора для идентификации выдаётся в автоматическом режиме после оплаты.\n➖➖➖➖➖➖➖➖➖➖➖➖\n♻️ Для перезапуска бота, введите /start\n➖➖➖➖➖➖➖➖➖➖➖➖\n', parse_mode="Html")

bot.polling()

