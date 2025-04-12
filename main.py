import os
from root.menu.data_visualisation import data_visualisation
from root.menu.basic_functionality import basic_functionality

def main():
    os.system('cls')
    print("МЕНЮ СИСТЕМИ МОНІТОРИНГУ СЕРВЕРІВ:\n")
    print("1 - Провести моніторинг серверів")
    print("2 - Візуалізація даних")
    print("3 - Вийти з програми")

    while True:
        choice = input("Ваш вибір: ")
        if choice == "1":
            basic_functionality()
        elif choice == "2":
            data_visualisation()
        elif choice == "3":
            print("Вихід з програми.")
            exit()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()