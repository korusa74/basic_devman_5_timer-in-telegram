import os
import time
import ptbot
from pytimeparse import parse

TG_TOKEN = os.environ['TG_TOKEN']# подставьте свой ключ API

def take_params_wait(author_id, received_message):
    time_seconds = parse(received_message)
    message_id = bot.send_message(author_id, "Запускаю таймер!")
    time.sleep(1)
    bot.create_countdown(time_seconds, notify_progress, author_id=author_id, message_id=message_id, time_seconds=time_seconds)
    bot.create_timer(time_seconds, send_final_message, author_id=author_id)
    
def notify_progress(secs_left, author_id, message_id, time_seconds):
    bot.update_message(author_id, message_id, "Осталось {} секунд!".format(secs_left)+'\n'+ render_progressbar(time_seconds, time_seconds-secs_left))  

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def send_final_message(author_id):
    bot.send_message(author_id,'Время вышло!')
       
if __name__ == '__main__':
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(take_params_wait)
    bot.run_bot()

