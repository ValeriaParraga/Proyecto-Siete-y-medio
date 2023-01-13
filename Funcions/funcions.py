from random import randint

import dades as dades

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
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
        exceptions = ["S"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            while opc == 1:
                menu01()
        elif opc == 2:
            menu02()
        elif opc == 3:
            menu03()
        elif opc == 4:
            menu04()
        elif opc == 5:
            menu05()
        elif opc == "S":
            dejar_este_nivel = True


# Menú 1

def menu01():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu01)
        textOpts = "1)New Human Player\n2)New Bot\n3)Show/Remove Players\nS)Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3]
        exceptions = ["S"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu011()
        elif opc == 2:
            menu012()
        elif opc == 3:
            menu013()
        elif opc == "S":
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


def menu012():
    nameOK = False
    typeofplayerOK = False
    try:
        name = input("Name: ")
        if name.isalnum():
            nameOK = True
        else:
            raise ValueError("Incorrect name, please, enter a name not empty with only letters")

        NUMBER_DNI = randint(10000000, 99999999)
        LETTER_DNI = dades.DNILetras[NUMBER_DNI % 23]
        nif_bot = str(NUMBER_DNI) + str(LETTER_DNI)
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


def menu013():
    print(dades.cabecera_menu013)
    mycursor.execute("SELECT player_id, player_name, player_risk FROM player")
    myresult = mycursor.fetchall()
    for x in myresult:
        for i in x:
            print(x)


# Menú 2

def menu02():
    dejar_este_nivel = False
    while not dejar_este_nivel:
        print(dades.cabecera_menu02)
        textOpts = "1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\nS)Go back"
        inputOptText = "Option: "
        lista = [1, 2, 3]
        exceptions = ["S"]
        opc = getOpt(textOpts, inputOptText, lista, exceptions)
        if opc == 1:
            menu021()
        elif opc == 2:
            menu022()
        elif opc == 3:
            menu023()
        elif opc == "S":
            dejar_este_nivel = True

# Opciones del menú 2

def menu021():
    print("aquí va el ejercicio")
def menu022():
    print("aquí va el ejercicio")
def menu023():
    print("aquí va el ejercicio")

# Menú 3

def menu03():
    print("El juego")


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

menu00()