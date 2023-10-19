import random




evenements_possibles = ["six-metre_psg", "six-metre_newcastle",
             "touche_newcastle", "touche_newcastle", "touche_psg"]
evenements_possibles = []
for tir_cadre in range(105):
    evenements_possibles.append("tir_cadré")
for corner in range(97):
    evenements_possibles.append("corner")
for carton in range(2):
    evenements_possibles.append("carton_rouge")
for carton in range(33):
    evenements_possibles.append("carton_jaune")
for corner in range(83):
    evenements_possibles.append("changement")
for six_metre in range(70):
    evenements_possibles.append("six_metre")
for sortie_en_touche in range(150):
    evenements_possibles.append("sortie_en_touche")
for i in range(460):
    evenements_possibles.append(None)


def jouer_match(equipes, auto=True):
    scores = [0, 0]
    minute = 0
    evenement_forcer = None
    print(f"Début du match {equipes[0]} contre {equipes[1]}")
    while True:
        if minute > 90:
            print("Le match est terminé !")
            if scores[0] > scores[1]:
                print(f"{equipes[0]} gagne le match ! L'histoire est en marche")
                print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")
            elif scores[1] > scores[0]:
                print(f"{equipes[1]} gagne le match ! L'histoire est en marche")
                print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")
            else:
                print("Match nul !")
                print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")
                return True

            return False
        if not evenement_forcer:
            # Générer un événement aléatoire à chaque minute
            evenement = random.choice(
            evenements_possibles)
        else:
            evenement = evenement_forcer
            evenement_forcer = None
        if not auto and evenement is not None:
            input()
            print(evenement)


        if evenement is None and auto:
            print('\n\n')

        if evenement == "tir_cadré":
            if random.randint(0, 100) < 35:
                if random.choice(equipes) == equipes[0]:
                    scores[0]+=1
                    print(f"Minute {minute}: But pour {equipes[0]} !")
                    print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")

                else:
                    scores[1]+=1
                    print(f"Minute {minute}: But pour {equipes[1]} ! ")
                    print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")
            else:
                if random.choice(equipes) == equipes[0]:
                    print(f"Minute {minute}: Tir cadré manqué pour {equipes[0]}.")
                else:
                    print(f"Minute {minute}: Tir cadré manqué pour {equipes[1]}.")


        elif evenement == "occasion_ratee":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Occasion ratée pour {equipes[0]}.")
            else:
                print(f"Minute {minute}: Occasion ratée pour {equipes[1]}.")
        elif evenement == "carton_jaune":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Carton jaune pour {equipes[0]}.")
            else:
                print(f"Minute {minute}: Carton jaune  pour {equipes[1]}.")
        elif evenement == "carton_rouge":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Carton rouge pour {equipes[0]}.")
            else:
                print(f"Minute {minute}: Carton rouge  pour {equipes[1]}.")
        elif evenement == "changement":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Changement pour {equipes[0]}")
            else:
                print(f"Minute {minute}: Changement pour {equipes[1]}")

        elif evenement == "sortie_en_touche":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Touche pour {equipes[0]}")
            else:
                print(f"Minute {minute}: Touche pour {equipes[1]}")

        elif evenement == "corner":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Corner pour {equipes[0]}")
                if random.randint(0, 100) < 5:
                    if random.choice(equipes) == equipes[0]:
                        scores[0] += 1
                        print(f"Minute {minute}: But grâce pour {equipes[0]} !")
                        print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")
                    else:
                        scores[1] += 1
                        print(f"Minute {minute}: But grâce pour {equipes[1]} ! ")
                        print(f"{equipes[0]} {scores[0]} - {scores[1]} {equipes[1]}")
            else:
                print(f"Minute {minute}: Corner pour {equipes[1]}")
        elif evenement == "six_metre":
            if random.choice(equipes) == equipes[0]:
                print(f"Minute {minute}: Six-Mètres pour {equipes[0]}")
            else:
                print(f"Minute {minute}: Six-Mètres pour {equipes[1]}")

        minute = minute + 1

        # but psg : 1
        # but {equipe2} : 1
        # none : 8
        # occasion raté : 3
        # CHangement psg : 1
        # changement newcastle : 1
        # carton : 2
        # touche : 4
        # corner : 2
        # six metres : 2



def start(choix_equipes_auto = False, continue_auto = True):
    if choix_equipes_auto:
        equipe1 = "SC Bastia"
        equipe2 = "AC Ajaccio"
    else:
        equipe1 = input("Entrer equipe 1: ")
        equipe2 = input("Entrer equipe 2: ")
    jouer_match([equipe1, equipe2], continue_auto)


start(choix_equipes_auto=False, continue_auto=True)
