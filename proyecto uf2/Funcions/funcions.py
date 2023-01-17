import time
from random import randint

import dades as dades

import mysql.connector
mydb = mysql.connector.connect(
    host="dbvad.mysql.database.azure.com",
    user="GPVAD",
    password="123Valeriaandreadiego.",
    database="SAH"
)
mycursor = mydb.cursor()
# Función para la gestión de menús

def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[]):
    print(textOpts)
    while True:
        opc = input(inputOptText)

        if opc.isdigit():
            opc = int(opc)
        try:
            if opc not in rangeList and opc not in exceptions:
                raise ValueError("===============================================================Invalid Option====="
                                 "==========================================================\n")
            else:
                return opc
        except ValueError as e:
            print(e)
            input("Press enter to continue")

# Menú 0

def menu00():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu00)
        textOpts = "1)ADD/REMOVE/SHOW players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\nS)Exit"
        inputOptText = "Option: "
        lista = [1, 2, 3, 4, 5]
        exceptions = ["S", "s"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu01()
        elif opc == 2:
            menu02()
        elif opc == 3:
            menu03()
        elif opc == 4:
            menu04()
        elif opc == 5:
            menu05()
        elif opc in exceptions:
            dejar_este_nivel = True


# Menú 1

def menu01():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu01)
        textOpts = "1)New Human Player\n2)New Bot\n3)Show/Remove Players\nS)Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3]
        exceptions = ["S", "s"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu011()
        elif opc == 2:
            menu012()
        elif opc == 3:
            menu013()
        elif opc in exceptions:
            dejar_este_nivel = True

# Opciones del menú 1


def menu011():
    nameOK = False
    DNIOK = False
    typeofplayerOK = False
    try:
        mycursor.execute("SELECT player_id FROM player")
        myresult = mycursor.fetchall()
        name = input("Name: ")
        if name.isalnum():
            nameOK = True
        else:
            raise ValueError("Incorrect name, please, enter a name not empty with only letters")
        nif = input("NIF: ")
        if not len(nif) == 9 or not nif[:8].isdigit() or not nif[8].isalpha():
            raise ValueError("Wrong NIF")
        elif not dades.DNILetras[int(nif[:8]) % 23] == nif[8].upper():
            raise ValueError("Wrong NIF")
        for i in myresult:
            for j in i:
                if nif == j:
                    raise ValueError(f"NIF {nif} already exists")
        else:
            DNIOK = True
        typeofplayer = input("Select your Profile:\n1)Cautious\n2)Moderated\n3)Bold\n>Option: ")
        if typeofplayer != "1" and typeofplayer != "2" and typeofplayer != "3":
            raise ValueError("===============================================================Invalid Option====="
                             "==========================================================\n")
        else:
            typeofplayerOK = True
            typeofplayer = int(typeofplayer)
            lista = ["g", "Catious", "Moderated", "Bold"]

        if nameOK and DNIOK and typeofplayerOK:

            print(f"Name:{name.rjust(20)}\nDNI:{nif.rjust(21)}\nProfile:{lista[typeofplayer].rjust(17)}")

            question = input("\nIs ok? Y/n: ")

            if question == "Y" or question == "y":
                sql = "INSERT INTO player (player_id, player_name, player_risk, human) VALUES (%s, %s, %s, %s)"
                val = (nif, name, typeofplayer, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "Record Inserted")
                menu01()
            else:
                menu01()
        else:
            print("There's an error")
    except ValueError as e:
        print(e)
        input("Enter to Continue ")
        menu011()

def newRandomDNI():
    NUMBER_DNI = randint(10000000, 99999999)
    LETTER_DNI = dades.DNILetras[NUMBER_DNI % 23]
    nif_bot = str(NUMBER_DNI) + str(LETTER_DNI)
    return nif_bot

def menu012():
    nameOK = False
    typeofplayerOK = False
    try:
        name = input("Name: ")
        if name.isalnum():
            nameOK = True
        else:
            raise ValueError("Incorrect name, please, enter a name not empty with only letters")

        nif_bot = newRandomDNI()
        print(f"Name:     {name}")
        print(f"DNI:      {nif_bot}")

        typeofplayer = input("Select Profile For The New Boot:\n1)Cautious\n2)Moderated\n3)Bold\n>Option: ")
        if typeofplayer != "1" and typeofplayer != "2" and typeofplayer != "3":
            raise ValueError("===============================================================Invalid Option====="
                             "==========================================================\n")
        else:
            typeofplayerOK = True
            typeofplayer = int(typeofplayer)
            lista = ["g", "Catious", "Moderated", "Bold"]

        if nameOK and typeofplayerOK:

            print(f"Name:{name.rjust(20)}\nDNI:{nif_bot.rjust(21)}\nProfile:{lista[typeofplayer].rjust(17)}")

            question = input("\nIs ok? Y/n: ")

            if question == "Y" or question == "y":
                sql = "INSERT INTO player (player_id, player_name, player_risk, human) VALUES (%s, %s, %s, %s)"
                val = (nif_bot, name, typeofplayer, 0)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "Record Inserted")
                menu01()
            else:
                menu01()
        else:
            print("There's an error")
    except ValueError as e:
        print(e)
        input("Enter to Continue ")
        menu011()

def removeBBDDPlayer():
    dict_humanos = {}
    list_dict_h = []
    dict_robot = {}
    list_dict_r = []
    dict_player = {1: dict_robot, 2: dict_humanos}
    lista = ["g", "Catious", "Moderated", "Bold"]
    mycursor.execute("SELECT human, player_id, player_name, player_risk FROM player")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[0] == 0:
            dict_robot.update({x[1]: {"Name": x[2], "Profile": lista[x[3]], "Human": x[0]}})
            list_dict_r.append(x)
        elif x[0] == 1:
            dict_humanos.update({x[1]: {"Name": x[2], "Profile": lista[x[3]], "Human": x[0]}})
            list_dict_h.append(x)

    showBBDDPlayer()

    print(dades.asteriscos)
    question = input("Option ( -id to remove player, -1 to exit): \n")
    if question[0] == "-" and question[1:] in dict_robot or question[1:] in dict_humanos:
        question = question[1:]
        sql = f"DELETE FROM player WHERE player_id = '{question}'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    elif question == "-1":
        menu01()
    else:
        print("===============================================================Invalid Option====="
              "==========================================================")
        input(" " * 58 + "Press enter to continue" + " " * 59)
        menu013()

def menu013():
    print(dades.cabecera_menu013)
    removeBBDDPlayer()


# Menú 2

def menu02():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu02)
        textOpts = "1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\nS)Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3]
        exceptions = ["S", "s"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu021()
        elif opc == 2:
            menu022()
        elif opc == 3:
            menu023()
        elif opc in exceptions:
            dejar_este_nivel = True

# Opciones del menú 2

def showBBDDPlayer():
    dict_humanos = {}
    list_dict_h = []
    dict_robot = {}
    list_dict_r = []
    dict_player = {1: dict_robot, 2: dict_humanos}
    lista = ["g", "Catious", "Moderated", "Bold"]
    mycursor.execute("SELECT human, player_id, player_name, player_risk FROM player")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[0] == 0:
            dict_robot.update({x[1]: {"Name": x[2], "Profile": lista[x[3]], "Human": x[0]}})
            list_dict_r.append(x)
        elif x[0] == 1:
            dict_humanos.update({x[1]: {"Name": x[2], "Profile": lista[x[3]], "Human": x[0]}})
            list_dict_h.append(x)

    sum = "0"
    while sum.isdigit():
        lista_identificador = []

        try:
            if len(list_dict_h) >= len(list_dict_r):
                if len(list_dict_r) == int(sum):
                    raise TypeError(f"{sum}", "hMayor")
                if isinstance(list_dict_h, list):
                    print(f"{list_dict_r[int(sum)][1]}".ljust(20) + f"{list_dict_r[int(sum)][2]}".ljust(
                        25) + f"{lista[list_dict_r[int(sum)][3]]}".ljust(25) + "||", end="")
                    print("", f"{list_dict_h[int(sum)][1]}".ljust(19), f"{list_dict_h[int(sum)][2]}".ljust(24),
                          f"{lista[list_dict_h[int(sum)][3]]}")

                sum = int(sum)
                sum += 1
                sum = str(sum)

            elif len(list_dict_h) < len(list_dict_r):
                if len(list_dict_h) == int(sum):
                    raise TypeError(f"{sum}", "rMayor")
                if isinstance(list_dict_h, list):
                    print(f"{list_dict_r[int(sum)][1]}".ljust(20) + f"{list_dict_r[int(sum)][2]}".ljust(
                        25) + f"{lista[list_dict_r[int(sum)][3]]}".ljust(25) + "||", end="")
                    print("", f"{list_dict_h[int(sum)][1]}".ljust(19), f"{list_dict_h[int(sum)][2]}".ljust(24),
                          f"{lista[list_dict_h[int(sum)][3]]}")
                sum = int(sum)
                sum += 1
                sum = str(sum)

        except TypeError as TE:
            x, y = TE.args
            sum = int(x)
            if y == "hMayor":
                while sum < len(list_dict_h):
                    print(f"||".rjust(72) + f" {list_dict_h[int(sum)][1]}".ljust(20),
                          f"{list_dict_h[int(sum)][2]}".ljust(24), f"{lista[list_dict_h[int(sum)][3]]}")
                    sum += 1
                sum = "a"
            if y == "rMayor":
                while sum < len(list_dict_r):
                    print(f"{list_dict_r[int(sum)][1]}".ljust(20) + f"{list_dict_r[int(sum)][2]}".ljust(
                        25) + f"{lista[list_dict_r[int(sum)][3]]}".ljust(25) + "||")
                    sum += 1
                sum = "a"

def showhPlayersGame():
    print(" " * 40 + "*******************ActualPlayersInGame*******************" + " " * 40)
    cadena = str()
    for i in dades.player_seleccionado:
        cadena = cadena + (' ' * 50 + str(i) + '    ' + dades.player_seleccionado[i].get("Name") + '  ' +
                           dades.player_seleccionado[i].get("Human") +
                           '   ' + dades.player_seleccionado[i].get("Profile") + '\n')
    print(cadena)

    input(" " * 58 + "Press enter to continue" + " " * 59)

def menu021():
    print(dades.cabecera_menu021)

    if dades.player_seleccionado == {}:

        print(" " * 40 + "*******************ActualPlayersInGame*******************" + " " * 40)
        print(" " * 55 + "There is no players in game" + " " * 55)
        input(" " * 60 + "Enter to continue" + " " * 63)
        print(dades.cabecera_menu0211)

        dict_humanos = {}
        dict_robot = {}
        lista = ["g", "Catious", "Moderated", "Bold"]
        mycursor.execute("SELECT human, player_id, player_name, player_risk FROM player")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == 0:
                dict_robot.update({x[1]: {"Name": x[2], "Profile": lista[x[3]]}})
            elif x[0] == 1:
                dict_humanos.update({x[1]: {"Name": x[2], "Profile": lista[x[3]]}})

        showBBDDPlayer()

        print(dades.asteriscos)
        question = input("Option (id to add to game, -id to remove player, sh to show actual players in game, "
                         "-1 to go back:\n")

        while question != "-1":
            if question not in dades.player_seleccionado:
                if question in dict_robot or question in dict_humanos:
                    lista = ["g", "Catious", "Moderated", "Bold"]
                    human = ["Human", "Boot"]
                    mycursor.execute("SELECT player_id, player_name, human, player_risk FROM player")

                    myresult = mycursor.fetchall()

                    for x in myresult:
                        if x[0] == question:
                            dades.player_seleccionado.update({x[0]: {"Name": x[1], "Human": human[x[2]], "Profile": lista[x[3]]}})

                    showhPlayersGame()
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input("Option (id to add to game, -id to remove player, sh to show actual players in game, "
                                     "-1 to go back:\n")
                elif question[0] == "-" and question[1:] in dict_robot or question[1:] in dict_humanos:
                    question = question[1:]
                    sql = f"DELETE FROM player WHERE player_id = '{question}'"
                    mycursor.execute(sql)
                    mydb.commit()
                    print(mycursor.rowcount, "record(s) deleted")
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                        "-1 to go back:\n")
                elif question == "sh":
                    if dades.player_seleccionado != {}:
                        showhPlayersGame()
                        print(dades.cabecera_menu0211)
                        showBBDDPlayer()
                        print(dades.asteriscos)
                        question = input(
                            "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                            "-1 to go back:\n")
                    else:
                        print(" " * 40 + "*******************ActualPlayersInGame*******************" + " " * 40)
                        print(" " * 55 + "There is no players in game" + " " * 55)
                        input(" " * 60 + "Enter to continue" + " " * 63)
                        print(dades.cabecera_menu0211)
                        showBBDDPlayer()
                        print(dades.asteriscos)
                        question = input(
                            "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                            "-1 to go back:\n")
                else:
                    print("===============================================================Invalid Option====="
                          "==========================================================")
                    input(" " * 58 + "Press enter to continue" + " " * 59)
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                        "-1 to go back:\n")
            else:
                print("===============================================================Invalid Option====="
                      "==========================================================")
                input(" " * 58 + "Press enter to continue" + " " * 59)
                print(dades.cabecera_menu0211)
                showBBDDPlayer()
                print(dades.asteriscos)
                question = input("Option (id to add to game, -id to remove player, sh to show actual players in game, "
                                 "-1 to go back:\n")
        else:
            menu02()
    else:

        showhPlayersGame()

        print(dades.cabecera_menu0211)

        dict_humanos = {}
        dict_robot = {}
        lista = ["g", "Catious", "Moderated", "Bold"]
        print(dades.cabecera_menu013)
        mycursor.execute("SELECT human, player_id, player_name, player_risk FROM player")
        myresult = mycursor.fetchall()
        for x in myresult:
            if x[0] == 0:
                dict_robot.update({x[1]: {"Name": x[2], "Profile": lista[x[3]]}})
            elif x[0] == 1:
                dict_humanos.update({x[1]: {"Name": x[2], "Profile": lista[x[3]]}})

        showBBDDPlayer()
        print(dades.asteriscos)
        question = input("Option (id to add to game, -id to remove player, sh to show actual players in game, "
                         "-1 to go back:\n")
        while question != "-1":
            if question not in dades.player_seleccionado:
                if question in dict_robot or question in dict_humanos:
                    lista = ["g", "Catious", "Moderated", "Bold"]
                    human = ["Human", "Boot"]
                    mycursor.execute("SELECT player_id, player_name, human, player_risk FROM player")

                    myresult = mycursor.fetchall()

                    for x in myresult:
                        if x[0] == question:
                            dades.player_seleccionado.update({x[0]: {"Name": x[1], "Human": human[x[2]], "Profile": lista[x[3]]}})

                    showhPlayersGame()
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input("Option (id to add to game, -id to remove player, sh to show actual players in game, "
                                     "-1 to go back:\n")
                elif question[0] == "-" and question[1:] in dict_robot or question[1:] in dict_humanos:
                    question = question[1:]
                    sql = f"DELETE FROM player WHERE player_id = '{question}'"
                    mycursor.execute(sql)
                    mydb.commit()
                    print(mycursor.rowcount, "record(s) deleted")
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                        "-1 to go back:\n")
                elif question == "sh":
                    showhPlayersGame()
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                        "-1 to go back:\n")
                else:
                    print("===============================================================Invalid Option====="
                          "==========================================================")
                    input(" " * 58 + "Press enter to continue" + " " * 59)
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                        "-1 to go back:\n")
            else:
                print("===============================================================Invalid Option====="
                      "==========================================================")
                input(" " * 58 + "Press enter to continue" + " " * 59)
                print(dades.cabecera_menu0211)
                showBBDDPlayer()
                print(dades.asteriscos)
                question = input("Option (id to add to game, -id to remove player, sh to show actual players in game, "
                                 "-1 to go back:\n")
        else:
            menu02()

def menu022():
    print(dades.cabecera_menu022)
    print("1) ESP - ESP\n2) POK - POK\n0) Go back")
    opc = input("Option: ")

    if opc.isdigit():
        opc = int(opc)
        if opc == 1:
            print("Established Card Deck ESP, Baraja Española")
            input("Enter to continue " + " " * 59)
            dades.mazo = "española"
            menu02()
        elif opc == 2:
            print("Established Card Deck POK, Poker Deck")
            input("Enter to continue " + " " * 59)
            dades.mazo = "poker"
            menu02()
        elif opc == 0:
            print("Established Card Deck POK, Poker Deck")
            input("Enter to continue " + " " * 59)
            dades.mazo = "poker"
            menu02()
        else:
            print("===============================================================Invalid Option====="
                  "==========================================================")
            input(" " * 58 + "Press enter to continue" + " " * 59)
            menu022()
    else:
        print("===============================================================Invalid Option====="
              "==========================================================")
        input(" " * 58 + "Press enter to continue" + " " * 59)
        menu022()

def menu023():
    print(dades.cabecera_menu023)
    rondas = input("Max Rounds :")

    if rondas.isdigit():
        rondas = int(rondas)

        if rondas > 20:
            print("Max Rounds Has To Be Between 0 and 20")
            input("Enter to continue ")
            menu023()
        else:
            print(f"Established maximum of rounds to {rondas}")
            dades.max_rondas = rondas
            input("Enter to continue ")
            menu02()
    else:
        print("Please, enter only numbers")
        input("Enter to continue ")
        menu023()

# Menú 3

def menu03():
    print("El juego")

    if dades.player_seleccionado == {}:
        print("Set the players that compose the game first")
        input("Enter to continue ")
        menu00()
    elif len(dades.player_seleccionado) < 2:
        print("Set the players that compose the game first")
        input("Enter to continue ")
        menu00()
    else:
        if dades.mazo == "":
            print("Set the deck of cards first")
            input("Enter to continue ")
            menu00()
        elif dades.max_rondas == 0:
            print("Set the max rounds of the game first")
            input("Enter to continue ")
            menu00()
        else:
            print(dades.cabecera_menu03)
            print("1)View Stats\n2)View Game Stats\n3)Set Bet\n4)Order Card\n5)Automatic Play\n6)Stand")
            input("Option: ")

# Menú 4

def menu04():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu04)
        textOpts = "1)Players With More Earnings\n2)Players With More Games Played\n3)Players With More Minutes Played"\
                   "\nS)Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3]
        exceptions = ["S"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu041()
        elif opc == 2:
            menu042()
        elif opc == 3:
            menu043()
        elif opc == "S":
            dejar_este_nivel = True

# Opciones del menú 4

def menu041():
    print("aquí va el ejercicio")
def menu042():
    print("aquí va el ejercicio")
def menu043():
    print("aquí va el ejercicio")

def menu05():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu05)
        textOpts = "1) Initial card more repeated by each user,\nonly users who have played a minium of 3 games.\n2) " \
                   "Player who makes the highest bet per game,\nfind the round with the highest bet\n3) " \
                   "Player who makes the lowest bet per game.\n4) Percentage of rounds won per player in each game\n" \
                   "(%), as well as their average bet for the game.\n5) List of games won by Bots.\n6) Rounds won by the" \
                   " bank in each game.\n7) Number of users have been the bank in each game.\n8) Average bet per game" \
                   "\n9) Average bet of the first round of each game.\n10) Average bet of the last round of each game.\n" \
                   "S) Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        exceptions = ["S"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu051()
        elif opc == 2:
            menu052()
        elif opc == 3:
            menu053()
        elif opc == 4:
            menu054()
        elif opc == 5:
            menu055()
        elif opc == 6:
            menu056()
        elif opc == 7:
            menu057()
        elif opc == 8:
            menu058()
        elif opc == 9:
            menu059()
        elif opc == 10:
            menu0510()
        elif opc == "S":
            dejar_este_nivel = True

# Opciones del menú 5

def menu051():
    print("aquí va el ejercicio")
def menu052():
    print("aquí va el ejercicio")
def menu053():
    print("aquí va el ejercicio")
def menu054():
    print("aquí va el ejercicio")
def menu055():
    print("aquí va el ejercicio")
def menu056():
    print("aquí va el ejercicio")
def menu057():
    print("aquí va el ejercicio")
def menu058():
    print("aquí va el ejercicio")
def menu059():
    print("aquí va el ejercicio")
def menu0510():
    print("aquí va el ejercicio")

# Programa

