print("Hey!! shall we play a game?? I'll ask your fav no between 1-9 and guess your personality ")

while True:
    yesno = input("shall we start(yes/no)")
    if (yesno.lower().startswith("y")):
        print("Well!! I'am preparing to guess your personality")
        favnumber = int(input("Enter your favourite number between (1-9): "))
        if (favnumber != 0 and favnumber == 1):
            print("Wow you people are always the best in any job\nsometimes pretend to do so..LOL\nYou people think you only have one soulmate in this entire world and do anything for them.\nyou prefer to be single your entire life if not commited.\nyou dont follow the crowd and respect your individuality.\n")
        elif (favnumber == 2):
            print("You people are dicotomous (i.e) if you feel happy now..you believe u'll feel sad after sometime..\nits like this new anirudh's song(two two two) \nyou people play with emotions.\ninterestingly you have double personality.\nYou're a strong believer in your intutions.\n")
        elif (favnumber == 3):
            print("Three lovers think life's a party\nYou're outgoing and really funny people\nAt the same time you people are strongly  egotistical\nNo human can understand better than you especially when it comes to drama LOL \n")
        elif (favnumber == 4):
            print("You people are really reliable at anycost\nyou people are really brave and honest\nyou are stubborn in your decisions\n")
        elif (favnumber == 5):
            print("You can be very curious and energetic, but that can sometimes lead you to trouble making up your mind.\nyou people are highly excited\nThe most challenging characteristic is your ability to attract or cause drama\n Women nicknamed (drama queen) may be lovers of the number 5.\n")
        elif (favnumber == 6):
            print("Six lovers are caring and patient.\nyou have lots of ideas u want to share with the world,\n this can make you a little vain or self-righteous.\n you're prone to feeling lonely and therefore clingier in your relationships.\n")
        elif (favnumber == 7):
            print(" Due to your higher IQ, and can tend to be more impatient and critical of others.\nThe phrase ‘calm, cool, and collected’ may have been coined for a seven.\nHowever you are also very loyal and faithful people, who will stick by you're loved ones in times of crisis.\n")
        elif (favnumber == 8):
            print("Eight lovers don’t need sevens luck to be successful.\nThey tend to be pretty powerful on their own, and work very hard to get what they want\nyou are very balanced in terms of both personality and mood\n")
        elif (favnumber == 9):
            print("Nine lovers use thier talents and abilities effectively which makes them great leaders.\nit is also the number of magic,wisdom and fulfillment\nHowever, you can be moody at times.\nif you favour nine you likely love action and adventure\n")
        elif (favnumber < 0):
            print("if i had a physical structure like you i would like to have a date with you in that temperature in antartica ")
        else:
            print("Humans mere humans think they're too intelligent nav... :)\n sometimes they don't read the constraint\n sometime they do wantedly... LOL\n")
    elif (yesno.lower().startswith("n")):
        print("I gotcha mind voice.. Bye Bye.. :)")
        break
