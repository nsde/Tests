print ("Passwort Checker")
#Passwort wird abgefragt
pw = input('Bitte Passwort eingeben: ')

#Sagt die Anzahl der Zeichen
print ('Dein Passwort ist ' + str(len(pw)) + ' Zeichen lang.')

#Nun soll ausgegeben werden, wie gut die Länge des Passworts ist.

print ('Wir finden:')
if len(pw) < 4:
    print('Das ist doch kein richtiges Passwort!')
elif len(pw) == 4:
    print ('Viel zu kurz!')
elif len(pw) == 5:
    print ('Sehr kurz!')
elif len(pw) == 6:
    print ('Ziemlich kurz!')
elif len(pw) == 7:
    print ('Etwas kurz.')
elif len(pw) == 8:
    print ('Nicht wirklich lang.')
elif len(pw) == 9:
    print ('Mittelmäßig lang.')
elif len(pw) == 10:
    print ('Okay!')
elif len(pw) == 11:
    print ('Gut!')
elif len(pw) == 12:
    print ('Ziemlich gut!')
elif len(pw) > 12 and len(pw) < 20:
    print ('Super!')
elif len(pw) > 20:
    print ('Arbeitest du bei einem Geheimdienst?')
else:
    print ('Ein Fehler ist aufgetreten.')
