import random
while True :
    print( )
    game=input("agar mikhahid bazi konid benevisid (play)  va agar nemikhahid benevisid (exit)    ")
    if game==exit :
        break
    else :
        print( )
        dice=random.randint(1 , 6)
        if dice==6 :
            print("    shoma bordid")
        else:
            print("    shoma bakhtid") 