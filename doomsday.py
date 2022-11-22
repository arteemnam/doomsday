import datetime
import random
import calendar
import time

def doomsday():
    start_date = datetime.date(1700, 1, 1)
    end_date = datetime.date(2400, 12, 31)

    random_date = start_date + (end_date - start_date) * random.random()
    random_date = datetime.datetime.combine(random_date, datetime.datetime.min.time())
    datum=(str(random_date.day) + "/" + str(random_date.month) + "/" + str(random_date.year))

    print("What day of week is " + datum + "?")

    #Uncomment the below line to show what the day is supposed to be
		#print("Hint: " + calendar.day_name[random_date.weekday()])

    guess = input("What is your guess? ")

    if guess.lower() == calendar.day_name[random_date.weekday()].lower():
        print("That is correct!")
    else:
        print("That is NOT correct!")

while True:
    doomsday()
