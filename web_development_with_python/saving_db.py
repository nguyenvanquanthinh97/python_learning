import csv


def saving_to_db(**kwargs):
    email = kwargs.get("email", "")
    subject = kwargs.get("subject", "")
    message = kwargs.get("message", "")

    with open('database.csv', newline='', mode="a") as db:
        writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])


