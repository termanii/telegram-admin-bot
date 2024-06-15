from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Directly add your bot token here
TOKEN = '7277467741:AAGx3IaYl0cGRa-R9cayasezkaHl_XlcPGU'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Become Admin", callback_data='become_admin')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome! Click the button to become an admin.', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    chat_id = query.message.chat.id

    try:
        context.bot.promote_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=True,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False
        )
        query.edit_message_text(text="You are now an admin! You can add people from your contacts.")
    except Exception as e:
        query.edit_message_text(text="Failed to promote you to admin.")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
