from Funcions.FuncionsPr import menu01, menu02

menuS = "*"*170
menu00 = "                                      _____                         ___              __   __  __      ______\n \
                                    / ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/\n \
                                    \__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /_\n \
                                   ___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/\n \
                                  /____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/"
menuOpc = "1) ADD/REMOVE/SHOW players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit"



opc = "0"
menuTotal = menuS + "\n" + menu00 + "\n" + menuS + "\n" + menuOpc
while opc.isdigit():
    print(menuTotal)
    opc = input("Select an option: ")
    if opc == "1":                                          #Menu00
        menu01()                                                   #Menu01
    if opc == "2":                                          #Menu00
        menu02()                                                   #Menu02
    if opc == "3":                                          #Menu00
        print("a")

    if opc == "4":                                          #Menu00
        print("a")

    if opc == "5":                                          #Menu00
        print("a")

    if opc == "6":                                          #Menu00
        break

