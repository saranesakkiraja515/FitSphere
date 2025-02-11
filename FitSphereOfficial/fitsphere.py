import datetime
import smtplib
import requests

def send_mail(contents, mail):
    connection =  smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("fitsphere2025@gmail.com", "spdn epsw lezj ejoz")
    connection.sendmail(
        from_addr="fitsphere2025@gmail.com",
        to_addrs=mail,
        msg=f"Subject:'Take care of your body. It's the only place you have to live.'!\n\n{contents}",
    )
    connection.close()

def day_of_weeks(name, mail, level_category):
    today = datetime.datetime.today()
    day_of_week = today.weekday()
    if day_of_week == 0:
        with open (f"{level_category}/monday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)

    elif day_of_week == 1:
        with open (f"{level_category}/tuesday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)

    elif day_of_week == 2:
        with open (f"{level_category}/wednesday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)

    elif day_of_week == 3:
        with open (f"{level_category}/thursday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)

    elif day_of_week == 4:
        with open (f"{level_category}/friday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)

    elif day_of_week == 5:
        with open (f"{level_category}/saturday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)

    else:
        with open (f"{level_category}/sunday", "r") as file:
            content = file.read()
            content = content.replace("[User's Name]", name)
            send_mail(content, mail)


response = requests.get(url="https://api.sheety.co/1b9f570a3d8e51a2d5f9f6b09f5d61e7/male/sheet1")
data = response.json()
for info in data["sheet1"]:
    name = info["name"]
    email = info["email"]
    level = info["level"]
    day_of_weeks(name, email, level)

response2 = requests.get(url="https://api.sheety.co/1b9f570a3d8e51a2d5f9f6b09f5d61e7/female/sheet1")
data = response2.json()
for info in data["sheet1"]:
    name = info["name"]
    email = info["email"]
    level = info["level"]

    day_of_weeks(name, email, level)


response1 = requests.get(url="https://api.sheety.co/1b9f570a3d8e51a2d5f9f6b09f5d61e7/food/sheet1")
data = response1.json()
for info in data["sheet1"]:
    name = info["name"]
    email = info["email"]
    preference = info["preferences"]
    day_of_weeks(name, email, preference)
