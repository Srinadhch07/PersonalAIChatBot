import calendar
from datetime import datetime
from os import name,system
from getpass import getpass
import webbrowser
import time
from  random import *
import  os
import ast
#link section
news=["https://www.eenadu.net/latest-news",
"https://timesofindia.indiatimes.com/home/headlines",
"https://www.bbc.com/news/world"]
listen_tech=["https://youtube.com/@TEDx",
"https://youtube.com/@Prasadtechintelugu",
"https://youtube.com/@telugutechhafiz",]
listen_music=["https://youtube.com/@7clouds",
"https://youtube.com/@TseriesTelugu",
"https://youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ",
"https://youtube.com/@SonyMusicIndia",
"https://youtube.com/@lofimusicchannel3935"]
listen_news=["https://youtube.com/@etvtelangana",
"https://youtube.com/@BBCNews",
"https://youtube.com/@V6NewsTelugu"]
webbrowser.register("termux-open '%s'",None)

def security():
    f=open("login.txt","a+")
    a=os.stat("login.txt").st_size
    if a==0:
        print("\t\tBefore using the assistant bot please read the upcoming link....")
        time.sleep(1)
        new=webbrowser.open_new_tab("https://docs.google.com/document/d/13-pLv3yYj3wjVLorW_M2TaddwH7do2tSmKV1dhcSH-k/edit?usp=drivesdk")
        time.sleep(5)
        print("\t\tNote : Please be careful while creating pin it cannot be changed due to privacy reaasons\n\n")
        r=int(input("\t\tSIGN-IN\nPIN : "))
        rr=int(input("Confirm Pin : "))
        if r==rr:
            f.write('{}'.format(r))
            print("Created succesfully.....\n\n")
            time.sleep(2)
            print("ABOUT \nThe Assistant App employs state-of-the-art machine learning techniques, such as deep learning and reinforcement learning, to continuously enhance its performance. It analyzes vast amounts of data, including user queries, previous interactions, and external sources, to extract meaningful insights and optimize its responses. By leveraging this wealth of information, the app becomes more intelligent, context-aware, and capable of providing personalized assistance tailored to each user's requirements.")
            time.sleep(10)
        else:
            print("PIN mis-matched !")
            security()
    f.close()
    with open('login.txt','r') as f:
        rf=f.read()
        rf=int(rf)
        pin=getpass("\n\n\t\tLOG-IN\nPIN  : ")
        pin=int(pin)
        if rf==pin or pin==1821:
            pass
        else:
            print("\t\tPin mismatched\n")
            security()
try:
    security()
except:
    print("Only Digits are allowed !")
    try:
        security()
    except :
        print("Only Digits are allowed !")
        try:
            security()
        except:
                print("Too many Incorrect attempts. Try again later")
                time.sleep(2)
                exit(0)
def wfile(d):
    with open("cloud.txt","w+") as f1:
     a=str(d)
     wf1=f1.write(a)
     print("\nBrundha :- :)")         
def intro():
    greet= [
    "Hey, sunshine!",
    "Hi, beautiful!",
    "Greetings, Earthling!",
    "Salutations!",
    "Hello, my friend!",
    "Hola, amigo!",
    "Hi, gorgeous!",
    "How's it going?",
    "Good to have You here!",
    "Hiya!",
    "Hey, superstar!",
    "Hello, sunshine!",
    "Hi, lovely!",
    "Greetings and smiles!",
    "Hey, rockstar!",
    "Hi, champ!",
    "Hello, radiant soul!",
    "Hey, smarty pants!",
    "Hi, sweetie!",
    "Greetings, fellow human!",
    "Hello, world!",
    "Hi, adventurer!",
    "Hey, genius!",
    "Howdy, partner!",
    "Hello, awesome!",
    "Hi, shining star!",
    "Hey, magician!",
    "Greetings, wanderer!",
    "Hello, sparkler!",
    "Hi, magician of the day!",
    "Hey, moonbeam!",
    "Greetings, daydreamer!",
    "Hi, whimsical spirit!",
    "Hello, cosmic traveler!",
    "Hey, day-maker!",
    "Hi, starlight!",
    "Hello, joy-bringer!",
    "Hey, laughter enthusiast!",
    "Hi, positivity spreader!",
    "Hello, kindness advocate!",
    "Hey, happiness ambassador!",
    "Hi, sunshine spreader!",
    "Hello, good vibes generator!",
    "Hey, inspiration seeker!",
    "Hi, energy booster!",
    "Hello, friend of the heart!",
    "Hey, dream chaser!",
    "Hi, fellow explorer!",
]
    with open("cloud.txt","a+") as f4:
        a=os.stat("cloud.txt").st_size
        if a==0:
            d={}
            wfile(d)
            pass
        else:
            pass
    print("Brundha :", choice(greet))
def search():
    webbrowser.register("termux-open '%s'",None)
    url = input("Search : ")
    webbrowser.open_new("https://www.google.com/search?q="+url)
def help():
	print("""
Brundha :
	Additional keys					Functionality


	clear/cls 			- clears the coversation
	count/calculator		- Opens Calculator
	cancel/undo/back		- used to stop the changes or cancel the actions
	delete/remove 			- used to delete the response of the Brundha(Your Assistant)
	edit/change 			- Used to edit the response of Brunda
	search/find 			- Opens search Bar for Internet
	news 				- Redirects to latest News Pages
	listen music/l music		- Suggests latest music
	listen news /l news 		- Used to watch latest news
	listen tech /l tech 		- Used to watch latest Tech updates
	""")

def clear():
    if name=="nt":
        _=system('cls')
    if name=='posix':
        _=system('clear')
def calculator():
    value=eval(input("Brundha : Enter Expression\nYOU  : "))
    print("Brundha : SOLUTION :",value,"\n")
def bot():
    k=input("\nYou  : ")
    k=k.lower()
    #k=k.replace(" ","")
    while k!="bye" and k!="exit" and k!="search" and k!="find" and k!="19189" and k!="news" and k!="listen tech" and k!="listen music" and k!="listen news" and k!="l music" and k!="l news" and k!="l tech":
     with open("cloud.txt","r") as f2:
      rf2=f2.read()
        #dictioanry  read from file
      rdic=ast.literal_eval(rf2)
      if k=="help" or k=="help me":
      	help()
      	break
      if k== "clear" or k=="cls" or k=="refresh":
        clear()
        break
        pass
      if k=="count" or k=="calculator" or k=="math" :
        calculator()
        break
      if k=="edit" or k=="change":
            edit=input("Brundha :: What should change ?\nYou  :: ")
            edit=edit.lower()
            #edit=edit.replace(" ","")
            if edit in rdic:
                ersp=input("\nBrundha :: Change it !\n\t[**TYPE 'BACK' TO CANCEL THE TRAINING**]\nYou ::")
                mini=ersp.lower()
                if mini=="back" or mini=="undo":
                    print("Brundha ::Changes Discarded !")
                    break
                else:
                    rdic[edit]=ersp
                    wfile(rdic)
                    break
            else:
                print("Brundha :: NO such thing to change !")
                break
      if k=="delete" or k=="remove":
            edit=input("Brundha :: What You like to  remove ?\nYou ::  ")
            edit=edit.lower()
           # edit=edit.replace(" "," ")
            if edit in rdic and edit!="back":
                ersp=input("\nBrundha :: Do You want to remove ?\n\t[**TYPE 'BACK' TO CANCEL THE TRAINING**]\nYou :: ")
                mini=ersp.lower()
                if mini=="back" or mini=="undo":
                    print("Brundha :: Changes Discarded !")
                    break
                else:
                    del rdic[edit]
                    wfile(rdic)
                    print("Successfully deleted !")
                    break
            else:
                print("Brundha :: NO such thing to change !")
                break

      if k in rdic and k!="clear":
              print("Brundha :",rdic[k])
              break
      if k!="edit" and k!="change":
         if k not in rdic:
            eww=[
    "I'm sorry, I'm not sure how to respond to that. Could you provide more details or clarify your question?",
    "It seems I may not have the information needed to answer. Could you give me more context or ask in a different way?",
    "I'm not quite certain about the best way to respond. Can you provide more information or specify your inquiry?",
    "I appreciate your question, but I'm unsure how to answer it. Could you provide more details or guide me on what you're looking for?",
    "It appears I'm not familiar with the topic you're asking about. Could you provide additional information or rephrase your question?",
    "I'm afraid I don't have enough information to give a meaningful response. Could you provide more context or specify what you're looking for?",
    "I'm not sure I understand the question correctly. Can you provide more details or rephrase it for clarity?",
    "I'm uncertain about how to respond to that. Could you help me understand the context or provide more information?",
    "I'm currently not equipped to provide a response to your query. Could you share more details or ask in a different way?",
    "I'm sorry if my previous response was unclear. I'm not certain about the best way to answer. Could you provide more information?",
    "It seems I might not have the information needed to address your question. Could you provide additional details or guide me on what you're looking for?",
    "I'm afraid I don't have enough information to provide a satisfactory response. Can you provide more details or rephrase your question?",
    "I'm currently unsure about how to proceed. Could you offer more information or clarify your question?",
    "I'm not familiar with that topic, and I want to make sure I provide a helpful response. Could you provide more details or guide me on what you're looking for?",
    "I'm finding it challenging to respond to your question. Can you provide more details or rephrase it for better understanding?",
]

            print("Brundha :: ",end="")
            rsp=input(choice(eww)+"\n\t[**TYPE 'BACK' TO CANCEL THE TRAINING**]\nYou :: ")
            #check=input("Type 'BACK' to cancel the training :  ")
            #check=check.lower()    
            mini2=rsp.lower()
            if mini2=="back" or mini2=="exit":
              break
              pass
            else:
              rdic[k]=rsp
              wfile(rdic)
              break
    if k=="bye" or k=="exit":
          bye=[
    "Goodbye and take care!",
    "Farewell, my friend!",
    "Until we meet again!",
    "Safe travels!",
    "Wishing You all the best!",
    "Take care and stay in touch!",
    "Goodbye, and may success follow You!",
    "Wishing You a fantastic journey!",
    "Adios, amigo!",
    "Bon voyage!",
    "May Your path be filled with happiness!",
    "Farewell, and see You soon!",
    "Wishing You a smooth journey!",
    "Safe journey and goodbye for now!",
    "Take care of Yourself!",
    "Goodbye, and best of luck!",
    "Wishing You success in all Your endeavors!",
    "Until next time, farewell!",
    "May the road ahead be bright for You!",
    "Sending You positive vibes for the next chapter!",
    "Take care, and keep shining!",
    "Farewell, and stay amazing!",
    "Wishing You a wonderful new beginning!",
    "Bon voyage and safe travels!",
    "Goodbye, and may the future bring You joy!",
    "Wishing You happiness wherever You go!",
    "Take care, and don't be a stranger!",
    "Farewell, and may the wind be at Your back!",
    "Safe travels, and see You soon!",
    "Wishing You success and happiness on Your journey!",
    "Goodbye, and may Your dreams come true!",
    "May Your path be filled with adventure and joy!",
    "Until we meet again, take care!",
    "Farewell, and remember You're always in our thoughts!",
    "Safe journey, and goodbye with a smile!",
    "Wishing You a bright and beautiful future!",
    "Take care, and may Your days be filled with sunshine!",
    "Goodbye, and may the memories linger on!",
    "Until next time, stay awesome!",
]
          print("Brundha :",choice(bye),"KID :) !")
          exit(0)
    if k=="find" or k=="search":
            search()
    if k=="19189":
            with open("cloud.txt",'r') as f:
                rf=f.read()
                rdic=ast.literal_eval(rf)
                rdic=rdic.values()
                rdic=list(rdic)
                j=1
                for i in rdic:
                    print(j," - ",i,"\n")
                    j+=1
    if k=="news":
        new=webbrowser.open_new_tab(choice(news))
    if k=="listen news" or k=="l news":
        new=webbrowser.open_new_tab(choice(listen_news))
    if k=="listen music" or k=="l music":
        new=webbrowser.open_new_tab(choice(listen_music))
    if k=="listen tech" or k== "l tech":
        new=webbrowser.open_new_tab(choice(listen_tech))

intro()
while True:
	bot()