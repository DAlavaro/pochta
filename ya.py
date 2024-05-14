import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv


def send_email(message):

    load_dotenv()
    sender = "dburunjuk@yandex.ru"
    password = os.getenv('PASS_YA')

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Candle_shop"
        server.sendmail(sender, sender, msg.as_string())
        return "The message was sent successfully!"
    except Exception as e:
        return f"{e}\n Check your login or password please!"
    finally:
        server.quit()


def main():
    message = "Количество просмотров товара x достигло 100!!!"
    print(send_email(message=message))


if __name__ == "__main__":
    main()