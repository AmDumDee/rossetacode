import datetime
today = datetime.date.today()

today.isoformat()

today.strftime("%A, %B %d, %Y")
"The date is {0:%A, %B %d, %Y}".format(d)

"The date is {date:%A, %B %d, %Y}".format(date=d)

f"The date is {d:%A, %B %d, %Y}"
