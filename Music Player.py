from playsound import playsound
import os
a = "on"
print("\n\n")
print("\t              @@@@@@@@@@@@@@@@ Music Player @@@@@@@@@@@@@@@@")
print("\n")
print("###################### Playlist ######################")
i = 1
files = os.listdir("C:\\Users\\Prithbiraj\\Music\\downloaded songs")
for file in files:
       print(str(i)+". "+file.title())
       i += 1
print("######################################################")
print("\n")
print("\t                                       ----- Developed By Prithbiraj Mahanta ")
print("\n")
while (a.lower()!="off"):
        
        choice = input("Please Enter The Song Number : ")
        print("\n")
        if choice.isdigit() and int(choice)<=len(files) and int(choice)>=1:
                print(f'\t         ########## "{files[int(choice)-1].title()}"  Playing... ##########')
                playsound("C:\\Users\\Prithbiraj\\Music\\downloaded songs\\"+files[int(choice)-1])
                print('\n')
                print("Choose What You Want Now : ")
                print("1. On\n2. Off")
                a = input("Enter [on-off] : ")
                while a.lower()!="on" and a.lower()!="off":
                                print("Invalid Keyword : ")
                                print("Choose What You Want Now : ")
                                print("1. On\n2. Off")
                                a = input("Enter [on-off] : ")
        else:
            print(f'Sorry :(  \nInvalid Number!')
            print("Choose What You Want Now : ")
            print("1. On\n2. Off")
            a = input("Type [on-off] : ")
            while a.lower()!="on" and a.lower()!="off":
                                print("Invalid Keyword : ")
                                print("Choose What You Want Now : ")
                                print("1. On\n2. Off")
                                a = input("Enter [on-off] : ")  
print("\n\n\n              #################### See You Again My Friend :) #####################\n")