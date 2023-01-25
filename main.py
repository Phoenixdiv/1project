import sql as sql
import telebot
import sqlite3
#Создать таблицу
connection = sqlite3.connect('taxibd.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS taxibd (clients TEXT, telephone INT)')
connection.commit()
connection.close()

#Получить
#selector = sql.execute('SELECT * taxibd; ')
#print(selector.fetchall())


bot = telebot.TeleBot('5878105732:AAEZD0OtzpYk-yX-iluyVaf-nw7sw-IC7NA')

# Обработчик команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    bot.send_message(message.from_user.id('Здравствуйте', reply_markup=keyboard))
    bot.send_message(message.from_user.id(
        'Введите номер телефона.\nДля этого нажмите на кнопку "Мой профиль"'))

    bot.send_message(user_id)

        # Перекидываем на этап получения имени
    bot.register_next_step_handler(message, get_name)


# Этап получения имени
def get_name(message):
    username = message.text

    bot.send_message(message.from_user.id, 'Отправьте свой номер', reply_markup=buttons.number_button())

    # Переход на этап получения номера телефона
    bot.register_next_step_handler(message, get_number, username)


# Этап получения номера телефона
def get_number(message, username):
    user_id = message.from_user.id

    # Если отправил номер в виде контакта
    if message.contact:
        user_number = message.contact.phone_number

        bot.send_message(user_id, 'Отправьте локацию', reply_markup=buttons.location_button())

        # Переход на этап получения локации
        bot.register_next_step_handler(message, get_location, username, user_number)

    # Если не в виде контакта
    else:
        bot.send_message(user_id, 'Отправьте номер используя кнопку')

        # Обратно перекинуть на этап получения номера
        bot.register_next_step_handler(message, get_number, username)

