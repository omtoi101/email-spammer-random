import smtplib
from colorama import Fore
from colorama import init
import string
import random
from urllib.request import Request, urlopen

init()

print(colored('', 'green', 'on_red'))

print(Fore.RED + """

                                __ __                                                                               
                               /  /  |                                                                              
  ______  _____  ____   ______ $$/$$ |        _______  ______   ______  _____  ____  _____  ____   ______   ______  
 /      \/     \/    \ /      \/  $$ |       /       |/      \ /      \/     \/    \/     \/    \ /      \ /      \ 
/$$$$$$  $$$$$$ $$$$  |$$$$$$  $$ $$ |      /$$$$$$$//$$$$$$  |$$$$$$  $$$$$$ $$$$  $$$$$$ $$$$  /$$$$$$  /$$$$$$  |
$$    $$ $$ | $$ | $$ |/    $$ $$ $$ |      $$      \$$ |  $$ |/    $$ $$ | $$ | $$ $$ | $$ | $$ $$    $$ $$ |  $$/ 
$$$$$$$$/$$ | $$ | $$ /$$$$$$$ $$ $$ |       $$$$$$  $$ |__$$ /$$$$$$$ $$ | $$ | $$ $$ | $$ | $$ $$$$$$$$/$$ |      
$$       $$ | $$ | $$ $$    $$ $$ $$ |      /     $$/$$    $$/$$    $$ $$ | $$ | $$ $$ | $$ | $$ $$       $$ |      
 $$$$$$$/$$/  $$/  $$/ $$$$$$$/$$/$$/       $$$$$$$/ $$$$$$$/  $$$$$$$/$$/  $$/  $$/$$/  $$/  $$/ $$$$$$$/$$/       
                                                     $$ |                                                           
                                                     $$ |                                                           
                                                     $$/                                                            


""")


email_me = str(input(" enter your email: "))
email_pass = str(input(" enter your email password: "))

print('\n', '\n',
      'if you do not want to send to multiple emails just put the same email in each option DONT LEAVE IT BLANK THE '
      'CODE WONT WORK', '\n', '\n')
target_email = str(input(" enter target email 1 : "))
target_email2 = str(input(" enter target email 2 : "))
target_email3 = str(input(" enter target email 3 : "))
target_email4 = str(input(" enter target email 4 : "))
target_email5 = str(input(" enter target email 5 : "))
send_amount = int(input(" enter how many emails you want to send: "))
print("emails sent:")
index = 0


def email_spammer_lol():
    letters = string.ascii_letters

    global index
    index += 1
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(str(email_me), str(email_pass))

        smtp.sendmail('none@gmail.com', str(target_email), (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('none@gmail.com', str(target_email2),  (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('none@gmail.com', str(target_email3),  (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('none@gmail.com', str(target_email4),  (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('none@gmail.com', str(target_email5),  (''.join(random.choice(letters) for i in range(10))))
        print(str(index))


for x in range(int(send_amount)):
    email_spammer_lol()

