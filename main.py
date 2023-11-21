import logging

from telegram import InputMediaPhoto
from telegram.ext import Application, MessageHandler, CommandHandler, CallbackQueryHandler,\
    ConversationHandler, filters

from config import BOT_TOKEN
from buttons import *
import sqlite3

import requests
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# Подключение к БД
con = sqlite3.connect('db/db.sqlite3')
cur = con.cursor()


async def start(update, context):
    users_id = [i[0] for i in list(cur.execute('SELECT id FROM dbase_courier'))]
    if update.effective_user.id in list(users_id):
        await update.message.reply_text(f'<b>Приветствуем в личном кабинете {update.effective_user.first_name}!</b>',
                                        parse_mode='HTML', reply_markup=main_menu_buttons)
    else:
        await update.message.reply_text(f'<b>К сожалению вы еще не зарегистрированы. Чтобы зарегистрироваться пройдите'
                                        f' регистрацию на нашем сайте: .</b>',
                                        parse_mode='HTML')


async def profile(update, context):
    await update.callback_query.edit_message_text(f'<b>Тут информация {update.effective_user.first_name}!</b>',
                                                  parse_mode='HTML', reply_markup=back_button)


async def orders_view(update, context):
    orders_list = list(cur.execute('SELECT * FROM dbase_orders'))
    orders = [(order[0], order[1], order[2]) for order in orders_list]

    context.user_data['current_index'] = 0
    current_index = context.user_data['current_index']
    await update.callback_query.edit_message_text(orders[current_index], reply_markup=scroll_menu_buttons)


async def orders_scroll(update, context):
    orders_list = list(cur.execute('SELECT * FROM dbase_orders'))
    orders = [(order[0], order[1], order[2]) for order in orders_list]

    if update.callback_query.data == 'prev':
        context.user_data['current_index'] -= 1
    elif update.callback_query.data == 'next':
        context.user_data['current_index'] += 1

    orders_index = orders[context.user_data['current_index'] % len(orders)]

    await update.callback_query.edit_message_text(orders_index, reply_markup=scroll_menu_buttons)


async def orders_history(update, context):
    await update.callback_query.edit_message_text(f'<b>Тут история заказов {update.effective_user.first_name}!</b>',
                                                  parse_mode='HTML', reply_markup=back_button)


async def take_order(update, context):
    await update.callback_query.edit_message_text(f'<b>Вы успешно взяли заказ {update.effective_user.first_name}!</b>',
                                                  parse_mode='HTML', reply_markup=order_back_button)


async def menu_with_order(update, context):
    await update.callback_query.edit_message_text(f'<b>Приветствуем в личном кабинете {update.effective_user.first_name}!</b>',
                                                  parse_mode='HTML', reply_markup=menu_with_order_buttons)


async def status_order(update, context):
    await update.callback_query.edit_message_text(f'<b>Информация о заказе {update.effective_user.first_name}!</b>',
                                                  parse_mode='HTML', reply_markup=status_order_buttons)


async def back(update, context):
    await update.callback_query.edit_message_text(f'<b>Приветствуем в личном кабинете {update.effective_user.first_name}!</b>',
                                                  parse_mode='HTML', reply_markup=main_menu_buttons)


def main():

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CallbackQueryHandler(profile, pattern='profile'))
    application.add_handler(CallbackQueryHandler(orders_view, pattern='orders'))
    application.add_handler(CallbackQueryHandler(orders_history, pattern='history'))
    application.add_handler(CallbackQueryHandler(orders_scroll, pattern='prev'))
    application.add_handler(CallbackQueryHandler(orders_scroll, pattern='next'))
    application.add_handler(CallbackQueryHandler(take_order, pattern='take_order'))
    application.add_handler(CallbackQueryHandler(menu_with_order, pattern='menu_with_order'))
    application.add_handler(CallbackQueryHandler(status_order, pattern='status_order'))
    application.add_handler(CallbackQueryHandler(back, pattern='back'))

    application.run_polling()


if __name__ == '__main__':
    main()



