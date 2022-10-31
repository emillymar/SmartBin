#!/usr/bin/python

import RPi.GPIO as GPIO
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

TRIG, ECHO = 23, 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Olá camarada {update.effective_user.first_name}')

async def ultra_sonico(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        while True:
            GPIO.output(TRIG, False)
            time.sleep(2)
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance,2)
            print("Distance: ", distance, "cm")

            if distance < 20:
                break

        await update.message.reply_text(f'Olá {update.effective_user.first_name}, venha me esvaziar!')
    except KeyboardInterrupt:
        print("Cleaning up!")
        gpio.cleanup()
        await update.message.reply_text(f'Alguém parou o bot!')

app = ApplicationBuilder().token("5704127464:AAHf-wWKxjRxu7qxwytwIpcCVyTV0lOLngg").build()

app.add_handler(CommandHandler("ola",hello))
app.add_handler(CommandHandler("MeAvisa",ultra_sonico))

app.run_polling()
