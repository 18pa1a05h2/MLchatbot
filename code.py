'''
This functions returns the greeting message according to the tym
'''
from datetime import datetime
import random
def current_time():
    current_time = datetime.now()
    greeting="\nGood morning"
    if current_time.hour>12 and current_time.hour<17:
        greeting="\nGood afternoon"
    elif current_time.hour>=17 and current_time.hour<22:
        greeting="\nGood evening"
    elif current_time.hour>=22:
        greeting="\nHi, its too late"
    return greeting
'''
This function gives the welcome message
'''

def welcome(name):
    message = [
        "\nHow can I help you?\n",
        "\nIs there anything I can help with?\n",
        "\nI hope you are doing well,How can i help you\n"
    ]
    print(f"{current_time()}! {name},\n {random.choice(message)}")

def Health_issue():
    print("1.Suffocation")
    print("2.low bp")
    print("3.high bp")
    print("4.heart attack")
    print("5.Reduce sugar levels")
    print("6.increase sugar levels")
    print("7.Snake bite")
    print("8.Food allergies")
    print("9.respiratory allergies")
    print("10.skin allergies ")
    try:
        return(int(input("Enter your health issue : ")))
    except :
        print("Invalid input")
        return 0

def Suffocation():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\nGrounding techniques\nMindful distractions\nTalk to your self\nExercise\nSelf care\nShock yourself\n")
    def Doctors_list():
        print("\nhttps://www.google.com/amp/s/www.credihealth.com/doctors/india/asthma/amp\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("\nSorry! Invalid input\n")
            option=case_situation()
    print_doctors()

def Low_bp():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\ntaking pomogranate juice gives instant relief\n")
    def Doctors_list():
         print("\nhttps://www.google.com/amp/s/www.credihealth.com/doctors/india/low-blood-pressure/amp\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("\nSorry! Invalid input\n")
            option=case_situation()
    print_doctors()

def High_bp():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("\nSorry! Invalid Input\n")
            return 0
    def emergency_instuctions():
        print("\npotassium and vitamin C rich foods like banana,oranges, lime water etc\n")
    def Doctors_list():
         print("\nhttps://www.google.com/amp/s/www.credihealth.com/doctors/india/blood-pressure-management/amp\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("\nSorry! Invalid input\n")
            option=case_situation()
    print_doctors()

def Heart_attack():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("Chew and swallow an aspirin, unless you are allergic to aspirin or have been told by your doctor never to take aspirin\nTake nitroglycerin\nBegin CPR if the person is unconscious")
    def Doctors_list():
         print("\nhttps://www.google.com/amp/s/www.indianhealthguru.com/cardiac-best-surgeons-top-hospitals-surgery-India.html")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("\nSorry! Invalid input\n")
            option=case_situation()
    print_doctors()

def Reduce_sugar_levels():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\nExercise Regularly\nControl Your Carb Intake\nIncrease Your Fiber Intake\nDrink Water and Stay Hydrated\nImplement Portion Control\nChoose Foods With a Low Glycemic Index\nControl Stress Levels\nMonitor Your Blood Sugar Levels.\n")
    def Doctors_list():
         print("\nhttps://www.medifee.com/list/best-hospitals-diabetes\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("Sorry! Invalid input")
            option=case_situation()
    print_doctors()

def Increase_sugar_levels():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\na piece of fruit like a banana,apple, or orange\n2 tablespoons of raisins\n15 grapes\n1/2 cup apple, orange, pineapple, or grapefruit juice\n1/2 cup regular soda (not sugar-free)\n1 cup fat-free milk\n1 tablespoon honey or jelly\n15 Skittles\n")
    def Doctors_list():
         print("\nhttps://www.hospitalkhoj.com/hospitals/diabetes#gsc.tab=0\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("Sorry! Invalid input")
            option=case_situation()
    print_doctors()

def Snake_bite():
    print("\nSelect any one option from 1 to 2\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\nMove the person beyond striking distance of the snake\nHave the person lie down with wound below the heart\nKeep the person calm and at rest, remaining as still as possible to keep venom from spreading\nCover the wound with loose, sterile bandage\nRemove any jewelry from the area that was bitten\nRemove shoes if the leg or foot was bitten\n")
    def print_doctors():
        option = case_situation()
        while option != 2:
            if option == 1:
                emergency_instuctions()
            else:
                print("\nSorry! Invalid input\n")
            option=case_situation()
    print_doctors()

def Food_allergies():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\nginger, turmeric and banana helps a lot\n")
    def Doctors_list():
         print("\nhttps://www.google.com/amp/s/www.credihealth.com/doctors/india/food-allergy/amp\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("Sorry! Invalid input")
            option=case_situation()
    print_doctors()

def Respiratory_allergies():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\npeppermint tea, steam inhalation with eucalyptus oil helps a lot\n")
    def Doctors_list():
         print("\nhttps://www.google.com/amp/s/www.credihealth.com/doctors/india/allergy/amp\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("\nSorry! Invalid input\n")
            option=case_situation()
    print_doctors()

def Skin_allergies():
    print("\nSelect any one option from 1 to 3\n")
    def case_situation():
        print("1.Emergency intructions")
        print("2.Doctors list")
        print("3.Go Back")
        try:
            return(int(input("Enter your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def emergency_instuctions():
        print("\nmint leaf or aloe vera paste or lemon to the region of affected area helps a lot\n")
    def Doctors_list():
         print("\nhttps://www.google.com/amp/s/www.credihealth.com/doctors/india/allergy/amp\n")
    def print_doctors():
        option = case_situation()
        while option != 3:
            if option == 1:
                emergency_instuctions()
            elif option == 2:
                Doctors_list()
            else:
                print("Sorry! Invalid input")
            option=case_situation()
    print_doctors()

def chatbot():
    print("\nThis bot helps you to find best doctors and gives emergency instructions for different health issues\n")
    name = input("Enter your name : ") 
    welcome(name)
    print("\nSelect any one of the below health issues so that you can know best doctors information from the URL and some emergency intructions for that particular health issue\n")
    choice = Health_issue()
    while choice != 11:
        if choice == 1:
            Suffocation()
        elif choice == 2:
            Low_bp()
        elif choice == 3:
            High_bp()
        elif choice == 4:
            Heart_attack()
        elif choice == 5:
            Reduce_sugar_levels()
        elif choice == 6:
            Increase_sugar_levels()
        elif choice == 7:
            Snake_bite()
        elif choice == 8:
            Food_allergies()
        elif choice == 9:
            Respiratory_allergies()
        elif choice==10:
            Skin_allergies()
        else:
            print("\nSelect a health issue from the above list\n")
    choice =Health_issue()
        
chatbot()
