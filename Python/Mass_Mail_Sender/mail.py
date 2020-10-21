# import required libraries
import smtplib,os,sys,imghdr
from email.message import EmailMessage

# path of the certificates
path=os.getcwd()+"/certificates"

# email id and password of the user gmail account
EMAIL_ADDRESS = 'your.mail.id@gmail.com'#give your own email id here
EMAIL_PASSWORD = input("enter your email password: \n")

## Sending email part

# An SMTP object is created with host name and port number. ssl is for the secure connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # do the login of the user
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD )

    # get the certificates from the file system   
    dirs = os.listdir( path )
    count = 0
    for file in dirs:
        msg=EmailMessage()
        msg['Subject'] = 'Subject of Mail'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = "Email ID"
        msg.set_content('<b>Content of the mail.</b>')

       # open the certificate to add it as an attachment in binary read format
        with open('certificates/'+file,'rb') as f:
            file_data = f.read()
            # get the file type
            file_type = imghdr.what(f.name)
            file_name = 'Poster'
        # add the attachment in the msg
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        # send the mail
        smtp.send_message(msg)
        count = count + 1
        print("mail has been sent to user no. {count} {file} \n".format(count=count,file="person_name"))

print("all emails have been successfully delivered to {count} users".format(count=count))