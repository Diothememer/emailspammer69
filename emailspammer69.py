import smtplib

num = 1000


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login("mohammadpalekar456@gmail.com","toxzgfxmtnnkrafe")

	subject = 'iniate ngerian prince scam?'
	body = 'this email was written by a python script made by  yours truly i nammed this script the nigerian prince scam cuze that is what this was made to do scam peopl!'

	msg = f"Subject: {subject}\n\n{body}"

	smtp.sendmail("mohammadpalekar456@gmail.com","ahmedjaser4@gmail.com",msg)

	for i in range(0,1000):
		smtp.sendmail("mohammadpalekar456@gmail.com","ahmedjaser4@gmail.com",msg)
		print('your scam is complete')







