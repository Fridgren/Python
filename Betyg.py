
#Betygssystem

ickeGodkant = 0
godkant = 0
vg = 0
mvg = 0

mydict = int(input("Hur många skrev provet: "))
for key in range(1, mydict):
    # print (key, str(mydict))
    resultatPaProvet = int(input("Ange slutresultat mellan 0-40 poäng för student: " + str(key)))

    if (resultatPaProvet <= 19):
        ickeGodkant += 1
    elif (resultatPaProvet >= 20 and resultatPaProvet <= 29):
        godkant += 1
    elif (resultatPaProvet >= 30 and resultatPaProvet <= 35):
        vg += 1
    elif (resultatPaProvet >= 36 and resultatPaProvet <= 40):
        mvg += 1
    else:
        print("Felaktigt resultat angavs")

procentsats = ickeGodkant / mydict * 100
print("Antalet studenter med betyget Underkänt: " + str(ickeGodkant) + " (" + str( format(procentsats, '0.1f')) + " %)")
procentsats = godkant / mydict * 100
print("Antalet studenter med betyget Godkänt: " + str(godkant) + " (" + str( format(procentsats, '0.1f')) + " %)")
procentsats = vg / mydict * 100
print("Antalet studenter med betyget Väldigt Godkänt: " + str(vg) + " (" + str( format(procentsats, '0.1f')) + " %)")
procentsats = mvg / mydict * 100
print("Antalet studenter med betyget Mycket Väl Godkänt: " + str(mvg) + " (" + str( format(procentsats, '0.1f')) + " %)")
