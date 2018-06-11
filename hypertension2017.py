def stghtn(sys, dia):
    HTN = 4  # 0: no HTN, 1: elevated BP, 2: HTN stage 1, 3: HTN stage 2
    interpretHTN = ["Normal blood pressure, no hypertension",
                    "Elevated blood pressure, pre-hypertension",
                    "Stage 1 hypertension, treatment recommended",
                    "Stage 2 hypertension, treatment recommended",
                    "Stage 2 hypertension with high chance for end-organ damage"]
    if sys < 90 or dia < 60:  # check for hypotension
        print("Your blood pressure is very low, please be careful of fainting!")

    emergency = True
    while emergency == True:
        if sys >= 180 or dia >= 120:
            e1mergency = True
            addsym = input("Are you experiencing any new symptoms of organ damage such as "
                           "chest pain, headaches, or abnormal sensations? "
                           "Y/N ").lower()
            if addsym == "y" or addsym == "yes":
                print("Please report to the emergency room")
                break
            elif addsym == "n" or addsym == "no":
                print("Please consult with your healthcare provider for additional therapy")
                break
            else:
                print("Please enter a valid entry (Y/N) ")

        elif sys >= 140 or dia >= 90:
            emergency = False
            HTN = 3
        elif 130 <= sys < 140 or 80 <= dia < 90:
            emergency = False
            HTN = 2
        elif 120 <= sys < 130:
            emergency = False
            HTN = 1
        else:
            emergency = False
            HTN = 0

    print(interpretHTN[HTN])
if __name__ == "__main__":

    disclaimer = "This application is based on the ACC/AHA 2017 Hypertension guidelines \n" \
                 "and does not provide medical advice, diagnosis or treatment, \n" \
                 "and is to be used for informational purposes only.\n" \
                 "Always seek the advice of your physician or other qualified health provider \n" \
                 "with any questions you may have regarding a medical condition. \n"
    print(disclaimer)
    #age = input("What is your age in years? ")
    BP = input("What is your blood pressure? ")
    #BP = "181/80"
    BP = BP.split("/")
    sys = int(BP[0].strip())
    dia = int(BP[1].strip())

    stghtn(sys,dia) # run command
    end = ""
    while end == "":  #pause and keeps results on screen
        end = input("Press Enter to exit ")
        end = 1
