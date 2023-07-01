import smtplib

# create an SMTP object
server = smtplib.SMTP('410413042@gms.ndhu.edu.tw', 587)

# start the SSL connection
server.starttls()

# login to the server
server.login("410413042@gms.ndhu.edu.tw", "R124594399")

# create the message
msg = "Hello,\n\nThis is a test email sent from Python."

# send the message
server.sendmail("410413042@gms.ndhu.edu.tw", "kewos554321@gmail.com", msg)

# close the connection
server.quit()
