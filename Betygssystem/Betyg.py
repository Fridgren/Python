# Betygssystem



ickeGodkant = 0
godkant = 0
vg = 0
mvg = 0

userinput = int(input("Hur många skrev provet: "))
for i in range(userinput):
    i += 1
    resultatPaProvet = int(input("Ange slutresultat mellan 0-40 poäng för student: " + str(i)))

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

procentsats = ickeGodkant / userinput * 100
print("Antalet studenter med betyget Underkänt: " + str(ickeGodkant) + " (" + str(format(procentsats, '0.1f')) + " %)")
procentsats = godkant / userinput * 100
print("Antalet studenter med betyget Godkänt: " + str(godkant) + " (" + str(format(procentsats, '0.1f')) + " %)")
procentsats = vg / userinput * 100
print("Antalet studenter med betyget Väldigt Godkänt: " + str(vg) + " (" + str(format(procentsats, '0.1f')) + " %)")
procentsats = mvg / userinput * 100
print("Antalet studenter med betyget Mycket Väl Godkänt: " + str(mvg) + " (" + str(format(procentsats, '0.1f')) + " %)")

