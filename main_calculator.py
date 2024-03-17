import requests
from config_calculator import creator_sign


creator_sign()
print("Welcome on this multi-XMR-tool :)\nPress Enter. ")
input("")



#__________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________        
#_________________________________________________________main menu________________________________________________________________
#__________________________________________________________________________________________________________________________________

def main_menu():
    
    print("Main menu :")
    print("1. Solo mining XMR calculator")
    print("2. XMR Price in real time USD/EUR")
    print("3. Exit")

def main():
    from config_calculator import mining_calcul, price_xmr
    while True:
        main_menu()
        choice = input("Chose a tool : ")

        if choice == '1':
            mining_calcul()
        elif choice == '2':
            price_xmr()
        elif choice == '3':
            print("Bye ! :) ")
            break
        else:
            print("Retry with a valid option.")

main()