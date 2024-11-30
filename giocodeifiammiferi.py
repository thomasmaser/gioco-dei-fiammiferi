import random

numFiammiferi = 0

print("Inizia il gioco dei fiammiferi")
while True :
    richiestaNum = input("con quanti fiammiferi vuoi giocare?\n")
    try:
        numFiammiferi = int(richiestaNum)
        if numFiammiferi>3 and numFiammiferi<100:
            print("giocheremo con", numFiammiferi, "fiammiferi")
            break
        else:
            print("il numero di fiammiferi deve essere compreso tra 3 e 100")
    except ValueError:
        numFiammiferi = random.randint(3, 100)
        print("giocheremo con", numFiammiferi, "fiammiferi")
        break



def computer(numFiammiferi):
    print("sta a me")
    if numFiammiferi%4 == 0:
        numFiammiferi -= 3
        print("ho tolto 3 fiammiferi, rimangono", numFiammiferi, "fiammiferi")
    elif numFiammiferi%4 == 1:
        numRan = random.randint(1, 3)
        numFiammiferi -= numRan
        print("ho tolto", numRan, "fiammiferi, rimangono", numFiammiferi, "fiammiferi")
    else:
        num = (numFiammiferi%4)-1
        numFiammiferi -= num
        print("ho tolto", num, "fiammiferi, rimangono", numFiammiferi, "fiammiferi")
    return numFiammiferi

def utente(numFiammiferi):
    print("sta a te")
    while True:
        tolti = input("quanti fiammiferi vuoi togliere?\n")
        try:
            fiammiferiTolti = int(tolti)
            if fiammiferiTolti>=1 and fiammiferiTolti<=3:
                numFiammiferi -= fiammiferiTolti
                print("hai tolto", fiammiferiTolti, "fiammiferi, rimangono", numFiammiferi, "fiammiferi")
                break
            else:
                print("puoi togliere da 1 a 3 fiammiferi")
        except ValueError:
            print("devi inserire un numero")
    return numFiammiferi

while True:
    numFiammiferi = computer(numFiammiferi)
    if numFiammiferi == 1:
        print("hai perso!")
        break
    else:
        numFiammiferi = utente(numFiammiferi)
        if numFiammiferi == 1:
            print("hai vinto!")
            break
        else:
            pass

# qual'è sempre stato il problema? che io mamdavo solo la funzione ma in realtà dovevo mettere 
# numFiammiferi = funz(numFiammiferi), solo così si può aggiornare il valore della variabile!!!
#
