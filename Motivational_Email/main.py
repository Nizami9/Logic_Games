# import smtplib
#
# my_email = "nizami.python@gmail.com"
# password = "gnzrtldhwvktahis"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="nizami.suleymanoff@yahoo.com",
#         msg="Subject:Hello\n\nThis is body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1994, month=6, day=22, hour=4 )
# print(date_of_birth)

import smtplib
import datetime as dt
import random

my_email = "nizami.python@gmail.com"
my_password = "fenlwqxhdglmewqt"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
