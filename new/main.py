import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_mail():
    print("Старт функції")
    sender_email = 'illya.d.donchenko@ukr.net'
    sender_password = 'BGZHLEDbT3qfNA1N'
    receiver_email = 'illya.d.donchenko@gmail.com'# емейл користувача, кому ми надсилаємо емейл

    subject = "Ви виграли міліон" # заголовок повідомлення
    body = "Реклама апельсинів" # текст повідомлення

    # створення та налаштування повідомлення
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    print("Створенно повідомлення")

    # підключеня до серверу
    try:
        print("Підключення до серверу")
        with smtplib.SMTP_SSL("smtp.ukr.net", 465) as server:
            server.login(sender_email, sender_password) # авторизуємся на сервері
            server.sendmail(sender_email, receiver_email, msg.as_string()) # відправляємо повідомлення
            print("Повідомлення надіслано")
    except smtplib.SMTPException:
        print("Error: unable to mail")


schedule.every().day.at("16:34").do(send_mail)
count = 0
while True:
    count+=1
    print(count)
    schedule.run_pending()
    time.sleep(1)