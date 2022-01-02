import random

wordList = ["abattu", "babille", "cabochon", "dalmatien", "effacerait", "fabrication", "galipoterais", "habits", "iceberg", "jacobine", "kalmoukes", "laceraient", "macadamisai", "nantissement", "oblate", "pactole", "quadrant", "rabaisser", "sabbatique", "tabletterie", "ultrasonique", "vaccin", "wallons", "xanthies", "yoghourts", "zambiennes"]

def choisirMotMystere() :
    return wordList[random.randint(0, 26)]

def initialiserMotMystere(motATrouver) :
    result = ""
    for i in range(len(motATrouver)) :
        result += "*"
    print("Mot mystère à trouver : " + result + "\n")
    return result

def afficherMotMystere(motATrouver, motMystere, saisieUtilisateur) :
    if saisieUtilisateur == "" :
        return motMystere
    for i in range(0, len(motATrouver)):
        if motATrouver[i] == saisieUtilisateur :
           motMystere = motMystere[:i] + saisieUtilisateur + motMystere[i+1:]
    print("Mot mystère à trouver : " + motMystere + "\n")
    return motMystere

def demanderSaisie() :
    saisie = ""
    while len(saisie) != 1 :
        saisie = str(input("Saisir une lettre : "))
    print("")
    return saisie

def controlerLettresSaisies(saisieUtilisateur, lettresSaisies) :
    entered = False
    for l in lettresSaisies :
        if saisieUtilisateur == l :
            print("Vous avez déjà saisi cette lettre.\n")
            entered = True
    return entered

def memoriserLettresSaisies(saisieUtilisateur, lettresSaisies, doublonLettreSaisie) :
    if not doublonLettreSaisie :
        lettresSaisies.append(saisieUtilisateur)
    return lettresSaisies

def controlerLettreDansMot(saisieUtilisateur, motATrouver) :
    isInputValid = False
    for l in motATrouver :
        if saisieUtilisateur == l :
            isInputValid = True
    return isInputValid

def afficherViesRestants(saisieCorrecte, nombreViesRestants, doublonLettreSaisie) :
    if not saisieCorrecte:
        print("Vous avez fait une erreur ...\n")
        nombreViesRestants -= 1
    print("Il vous reste encore : " + str(nombreViesRestants) + " vie(s)\n")
    return nombreViesRestants

def validerReponse(motATrouver, motMystere) :
    if motMystere == motATrouver :
        print("Vous avez gangé. Le mot mystère a été trouvé !")
        return True
    return False

if __name__ == "__main__" :
    lettresSaisies = []
    nombreViesMax = 10
    nombreViesRestants = nombreViesMax
    reponseValide = False

    motATrouver = choisirMotMystere()
    motMystere = initialiserMotMystere(motATrouver)

    while not reponseValide :
        saisieUtilisateur = demanderSaisie()
        motMystere = afficherMotMystere(motATrouver, motMystere, saisieUtilisateur)
        doublonLettreSaisie = controlerLettresSaisies(saisieUtilisateur, lettresSaisies)
        lettresSaisies = memoriserLettresSaisies(saisieUtilisateur, lettresSaisies, doublonLettreSaisie)
        saisieCorrecte = controlerLettreDansMot(saisieUtilisateur, motATrouver)
        nombreViesRestants = afficherViesRestants(saisieCorrecte, nombreViesRestants, doublonLettreSaisie)
        if nombreViesRestants == 0 :
            print("Désolé, vous avez perdu toutes vos vies.")
            print("Le mot mystère à trouver est : " + motATrouver)
            break
        reponseValide = validerReponse(motATrouver, motMystere)