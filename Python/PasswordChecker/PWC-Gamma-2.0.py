print ("Passwort Checker")
pw = input('Bitte ein Passwort eingeben:\n')
print ('\n')
print ('Anzahl der Zeichen: ' + str(len(pw)))

# Der folgende Code ist alles andere als sauber!
# Sorry deswegen! Heute weiß ich, wie man sowas
# besser lösen könnte ;)

sonderzeichen = 0
sonderzeichen += pw.count('^')
sonderzeichen += pw.count('°')
sonderzeichen += pw.count('!')
sonderzeichen += pw.count('"')
sonderzeichen += pw.count('§')
sonderzeichen += pw.count('$')
sonderzeichen += pw.count('%')
sonderzeichen += pw.count('&')
sonderzeichen += pw.count('/')
sonderzeichen += pw.count('{')
sonderzeichen += pw.count('(')
sonderzeichen += pw.count('[')
sonderzeichen += pw.count(')')
sonderzeichen += pw.count(']')
sonderzeichen += pw.count('=')
sonderzeichen += pw.count('}')
sonderzeichen += pw.count('?')
sonderzeichen += pw.count('\u005C')
sonderzeichen += pw.count('ß')
sonderzeichen += pw.count('`')
sonderzeichen += pw.count('´')
sonderzeichen += pw.count('*')
sonderzeichen += pw.count('+')
sonderzeichen += pw.count('~')
sonderzeichen += pw.count('\u0027')
sonderzeichen += pw.count('#')
sonderzeichen += pw.count('<')
sonderzeichen += pw.count('>')
sonderzeichen += pw.count('|')
sonderzeichen += pw.count(';')
sonderzeichen += pw.count(',')
sonderzeichen += pw.count(':')
sonderzeichen += pw.count('.')
sonderzeichen += pw.count('_')
sonderzeichen += pw.count('-')

mittelsicher = 0
mittelsicher += pw.count('x')
mittelsicher += pw.count('q')
mittelsicher += pw.count('X')
mittelsicher += pw.count('Q')
mittelsicher += pw.count('z')
mittelsicher += pw.count('Z')
mittelsicher += pw.count('v')
mittelsicher += pw.count('V')
mittelsicher += pw.count('c')
mittelsicher += pw.count('C')
mittelsicher += pw.count('y')
mittelsicher += pw.count('Y')
mittelsicher += pw.count('ü')
mittelsicher += pw.count('Ü')
mittelsicher += pw.count('Ö')
mittelsicher += pw.count('ö')
mittelsicher += pw.count('ä')
mittelsicher += pw.count('Ä')

zahl = 0
zahl += pw.count('1')
zahl += pw.count('2')
zahl += pw.count('3')
zahl += pw.count('4')
zahl += pw.count('5')
zahl += pw.count('6')
zahl += pw.count('7')
zahl += pw.count('8')
zahl += pw.count('9')
zahl += pw.count('0')


print ('Anzahl der Sonderzeichen: ' + str(sonderzeichen))

sicherheit = len(pw) + (sonderzeichen * 2) + (mittelsicher * 1.5) + (zahl * 0.5)

print ('\n')

print ('Deine Sicherheits-Punkzahl: ' + str(sicherheit))

if sicherheit < 6:
    print('Das ist doch kein richtiges Passwort!')
elif sicherheit > 7 and sicherheit < 10:
    print ('Schlechtes Passwort.')
elif sicherheit > 9 and sicherheit < 15:
    print ('Mittelmäßiges Passwort.')
elif sicherheit > 15 and sicherheit < 25:
    print ('Ziemlich gutes Passwort!')
elif sicherheit > 24 and sicherheit < 38:
    print ('Sehr gutes Passwort!')
else:
    print ('Unglaublich gutes Passwort!')
