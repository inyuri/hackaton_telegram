from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from build_menu import build_menu

# Кнопки главного меню
button_list_main_menu = [
        InlineKeyboardButton("📦 Доступные заказы", callback_data='orders'),
        InlineKeyboardButton("🤗 Ваш профиль", callback_data='profile'),
        InlineKeyboardButton("📋 История заказов", callback_data='history')
    ]
main_menu_buttons = InlineKeyboardMarkup(build_menu(button_list_main_menu, n_cols=1))

# Кнопки меню со взятым заказом
button_list_menu_with_order = [
        InlineKeyboardButton("📦 Доступные заказы", callback_data='orders'),
        InlineKeyboardButton("🤗 Ваш профиль", callback_data='profile'),
        InlineKeyboardButton("📋 История заказов", callback_data='history'),
        InlineKeyboardButton("🚚 Статус заказа", callback_data='status_order')
    ]
menu_with_order_buttons = InlineKeyboardMarkup(build_menu(button_list_menu_with_order, n_cols=1))

# Кнопки перелистывания
scroll_list_menu = [
    InlineKeyboardButton("◀", callback_data='prev'),
    InlineKeyboardButton("✅ Взять заказ!", callback_data='take_order'),
    InlineKeyboardButton("▶️", callback_data='next'),
    InlineKeyboardButton("◀ Назад", callback_data='back')
]

scroll_menu_buttons = InlineKeyboardMarkup(build_menu(scroll_list_menu, n_cols=3))

# Кнопки статуса
button_list_status_order = [
    InlineKeyboardButton("✅ Подтвердить выполнение заказа", callback_data='confirm_order'),
    InlineKeyboardButton("❌ Отменить заказ", callback_data='cancel_order'),
    InlineKeyboardButton("◀ Назад", callback_data='menu_with_order')
]
status_order_buttons = InlineKeyboardMarkup(build_menu(button_list_status_order, n_cols=1))

# Кнопка возвращения в меню заказа
order_back_button = InlineKeyboardMarkup(build_menu([InlineKeyboardButton("◀ Назад", callback_data='menu_with_order')],
                                                    n_cols=1))

# Кнопка "Назад"
back_button = InlineKeyboardMarkup(build_menu([InlineKeyboardButton("◀ Назад", callback_data='back')], n_cols=1))