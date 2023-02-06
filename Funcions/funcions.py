# Imports
import math
import random
from datetime import datetime as dt
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


# Funciones del menú 1

# Función para añadir a todos los jugadores que se encuentran en la BBDD en el diccionario Players
def dict_players():
    mycursor.execute("SELECT player_id, player_name, human, player_risk FROM player")
    myresult = mycursor.fetchall()
    lista = [0, 30, 40, 50]
    lista1 = [False, True]
    for x in myresult:
        dades.players[x[0]] = {"name": x[1], "human": lista1[x[2]], "bank": False, "initialCard": "", "priority": 0,
                               "type": lista[x[3]], "bet": 0, "points": 0, "cards": [], "roundPoints": 0}


# Función que ejecuta el menu011
def menu011():
    print(dades.cabecera_menu011)
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
                dict_players()
                return
            else:
                return
        else:
            print("There's an error")
    except ValueError as e:
        print(e)
        input("Enter to Continue ")


# Función que devuelve un dni aleatorio para un boot
def newRandomDNI():
    NUMBER_DNI = randint(10000000, 99999999)
    LETTER_DNI = dades.DNILetras[NUMBER_DNI % 23]
    nif_bot = str(NUMBER_DNI) + str(LETTER_DNI)
    return nif_bot


# Función que ejecuta el menú012
def menu012():
    print(dades.cabecera_menu012)
    nameOK = False
    typeofplayerOK = False
    try:
        name = input("Name: ")
        if name.isalnum():
            nameOK = True
        else:
            raise ValueError("Incorrect name, please, enter a name not empty with only letters")

        nif_bot = newRandomDNI()
        mycursor.execute("SELECT player_id FROM player")
        myresult = mycursor.fetchall()
        for x in myresult:
            if nif_bot == x:
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
                dict_players()
                return
            else:
                return
        else:
            print("There's an error")
    except ValueError as e:
        print(e)
        input("Enter to Continue ")
        return


# Función para eliminar a un jugador de la BBDD
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
        return
    else:
        print("===============================================================Invalid Option====="
              "==========================================================")
        input(" " * 58 + "Press enter to continue" + " " * 59)
        return


# Función para ejecutar el menú013
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


# Función que muestra los jugadores que hay en la BBDD
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

# Función que muestra los jugadores actuales seleccionados para jugar
def showhPlayersGame():
    print(" " * 40 + "*******************ActualPlayersInGame*******************" + " " * 40)
    cadena = str()
    for i in dades.player_seleccionado:
        cadena = cadena + (' ' * 50 + str(i) + '    ' + dades.player_seleccionado[i].get("Name") + '  ' +
                           dades.player_seleccionado[i].get("Human") +
                           '   ' + dades.player_seleccionado[i].get("Profile") + '\n')
    print(cadena)

    input(" " * 58 + "Press enter to continue" + " " * 59)


# Función que ejecuta el menú021
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
            if question not in dades.player_seleccionado and len(dades.player_seleccionado) <= 5:
                if question in dict_robot or question in dict_humanos:
                    lista = ["g", "Catious", "Moderated", "Bold"]
                    human = ["Boot", "Human"]
                    mycursor.execute("SELECT player_id, player_name, human, player_risk FROM player")

                    myresult = mycursor.fetchall()

                    for x in myresult:
                        if x[0] == question:
                            dades.game.append(x[0])
                            dades.player_seleccionado.update(
                                {x[0]: {"Name": x[1], "Human": human[x[2]], "Profile": lista[x[3]]}})

                    showhPlayersGame()
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
                        "-1 to go back:\n")
                elif question == "" or question.isspace():
                    print("===============================================================Invalid Option====="
                          "==========================================================")
                    input(" " * 58 + "Press enter to continue" + " " * 59)
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
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
                if len(dades.player_seleccionado) > 5 and question not in dades.player_seleccionado:
                    print("Maxim number of players in game reached!!")
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
            return
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
            if question not in dades.player_seleccionado and len(dades.player_seleccionado) <= 5:
                if question in dict_robot or question in dict_humanos:
                    lista = ["g", "Catious", "Moderated", "Bold"]
                    human = ["Boot", "Human"]
                    mycursor.execute("SELECT player_id, player_name, human, player_risk FROM player")

                    myresult = mycursor.fetchall()

                    for x in myresult:
                        if x[0] == question:
                            dades.game.append(x[0])
                            dades.player_seleccionado.update(
                                {x[0]: {"Name": x[1], "Human": human[x[2]], "Profile": lista[x[3]]}})

                    showhPlayersGame()
                    print(dades.cabecera_menu0211)
                    showBBDDPlayer()
                    print(dades.asteriscos)
                    question = input(
                        "Option (id to add to game, -id to remove player, sh to show actual players in game, "
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
                if len(dades.player_seleccionado) > 6 and question not in dades.player_seleccionado:
                    print("Maxim number of players in game reached!!")
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
            return


# Función que ejecuta el menú022
def menu022():
    print(dades.cabecera_menu022)
    print("1) ESP - ESP\n2) POK - POK\n0) Go back")
    opc = input("Option: ")

    if opc.isdigit():
        opc = int(opc)
        if opc == 1:
            print("Established Card Deck ESP, Baraja Española")
            input("Enter to continue " + " " * 59)
            dades.context_game["mazo"] = "española"
            return
        elif opc == 2:
            print("Established Card Deck POK, Poker Deck")
            input("Enter to continue " + " " * 59)
            dades.context_game["mazo"] = "poker"
            return
        elif opc == 0:
            print("Established Card Deck ESP, Baraja Española")
            input("Enter to continue " + " " * 59)
            dades.context_game["mazo"] = "española"
            return
        else:
            print("===============================================================Invalid Option====="
                  "==========================================================")
            input(" " * 58 + "Press enter to continue" + " " * 59)
    else:
        print("===============================================================Invalid Option====="
              "==========================================================")
        input(" " * 58 + "Press enter to continue" + " " * 59)


# Función que ejecuta el menú023
def menu023():
    print(dades.cabecera_menu023)
    rondas = input("Max Rounds :")

    if rondas.isdigit():
        rondas = int(rondas)

        if rondas > 20:
            print("Max Rounds Has To Be Between 0 and 20")
            input("Enter to continue ")
        else:
            print(f"Established maximum of rounds to {rondas}")
            dades.context_game["maxRounds"] = rondas
            input("Enter to continue ")
            return
    else:
        print("Please, enter only numbers")
        input("Enter to continue ")

# Función que mezcla la lista con los id's de las cartas. Devuelve barajada las cartas.
def mezclar_lista(mazo):
    lista = mazo[:]
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        indice_aleatorio = random.randint(0, longitud_lista - 1)
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
    return lista

# Función que establece las apuestas de cada jugador según su perfil al inicio de la partida
def setBets():
    for i in dades.players:
        if i in dades.game:
            apuesta = (dades.players[i]["points"] * dades.players[i]["type"] / 100)
            dades.players[i]["bet"] = math.ceil(apuesta)

# Función que limpia las cartas para una nueva ronda
def clearCards():
    for i in dades.game:
        dades.players[i]["cards"].clear()

# Función que calcula si pide una carta la banca
def bankOrderNewCard(ident,isbank):
    if isbank is True:
        checkIfExeeds = 0
        for i in range(len(dades.playerPTS)-1):
            if dades.playerPTS[list(dades.playerPTS.keys())[i]]["roundPoints"] > 7.5:
                checkIfExeeds += 1
        if checkIfExeeds == len(dades.playerPTS.keys())-1:
            pickCard(ident, dades.baraja)
            return
        while calculateRisk(ident) <= dades.players[ident]['type']:
            if dades.players[ident]["roundPoints"] < 7.5:
                pickCard(ident, dades.baraja)
            else:
                return

# Función que calcula el riesgo de pasarse de 7.5 puntos para los bots
def calculateRisk(ident):
    rest = 0
    r = 0
    if dades.context_game["mazo"] == "española":
        d = dades.cartas_espanyola.copy()
    elif dades.context_game["mazo"] == "poker":
        d = dades.cartas_poker.copy()
    for i in dades.cartas_totales:
        if i in dades.players[ident]["cards"] and i not in dades.cartas_totales:
            r += d[i]["realValue"]
        else:
            pass
        try:
            d.pop(i)
        except Exception:
            pass
    ac = 0
    for i in d.keys():
        # print(i)
        card_that_exeeds = r
        card_that_exeeds += d[i]["realValue"]
        # print(valor)
        if card_that_exeeds > 7.5:
            ac = ac + 1
            rest = rest + 1
        else:
            rest += 1
    try:
        risk = ac / rest * 100
        return risk
    except Exception:
        print("out of cards")
        risk = 0
        return risk

# Función que reparte una carta a un humano que la pide
def pickCard(ident,mazo):

    if dades.players[ident].get("human") is True and dades.automatic is False:
        eCard = mazo.pop()
        dades.cartas_totales.append(eCard)
        dades.players[ident]["cards"].append(eCard)
        pts = 0
        for card in dades.players[ident].get("cards"):
            if dades.context_game["mazo"] == "española":
                pts += dades.cartas_espanyola[card].get("realValue")
            elif dades.context_game["mazo"] == "poker":
                pts += dades.cartas_poker[card].get("realValue")
        print("\nOrder card")
        if dades.context_game["mazo"] == "española":
            print(f"The new card is {dades.cartas_espanyola[eCard].get('literal')}")
        elif dades.context_game["mazo"] == "poker":
            print(f"The new card is {dades.cartas_poker[eCard].get('literal')}")
        print("now you have", pts, "points")
        dades.players[ident]["roundPoints"] = pts
        input("\nEnter to continue: ")
        return
    elif dades.players[ident]["human"] is False or (dades.players[ident]["human"] is True and dades.automatic is True):
        eCard = mazo.pop()
        dades.cartas_totales.append(eCard)
        dades.players[ident]["cards"].append(eCard)
        pts = 0
        for card in dades.players[ident].get("cards"):
            if dades.context_game["mazo"] == "española":
                pts += dades.cartas_espanyola[card].get("realValue")
            elif dades.context_game["mazo"] == "poker":
                pts += dades.cartas_poker[card].get("realValue")
        dades.players[ident]["roundPoints"] = pts
        return

# Función que calcula las probabilidades de pasar los 7.5 puntos al escoger una nueva carta si ya tiene otras
def standarRound(ident, mazo):
    cards_guard = dades.players[ident].get("cards")
    if dades.players[ident].get('human') is True and dades.automatic is False:
        if len(cards_guard) > 0:
            if dades.players[ident]["roundPoints"] < 7.5:
                print("Chance of exceed", calculateRisk(ident),"%")
                sure = input("Are You sure do you want to order another card? Y/y = yes another key = not: ")
                if sure == "y" or sure == "Y":
                    pickCard(ident, mazo)
                else:
                    return
            else:
                print("you have exceeded 7.5 points! You're not allowed to order another card")
                return
        else:
            pickCard(ident, mazo)

    elif dades.players[ident].get('human') is True and dades.automatic is True:
        while calculateRisk(ident) < dades.players[ident]['type']:
            if dades.players[ident]["roundPoints"] < 7.5:
                pickCard(ident, mazo)
            else:
                return
        return
    elif dades.players[ident].get("human") is False:
        while calculateRisk(ident) < dades.players[ident]['type']:
            if dades.players[ident]["roundPoints"] < 7.5:
                pickCard(ident, mazo)
            else:
                return
        return

# Función que muestra los stats de un jugador humano
def printPlayerStats(id):
    print(dades.cabecera_menu03)
    print("*" * 60 + f"Round {dades.context_game['round']}, Turn of {dades.players[id]['name']}" + "*" * 60)
    print(f"name           {dades.players[id]['name']}\ntype           {dades.players[id]['type']}\n"
          f"human          {dades.players[id]['human']}\n"
          f"bank           {dades.players[id]['bank']}\ninitialCard    {dades.players[id]['initialCard']}\n"
          f"priority       {dades.players[id]['priority']}\nbet            {dades.players[id]['bet']}\n"
          f"points         {dades.players[id]['points']}")
    print(f"cards          {printCards(id)}\nroundPoints", end='    ')
    print(f"{dades.players[id]['roundPoints']}")

    return
def printCards(ident):
    linea = ''
    for i in dades.players[ident]['cards']:
        linea += i + " "
    return linea
# Función que imprime los stats de todos los jugadores de la partida
def printStats(titulo=""):
    if dades.print_resultado_ronda == 'no':
        print(dades.cabecera_menu03)
        print(titulo)
    posicion = 0
    print("Name".ljust(11), end='   ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['name']}".ljust(30), end='        ')
    posicion = 0
    print("\n""Human".ljust(11), end='    ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['human']}".ljust(30), end='        ')
    posicion = 0
    print("\n""Priority".ljust(11), end='    ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['priority']}".ljust(30), end='        ')
    posicion = 0
    print("\n""Bank".ljust(11), end='    ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['bank']}".ljust(30), end='        ')
    posicion = 0
    print("\n""Bet".ljust(11), end='    ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['bet']}".ljust(30), end='        ')
    posicion = 0
    print("\n""Points".ljust(11), end='    ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['points']}".ljust(30), end='        ')
    posicion = 0
    print("\n""Cards".ljust(11), end='    ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{printCards(id)}".ljust(30), end='        ')
    posicion = 0
    print("\n""Roundpoints".ljust(11), end='   ')
    for id in dades.game:
        posicion = posicion + 1
        if posicion < 4:
            print(f"{dades.players[id]['roundPoints']}".ljust(30), end='        ')

    if len(dades.game) >= 4:
        print('\n' + "-" * 141)
        posicion = 0
        print("Name".ljust(11), end='   ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['name']}".ljust(30), end='        ')
        posicion = 0
        print("\n""Human".ljust(11), end='    ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['human']}".ljust(30), end='        ')
        posicion = 0
        print("\n""Priority".ljust(11), end='    ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['priority']}".ljust(30), end='        ')
        posicion = 0
        print("\n""Bank".ljust(11), end='    ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['bank']}".ljust(30), end='        ')
        posicion = 0
        print("\n""Bet".ljust(11), end='    ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['bet']}".ljust(30), end='        ')
        posicion = 0
        print("\n""Points".ljust(11), end='    ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['points']}".ljust(30), end='        ')
        posicion = 0
        print("\n""Cards".ljust(11), end='    ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{printCards(id)}".ljust(30), end='        ')
        posicion = 0
        print("\n""Roundpoints".ljust(11), end='   ')
        for id in dades.game:
            posicion = posicion + 1
            if posicion >= 4:
                print(f"{dades.players[id]['roundPoints']}".ljust(30), end='        ')

    input("\nEnter to continue")
    return

# Función que gestiona la tirada de un jugador humano. Muestra el menú de opciones
def humanRound(id, mazo):
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu03)
        print("*" * 60 + f"Round {dades.context_game['round']}, Turn of {dades.players[id]['name']}" + "*" * 60)
        textOpts = "\n1)View Stats\n2)View Game Stats\n3)Set Bet\n4)Order Card\n5)Automatic Play\nS)Stand"
        inputOptText = "Option: "
        lista = [1, 2, 3, 4, 5]
        exceptions = ["S", "s"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            printPlayerStats(id)
            input("Enter to continue ")
        elif opc == 2:
            printStats(titulo="*" * 60 + f"Round {dades.context_game['round']}, "
                                         f"Turn of {dades.players[id]['name']}" + "*" * 60)
        elif opc == 3:
            if dades.players[id]["bank"] is True:
                print("You're not allowed to change the bet if you're de bank")
                input("Enter to Continue ")
            else:
                correct = False
                while correct is False:
                    bet = input("Set the new Bet: ")
                    if bet.isdigit():
                        bet = int(bet)
                        if bet > 0 and bet <= dades.players[id]["points"]:
                            correct = True
                            dades.players[id].update({"bet": bet})
                            input("Enter to continue ")
                        else:
                            print(f"Please, introduce only numbers between 1 and {dades.players[id]['points']}")
                    else:
                        if not bet.isdigit():
                            print("Please, introduce only numbers")
        elif opc == 4:
            standarRound(id, dades.baraja)
        elif opc == 5:
            dades.automatic = True
            standarRound(id, dades.baraja)
            printStats(titulo="*" * 60 + f"Round {dades.context_game['round']}, "
                                         f"Turn of {dades.players[id]['name']}" + "*" * 60)
            return
        elif opc in exceptions:
            dejar_este_nivel = True


# Función principal del proyecto
def playGame():
    # Se conoce la baraja con la que se va a jugar y se llama a la función que establece la prioridad de cada jugador
    if dades.context_game["mazo"] == "española":
        dades.deck = 1
        dades.baraja = mezclar_lista(dades.mazo_espanyola)
        setGamePriority(dades.baraja)
    elif dades.context_game["mazo"] == "poker":
        dades.deck = 2
        dades.baraja = mezclar_lista(dades.mazo_poker)
        setGamePriority(dades.baraja)

    # Creamos variables que se insertarán al final de la partida en el diccionario cardgame
    dades.num_jugadores = len(dades.game)
    tiempo_actual = actual_hour()
    dades.rounds = dades.context_game["maxRounds"]


    # mycursor.execute("SELECT cardgame_id, players from cardgame")
    # myresult = mycursor.fetchall()
    # for i in myresult:
    #     cardgame_id = i[0]
    #     print(i)
    #     cardgame = {"cardgame_id": cardgame_id, "players": num_jugadores, "start_hour": tiempo_actual,
    #             "rounds": i[1], "end_hour": tiempo_final}
    #
    # # Creamos e insertamos datos de la partida en el diccionario player_game
    #
    # for i in dades.game:
    #     dades.player_game[myresult] = {i: {"initial_card_id": dades.players[i]["initialCard"],
    #                                              "starting_points": dades.players[i]["points"], "ending_points": 0}}
    #
    # print(dades.player_game)
    #
    # # Creamos e insertamos datos de la partida en el diccionario player_game_round
    #
    # for i in dades.players:
    #     if i in dades.game:
    #         if dades.players[i]["bank"] is True:
    #             dades.player_game_round[dades.context_game["round"]] = \
    #                     {i: {"is_bank": 1, "bet_points": "apuesta en la ronda",
    #                          "starting_round points": dades.players[i]["points"],
    #                          "cars_value": "puntos obtenidos en la actual ronda",
    #                          "ending_round_points": "puntos al final de la ronda"}}
    #         else:
    #             dades.player_game_round[dades.context_game["round"]] = \
    #                 {i: {"is_bank": 0, "bet_points": "apuesta en la ronda",
    #                      "starting_round points": dades.players[i]["points"],
    #                      "cars_value": "puntos obtenidos en la actual ronda",
    #                      "ending_round_points": "puntos al final de la ronda"}}
    #
    # print(dades.player_game_round)

    # Se llama a la función que resetea los puntos de cada jugador a 20
    resetPoints()
    # Se establecen las apuestas según el perfil de cada jugador


    # La partida comienza mientras haya mínimo dos jugadores y no se superen las rondas máximas
    while checkMinimun2PlayerWithPoints() is True and dades.context_game["round"] <= dades.context_game["maxRounds"]:
        dades.print_resultado_ronda = 'no'
        # Empiezan a jugar según prioridad
        for i in dades.game:
            setBets()
            if dades.context_game["mazo"] == "española":
                dades.baraja = mezclar_lista(dades.mazo_espanyola)
            elif dades.context_game["mazo"] == "poker":
                dades.baraja = mezclar_lista(dades.mazo_poker)
            dades.nif_starting_points.update({i:dades.players[i]["points"]})
            if dades.players[i]['human'] is True:
                humanRound(i, dades.baraja)
            elif dades.players[i]['human'] is False and dades.players[i]['bank'] is False:
                standarRound(i, dades.baraja)
                printStats(titulo="*" * 60 + f"Round {dades.context_game['round']}, "
                                             f"Turn of {dades.players[i]['name']}" + "*" * 60)
            elif dades.players[i]['human'] is False and dades.players[i]['bank'] is True:
                bankOrderNewCard(i, dades.players[i]['bank'])
                printStats(titulo="*" * 60 + f"Round {dades.context_game['round']}, "
                                             f"Turn of {dades.players[i]['name']}" + "*" * 60)

            dades.playerPTS.update({i: {"roundPoints": dades.players[i]["roundPoints"], "bet": dades.players[i]["bet"]}})

        # Sumamos las rondas finalizadas
        dades.context_game["round"] = dades.context_game["round"] + 1

        # Repartimos puntos, eliminamos jugadores si se quedan sin puntos y ordenamos prioridades si hay nueva banca

        list_players_con_posibilidad = []
        suma_bets_bank = 0
        empate = []
        resta_bets_posibilidades = 0
        apuesta_empate = 0
        for i in dades.game:
            if dades.players[i]['bank'] is False:
                if dades.players[i]['roundPoints'] > 7.5:
                    suma_bets_bank = suma_bets_bank + dades.players[i]['bet']
                    new_points = (dades.players[i]['points'] - dades.players[i]['bet'])
                    dades.players[i]['points'] = new_points
                    if dades.players[i]['points'] == 0:
                        dades.game.remove(i)
                elif 7.5 > dades.players[i]['roundPoints'] > 0:
                    list_players_con_posibilidad.append(i)
                    resta_bets_posibilidades += dades.players[i]['bet']
                elif dades.players[i]['roundPoints'] == 7.5:
                    empate.append(i)
                    list_players_con_posibilidad.append(i)
                    apuesta_empate = suma_bets_bank + dades.players[i]['bet']
            elif dades.players[i]['bank'] is True:
                if dades.players[i]['roundPoints'] > 7.5:
                    pts_lost = (dades.players[i]['points'] - resta_bets_posibilidades)
                    dades.players[i]['points'] = pts_lost
                    if empate != []:
                        players_bank = new_bank(empate)
                        dades.players[players_bank]['points'] += (dades.players[players_bank]['bet'] * 2)
                        dades.players[players_bank]['bank'] = True
                        dades.players[i]['bank'] = False
                        dades.players[players_bank]['priority'], dades.players[i]['priority'] = dades.players[i][
                                                                                                    'priority'], \
                                                                                                dades.players[
                                                                                                    players_bank][
                                                                                                    'priority']
                    if dades.players[i]['points'] == 0:
                        player_bank = new_bank(list_players_con_posibilidad)
                        dades.players[player_bank]['bank'] = True
                        dades.players[player_bank]['priority'] = dades.players[i]['priority']
                        dades.game.remove(i)
                    for j in list_players_con_posibilidad:
                        suma = dades.players[j]['bet'] + dades.players[j]['points']
                        dades.players[j]['points'] = suma
                elif list_players_con_posibilidad == []:
                    dades.players[i]['points'] += suma_bets_bank
                elif 7.5 > dades.players[i]['roundPoints'] > 0:
                    player_posible_bank = new_bank_2(list_players_con_posibilidad)
                    if dades.players[i]['roundPoints'] > dades.players[player_posible_bank]['roundPoints']:
                        dades.players[i]['points'] += dades.players[player_posible_bank]['bet'] + suma_bets_bank
                        nuevos_points = (dades.players[player_posible_bank]['points'] -
                                         dades.players[player_posible_bank]['bet'])
                        dades.players[player_posible_bank]['points'] = nuevos_points
                    elif dades.players[i]['roundPoints'] < dades.players[player_posible_bank]['roundPoints']:
                        if dades.players[player_posible_bank]['roundPoints'] == 7.5:
                            dades.players[player_posible_bank]['bank'] = True
                            dades.players[i]['bank'] = False
                            dades.players[player_posible_bank]['priority'], dades.players[i]['priority'] = \
                                dades.players[i]['priority'], dades.players[player_posible_bank]['priority']
                            dades.players[player_posible_bank]['points'] += dades.players[player_posible_bank]['bet']
                            pts_lost = (dades.players[i]['points'] - resta_bets_posibilidades)
                            dades.players[i]['points'] = pts_lost
                        else:
                            dades.players[player_posible_bank]['points'] += dades.players[player_posible_bank]['bet']
                            pts_lost = (dades.players[i]['points'] - resta_bets_posibilidades)
                            dades.players[i]['points'] = pts_lost
                elif empate != [] and dades.players[i]['roundPoints'] == 7.5:
                    dades.players[i]['points'] += apuesta_empate
                    apuesta_empate = 0
        for i in dades.player_seleccionado:
            dades.player_game_round.update({i: {}})
            for j in range(dades.context_game["round"]):
                if dades.players[i]["bank"] is True:
                    dades.player_game_round[i].update({j:{"is_bank": 1, "bet_points":dades.players[i]['bet'],
                                                          "cards_value":dades.players[i]["roundPoints"],
                                                          "starting_round_points":dades.nif_starting_points[i],
                                                          "ending_round_points":dades.players[i]["roundPoints"]}})
                elif dades.players[i]["bank"] is False:
                    dades.player_game_round[i].update({j: {"is_bank": 0, "bet_points": dades.players[i]['bet'],
                                                           "cards_value": dades.players[i]["roundPoints"],
                                                           "starting_round_points": dades.nif_starting_points[i],
                                                           "ending_round_points": dades.players[i]["roundPoints"]}})
        cab1 = f"***********************************************************  STATS AFTER ROUND {dades.context_game['round']-1} **********" \
               f"*************************************************\n"
        print(cab1)
        print(dades.cabecera_menu03resultado)
        dades.print_resultado_ronda = 'yes'
        printStats()
        clearCards()
        answer = input("Enter to continue to new Round, exit to leave game:")
        if answer == 'exit' or answer == 'EXIT':
            print(dades.menu03game_over)
            ganador = winner(dades.game)
            print(f"The winner is {ganador} - {dades.players[ganador]['name']}, in {dades.context_game['round']-1} rounds,  "
                f"with {dades.players[ganador]['points']} points")
            tiempo_final = actual_hour()
            insertBBDDcardgame(players=dades.num_jugadores, rounds=dades.rounds, start_hour=tiempo_actual,
                               end_hour=tiempo_final, deck_id=dades.deck)
            # Se hace un clear de todos los campos que se llenan en la partida de los jugadores menos NIF, nombre y type
            for i in dades.game:
                dades.players[i]["cards"] = ''
                dades.players[i]["bank"] = False
                dades.players[i]["initialCard"] = ''
                dades.players[i]["priority"] = 0
                dades.players[i]["bet"] = 0
                dades.players[i]["points"] = 0
                dades.players[i]["roundPoints"] = 0

            input("Enter to continue ")
            return
        for i in dades.game:
            dades.players[i]["roundPoints"] = 0
    else:
        print(dades.menu03game_over)
        ganador = winner(dades.game)
        print(f"The winner is {ganador} - {dades.players[ganador]['name']}, in {dades.context_game['round']-1} rounds,  "
              f"with {dades.players[ganador]['points']} points")

        # Insertamos datos en los diccionarios
        tiempo_final = actual_hour()
        insertBBDDcardgame(players=dades.num_jugadores, rounds=dades.rounds, start_hour=tiempo_actual,
                           end_hour=tiempo_final, deck_id=dades.deck)
        # Se hace un clear de todos los campos que se llenan en la partida de los jugadores menos NIF, nombre y type
        for i in dades.game:
            dades.players[i]["cards"] = ''
            dades.players[i]["bank"] = False
            dades.players[i]["initialCard"] = ''
            dades.players[i]["priority"] = 0
            dades.players[i]["bet"] = 0
            dades.players[i]["points"] = 0
            dades.players[i]["roundPoints"] = 0

        input("Enter to continue\n ")
        return
def winner(lista):
    maximo = 0
    ganador = ''
    for i in lista:
        if dades.players[i]['points'] > maximo:
            maximo = dades.players[i]['points']
            ganador = i
    return ganador
def new_bank(lista):
    maximo = 0
    persona = ''
    for i in lista:
        if dades.players[i]['priority'] > maximo:
            maximo = dades.players[i]['priority']
            persona = i
    return persona

def new_bank_2(lista):
    maximo = 0
    pers = ''
    for i in lista:
        if dades.players[i]['roundPoints'] > maximo:
            maximo = dades.players[i]['roundPoints']
            pers = i
    return pers

# Función que resetea los puntos a 20 al inicio de la partida
def resetPoints():
    for i in dades.game:
        dades.players[i]["points"] = 20

# Función que ejecuta el menú03
def menu03():
    while dades.game != [] and not len(dades.game) < 2 and dades.context_game["mazo"] != " ":
        playGame()
        return
    else:
        if dades.game == []:
            print("Set the players that compose the game first")
            input("Enter to continue ")
            return
        elif len(dades.player_seleccionado) < 2:
            print("Set the players that compose the game first")
            input("Enter to continue ")
            return
        elif dades.context_game["mazo"] == " ":
            print("Set the deck of cards first")
            input("Enter to continue ")
            return

# Función que comprueba que mínimo hayan dos personas con puntos para que continue el juego
def checkMinimun2PlayerWithPoints():
    min = 0
    for i in dades.players:
        if i in dades.game:
            if dades.players[i]["points"] > 0:
                min += 1
    if min >= 2:
        return True
    else:
        return False

# Función que establece la prioridad de jugar según la carta
def setGamePriority(mazo):
    dict_players()
    cartas_iniciales = 0
    for i in dades.players:
        if i in dades.game:
            dades.players[i].update({"initialCard": mazo[cartas_iniciales]})
            cartas_iniciales += 1

    baraja = dades.context_game["mazo"]

    dict_primera_carta = {}

    if baraja == "española":
        for i in dades.players:
            if i in dades.game:
                carta_guardada = dades.players[i].get("initialCard")
                for j in dades.cartas_espanyola:
                    if carta_guardada == j:
                        dict_primera_carta.update({i: (dades.cartas_espanyola[j].get("value") * 10 +
                                                       dades.cartas_espanyola[j].get("priority"))})

        o_dict_primera_carta = dict(sorted(dict_primera_carta.items(), key=lambda item: item[1]))

        n = 1
        for i in o_dict_primera_carta:
            o_dict_primera_carta[i] = n
            dades.players[i]["priority"] = n
            dades.game[n - 1] = i
            n = n + 1

        for i in dades.players:
            if i == dades.game[-1]:
                dades.players[i]["bank"] = True

    elif baraja == "poker":
        for i in dades.players:
            if i in dades.game:
                carta_guardada = dades.players[i].get("initialCard")
                for j in dades.cartas_poker:
                    if carta_guardada == j:
                        dict_primera_carta.update({i: (dades.cartas_poker[j].get("value") * 10 +
                                                       dades.cartas_poker[j].get("priority"))})

        o_dict_primera_carta = dict(sorted(dict_primera_carta.items(), key=lambda item: item[1]))

        n = 1
        for i in o_dict_primera_carta:
            o_dict_primera_carta[i] = n
            dades.players[i]["priority"] = n
            dades.game[n - 1] = i
            n = n + 1

        for i in dades.players:
            if i == dades.game[-1]:
                dades.players[i]["bank"] = True


def insertBBDDcardgame(players=0, rounds=0, start_hour="", end_hour="", deck_id=0):

    dades.cardgame = {players, rounds, start_hour, end_hour, deck_id}

    sql = "INSERT INTO cardgame (players, rounds, start_hour, end_hour, deck_id) VALUES (%s, %s, %s, %s, %s)"
    val = (players, rounds, start_hour, end_hour, deck_id)
    mycursor.execute(sql, val)
    mydb.commit()

    mycursor.execute(f"SELECT cardgame_id FROM cardgame WHERE start_hour like '{start_hour}'")
    dades.cardgame_id = mycursor.fetchall()
    for j in dades.cardgame_id:
        for i in dades.player_seleccionado:
            insertBBDDplayergame(j[0], i, dades.players[i]['initialCard'], 20, dades.players[i]['points'])
    for x in dades.cardgame_id:
        insertBBDDplayergameround(dades.player_game_round, x[0])

def insertBBDDplayergame(cardgame_id=0, idplayer='', initial_card_id='', starting_points=0, ending_points=0):

    sql = "INSERT INTO player_game (cardgame_id, player_id, initial_card_id, starting_points, ending_points) VALUES (%s, %s, %s, %s, %s)"
    val = (cardgame_id, idplayer, initial_card_id, starting_points, ending_points)
    mycursor.execute(sql, val)
    mydb.commit()

def insertBBDDplayergameround(dict, ident):
    for i in dict.keys():
        for j in dict[i]:
            sql = "INSERT INTO player_game_round (round_num, cardgame_id, player_id, is_bank, bet_points, card_value, starting_round_points,ending_round_points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (j, ident, i, dict[i][j]["is_bank"], dict[i][j]["bet_points"], dict[i][j]["cards_value"], dict[i][j]["starting_round_points"], dict[i][j]["ending_round_points"])
            mycursor.execute(sql, val)
            mydb.commit()
# Menú 4
def menu04():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu04)
        textOpts = "1)Players With More Earnings\n2)Players With More Games Played\n3)Players With More Minutes Played" \
                   "\nS)Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3]
        exceptions = ["S", "s"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu041()
        elif opc == 2:
            menu042()
        elif opc == 3:
            menu043()
        elif opc in exceptions:
            dejar_este_nivel = True


# Opciones del menú 4
def menu041():
    print(dades.cabecera_menu041)
    print('''************************************************************************
    \nPlayer ID                         Earnings  Games Played  Minutes Played
    \n************************************************************************''')
    mycursor.execute(
        "SELECT player_id, earningpoints, gamesplayed, minutesplayed FROM ranking ORDER BY earningpoints desc")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i[0].ljust(9) + str(i[1]).rjust(33) + str(i[2]).rjust(14) + str(i[3]).rjust(16))

    input("Enter to continue ")


def menu042():
    print(dades.cabecera_menu042)
    print('''************************************************************************
        \nPlayer ID                         Earnings  Games Played  Minutes Played
        \n************************************************************************''')
    mycursor.execute(
        "SELECT player_id, earningpoints, gamesplayed, minutesplayed FROM ranking ORDER BY gamesplayed desc")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i[0].ljust(9) + str(i[1]).rjust(33) + str(i[2]).rjust(14) + str(i[3]).rjust(16))
    input("Enter to continue ")

def menu043():
    print(dades.cabecera_menu043)
    print('''************************************************************************
           \nPlayer ID                         Earnings  Games Played  Minutes Played
           \n************************************************************************''')
    mycursor.execute(
        "SELECT player_id, earningpoints, gamesplayed, minutesplayed FROM ranking ORDER BY minutesplayed desc")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i[0].ljust(9) + str(i[1]).rjust(33) + str(i[2]).rjust(14) + str(i[3]).rjust(16))
    input("Enter to continue ")

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
        exceptions = ["S", "s"]
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
        elif opc in exceptions:
            dejar_este_nivel = True

# Función que devuelve la fecha , la hora, los minutos y segundos actuales
def actual_hour():
    time = dt.time(dt.now())
    date = dt.date(dt.now())
    tiempo = str(date) + ' ' + str(time.hour) + ':' + str(time.minute) + ':' + str(time.second)
    return tiempo

# Opciones del menú 5
def menu051():
    print("ejercicio")

def menu052():
    print(dades.cabecera_menu05)
    mycursor.execute("SELECT player_id, bet_points FROM sah.highest_bet")
    r = mycursor.fetchall()
    print("player whith highest bet".ljust(40), "bet_points")
    for x, y in r:
        print(str(x).ljust(40), y)
    input("\nEnter to continue")
def menu053():
    print(dades.cabecera_menu05)
    mycursor.execute("SELECT player_id, bet_points FROM sah.lowest_bet")
    r = mycursor.fetchall()
    print("player whith lowest bet".ljust(40), "bet_points")
    for x, y in r:
        print(str(x).ljust(40), y)
    input("\nEnter to continue")


def menu054():
    print("aquí va el ejercicio")


def menu055():
    print("aquí va el ejercicio")


def menu056():
    print("aquí va el ejercicio")


def menu057():
    print(dades.cabecera_menu05)
    mycursor.execute("SELECT cardgame_id, banks FROM sah.banks_in_game")
    r = mycursor.fetchall()
    print("player whith lowest bet".ljust(40), "bet_points")
    for x, y in r:
        print(str(x).ljust(40), y)
    input("\nEnter to continue")

def menu058():
    print(dades.cabecera_menu05)
    mycursor.execute("SELECT cardgame_id, bp FROM sah.avg_bet_per_game")
    r = mycursor.fetchall()
    print("player whith lowest bet".ljust(40), "bet_points")
    for x, y in r:
        print(str(x).ljust(40), y)
    input("\nEnter to continue")


def menu059():
    print(dades.cabecera_menu05)
    mycursor.execute("SELECT cardgame_id, abp FROM sah.avg_bets_1st_round")
    r = mycursor.fetchall()
    print("player whith lowest bet".ljust(40), "bet_points")
    for x, y in r:
        print(str(x).ljust(40), y)
    input("\nEnter to continue")


def menu0510():
    print("aquí va el ejercicio")
