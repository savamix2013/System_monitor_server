import os
from root.gra_generation.widget import create_widgets
from root.gra_generation.data_loader import DataLoader

def data_visualisation():
    os.system('cls')
    print("Візуалізація даних...\n")
    
    data_loader = DataLoader("root/data/data_history.json")
    data_loader.load_from_file()

    create_widgets(data_loader.data_store)

    input("Натисніть Enter, щоб повернутися в меню.")
    from main import main
    main()