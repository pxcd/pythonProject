##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib



my_email = ""
password = ""


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


letter_number = random.randint(1, 3)

birthdays = pandas.read_csv("birthdays.csv")
# the dictionary key is a tuple (month, day) with value = to the whole data_row
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    name = birthdays_dict[today]["name"]
    print(name)
    email = birthdays_dict[today]["email"]
    print(email)

    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        letter_data = letter.read()
        print(letter_data)
        new_letter = letter_data.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", "587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{new_letter}"
        )






# 4. Send the letter generated in step 3 to that person's email address.




