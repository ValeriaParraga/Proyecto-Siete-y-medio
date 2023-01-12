

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="SAH"
)
DNILetras = ["T","R","W","A", "G", "M", "Y","F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
mycursor = mydb.cursor()
def menu01():          #----------------------------------ADD/REMOVE/SHOW PLAYER--------------------------------------
    printmenu01 = "1)New Human Player\n2)New Bot\n3)Show/Remove Players\n4)Go back"
    try:
        print("\n\n\n" + printmenu01)
        opc01 = input("Select an option: ")
        if opc01 == "1":  # Human player
            nameOK = False
            DNIOK = False
            typeofplayerOK = False
            name = input("Insert the name of the player: ")
            if name.isalnum():
                nameOK = True
            else:
                raise TypeError("Special character detected")
            DNI = input("Insert the DNI of the player: ")
            if len(DNI) == 8:
                letDNI = DNI[len(DNI)-1]
                numDNI = DNI[:len(DNI)-2]
            else:
                raise TypeError("DNI muy corto")
            if not DNI.isalnum() or len(DNI) != 9:
                raise TypeError("Not_valid_DNI")
            elif not DNI[0:7].isdigit():
                raise TypeError("Not_valid_DNI")
            elif len(DNI) != 9:
                raise TypeError("Incorrect_DNI_length")
            elif DNILetras[(int(DNI[0:7]) % 23)] == DNI[8:]:
                raise TypeError("Incorrect_word")
            else:
                DNIOK = True
            typeofplayer = input("select the type of player:\n1)Beginner\n2)Intermediate\n3)Advanced\n>")
            if typeofplayer != "1" and typeofplayer != "2" and typeofplayer != "3":
                raise TypeError("not_valid_digit")
            else:
                typeofplayerOK =True
                typeofplayer = int(typeofplayer)
            if nameOK and DNIOK and typeofplayerOK:
                sql = "INSERT INTO player (player_id, player_name, player_risk, human) VALUES (%s, %s, %s, %s)"
                val = (DNI, name, typeofplayer, 1)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "Record Inserted")
            else:
                print("There's an error")
        elif opc01 == "2":  # Bot player
            print("a")
        elif opc01 == "3":  # Menu01
            print("a")
        elif opc01 == "4":  # Menu01
            print("a")
        else:
            print(f"Invalid option: {opc01}")
    except TypeError as TE:
        print("Error:", TE)
    except Exception:
        print("There's an error, try again")


def menu02():                    #----------------------------------Settings--------------------------------------
    printmenu02 = "1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\n4)Go back"
    try:
        print("\n\n\n" + printmenu02)
        opc02 = input("Select an option: ")
        if opc02 == "1":  # Menu02
            print("a")
        elif opc02 == "2":  # Menu02
            print("a")
        elif opc02 == "3":  # Menu02
            print("a")
        elif opc02 == "4":  # Menu02
            print("a")
        else:
            print(f"Invalid Option: {opc02}")
    except Exception:
        print("There's an error, try again")


def menu03():                   #--------------------------------Este es el juego--------------------------------------
    print("El juego")           #----------------------------------------------------------------------------------------------al terminar borrar esto


def menu04():                   #--------------------------------Ranking--------------------------------------
    print("menu04")
    printmenu04 = "1)Players With More Earnings\n2)Players With More Games Played\n3)Players With More Minutes Played"
    try:
        print(printmenu04)
        opc04 = input("Select an option: ")
        if opc04 == "1":
            print("a")
        if opc04 == "2":
            print("a")
        if opc04 == "3":
            print("a")
    except Exception:
        print("There's an error, try again")


def menu05():                   #--------------------------------Reports--------------------------------------
    print("menu05")
