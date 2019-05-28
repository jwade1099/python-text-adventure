#JUSTIN WADE
#5/21/19
#APCSP
#//////////////////////////////////

career1= ["Marine", "marine", "MARINE, ocean","a"]
career2= ["Astronomy", "astronomy", "space","b"]

male= ["boy","m","male"]
female= ["girl","f","female"]
enjoyment=0
study=0
datingval=0

answer_A= {"a","A","leave"}
answer_B= {"b", "B","go"}
answer_C= {"c", "C"}

smartz= ("\n good choice to study instead!\n")
funz=  ("\n You gotta have fun in college!\n")

invalid_answer = ("\nNot a valid answer\n")


gender=input("what is your gender (m/f)")
if gender in male:
    dating="girlfriend"
elif gender in female:
    dating="boyfriend"
else:
    dating= "partner"

print ("hello fellow student. You have been studying at Hopkinton Academy for two years now. It is now time to pick your final major")

print ("You are currently enrolled in marine research and astronomy. You must choose one now. Marine or astronomy?")

career= input(" > ")
if career in career1:
    print ("Very good choice of Marine biology!")
    pass
elif career in career2:
    print("yay You're going to space")
    pass
else:
    print (invalid_answer)
    print("Im serious....")
    career= input(" > ")
print(f"To become a major in {career}, you're going to have to study and work hard these next two years.\n\n")

def firstz():
    print("your friends are going out to a party, do you\n a) go to the party\n b) go to library to study\n")

    firstchoice= input(" > ")
    if firstchoice in answer_A:
        print(funz)
        global enjoyment
        enjoyment=enjoyment+1
    elif firstchoice in answer_B:
        print(smartz)
        global study
        study=study+1
    else:
        print(invalid_answer)
        firstz()

def secondz():
    print("wild weekend coming in! your friends are all going to the beach for the weekend, but you have a Lab coming up..")
    print("a) SEND IT to the beach!!\nb) gotta do well on this lab...\n")
    secondchoice= input(" > ")
    if secondchoice in answer_A:
        print(funz)
        global enjoyment
        enjoyment=enjoyment+1
    elif secondchoice in answer_B:
        print(smartz)
        global study
        study=study+1
    else:
        print(invalid_answer)
        secondz()

def thirdz():
    print("congratulation, that special someone wants to go out on a date...\na)GO!\nb)nah I don't have time\n")
    thirdchoice=input(" > ")
    if thirdchoice in answer_A:
        print(funz)
        print(f"congratulations you now have a {dating}. even helps you study..\n")
        global enjoyment
        global study
        global datingval
        enjoyment=enjoyment+3
        study=study+1
        datingval=datingval+1
    elif thirdchoice in answer_B:
        print(smartz)
        print("now you're kinda lonely and its harder to focus.. but you still have more time I guess..\n")
        study=study+1
    else:
        print(invalid_answer)
        thirdz()

def fourthz():
    global datingval
    if datingval==1:
        print("you are having relationship troubles, but the final exam is coming up...\n")
        print(f"a) leave your {dating}, you need time to prepare for the exam")
        print("b) you choose to work things out at ths cost of studying time")
        print("c)put it aside for now till after the exam")
        fourthchoice= input(" > ")
        if fourthchoice in answer_A:
            print("You wipe away your tears so you can see your books. Studying is hard to do right now\n")
            global enjoyment
            global study
            enjoyment=enjoyment-2
            study= study+1
            datingval=datingval-1

        elif fourthchoice in answer_B:
            print("your relationship is even stronger now <3")
            enjoyment=enjoyment+1
            study=study-1

        elif fourthchoice in answer_C:
            print(f"you have time to study, but you can not stop thinking of your {dating}")
            study=study+2
            hidden_path= input("Maybe its time.. take a guess A,B,C??\n")
            if hidden_path in answer_A:
                print(f"you're back with your {dating}, nice talk. you even did well on exam")
                enjoyment=enjoyment +1
                study=study+1
            elif hidden_path in answer_B:
                print(f"you're done with your {dating}, you're sad, but did well on exam")
                enjoyment=enjoyment -1
                study=study+2
                datingval=datingval-1
            elif hidden_path in answer_C:
                print("decide to go to a couples therapy session. who do you want to go see? \n ")
                print("a) someone all the way out of the way, good but time consuming\n")
                print("b)someone close and okay")
                print("c)ominous....")
                therapist= input(" > ")
                if therapist in answer_A:
                    print("Back together! better than ever!\n")
                    enjoyment=enjoyment+2
                    study= study-1

                elif therapist in answer_B:
                    print("your relationship is okay now <3")
                    enjoyment=enjoyment
                    study=study+1

                elif therapist in answer_C:
                    print("very interesting, a weird man greets you in an alley. (leave/go)")
                    alley_decision = input(" < ")
                    if alley_decision in answer_A:
                        print("sorry, you two broke up")
                        study=study+2
                        enjoyment=enjoyment-1
                        datingval=datingval-1
                    elif alley_decision in answer_B:
                        print("HEHEHE welcome children\n He hands you a potion, and you drink it. You are now back in love, and you gained infinite knowledge\n")
                        enjoyment=enjoyment +5
                        study=study+5
        else:
            print(invalid_answer)
            fourthz()
    else:
        print("you have extra time to study :)")
        study=study+2

def fifthz():
    global study
    global enjoyment
    global datingval
    if datingval==1:
        date_string= "have"
    else:
        date_string= "don't have"
    if study>=3:
        print("You have been invited to go on a science expedition.\n This include instant graduation and a job later. \na)go\nb)decline the offer")
        science_exp= input(" > ")
        if science_exp in answer_A:
            print(f"good choice you graduated with {enjoyment} happiness and a {study} smart level and you {date_string} a {dating}")
            enjoyment=enjoyment+1
        elif science_exp in answer_B:
            print(f"Congrats you declned and graduated with a {enjoyment} happiness and a {study} smart level and you {date_string} a {dating}")

        else:
            print(invalid_answer)
            fifthz()
    else:
        print("sorry you should have made better choices. failed out of college")
        return 0




#////////////////////////////////////////////////////////////////
firstz()
secondz()
thirdz()
fourthz()
fifthz()
