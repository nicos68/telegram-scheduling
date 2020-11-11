import logging
import os

import arrow
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

timezone = 'Europe/Paris'


def daily(context):
    job_context = context.job.context
    chat_id = job_context.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text="It works !")


def schedule(update, context):
    hour, minute = [int(e) for e in context.args[0].split(':')]
    now = arrow.now()
    target_datetime = now.replace(tzinfo=timezone,
                              hour=hour, minute=minute,
                              second=0)
    utc_datetime = target_datetime.to('utc')
    time = utc_datetime.time()
    context.job_queue.run_daily(daily, time)


def main():
    logger.info("Starting up Bot")
    token = os.environ.get('TG_TOKEN')
    updater = Updater(token=token)
    updater.dispatcher.add_handler(CommandHandler(command='schedule', callback=schedule))

    updater.start_polling()
    logger.info('Bot started.')


if __name__ == '__main__':
    main()
