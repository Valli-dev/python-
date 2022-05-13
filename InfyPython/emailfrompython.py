import smtplib
server= smtplib.SMTP('smtp.gmail.com', '587') #smtp object for gmail server and port number
server.starttls()
login=('vallimayilannamalai@gmail.com', 'Redmond@01')
sendmail= ('vallimayilannamalai@gmail.com', 'vjntele@gmail.com', 'Mail sent from python code')
print("mail sent")
