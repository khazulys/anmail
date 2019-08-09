#Anonymous Mail

import os
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
	def banner():

		os.system('clear')
		print ("""\033[1;31m
         _   _   _   _   _   _   _   _   _
        / \ / \ / \ / \ / \ / \ / \ / \ / \\
       ( A | n | o | n | y | m | o | u | s )
        \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/
			""")
		print ("\033[1;33m      Anonymous Mails.Coded by Termux Official")
	banner()

except KeyboardInterrupt:
	print ("GoodBye,Thanks for use..")

try:

	def sendmail():
		mail_content = str(input("\n\033[1;32m[√]\033[1;34m Your Messages:\n\033[1;36m>\033[1;37m "))
		sender_address = 'anonymousmailshack@gmail.com'
		sender_pass = 'diki0821'
		receiver_address = str(input("\033[1;32m[√]\033[1;34m Insert receiver mail:\n\033[1;36m>\033[1;37m "))
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = str(input("\033[1;32m[√]\033[1;34m Insert Subject Mail:\n\033[1;36m>\033[1;37m "))
		message.attach(MIMEText(mail_content, 'plain'))
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print ("\n\033[1;31m	[+]\033[1;33m Mail Successfully Send..")
	sendmail()

	while True:
		ul=str(input("\n\033[1;32m[√]\033[1;34m Do you want to try again?(y/n): "))
		if ul == "y":
			sendmail()
		elif ul == "n":
			print ("\033[1;31m[*]\033[1;33mSee you next time, Don't forget to donate..");print ("\n\033[1;31m	[+]\033[1;33m Redirecting in 10 sec..");sleep(0.10);os.system("termux-open https://www.instagram.com/termuxofficial");exit()
		break
		if not ul:
			os.system("termux open www.instagram.com/termuxofficial")

except KeyboardInterrupt:
	print ("\033[1;31m[*]\033[1;33m GoodByeeee..");print ("\n\033[1;32m[√]\033[1;35m Please support me on instagram. thanks..");sleep(2);os.system("termux-open https://www.instagram.com/termuxofficial")
except OSError:
	print ("[×] Errors")
