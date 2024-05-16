import random

class Match:
    evenements_possibles = ["tir_cadré", "corner", "carton_rouge", "carton_jaune", "changement", "six_metre", "sortie_en_touche", None]
    def __init__(self, equipe1="Equipe 1", equipe2="Equipe 2", scores=None, minute=0):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        if scores is None:
            self.scores = [0, 0]
        else:
            self.scores = scores
        self.minute = minute
        self.probabilites_evenements = self.generate_odds()
        self.temps_additionel = False
        self.minutes_temps_additionel = 0
        self.occurences_evenements = {event: 0 for event in self.evenements_possibles}

    def generate_odds(self):
        probabilites_evenements = []
        for tir_cadre in range(105):
            probabilites_evenements.append("tir_cadré")
        for corner in range(97):
            probabilites_evenements.append("corner")
        for carton in range(2):
            probabilites_evenements.append("carton_rouge")
        for carton in range(33):
            probabilites_evenements.append("carton_jaune")
        for corner in range(83):
            probabilites_evenements.append("changement")
        for six_metre in range(70):
            probabilites_evenements.append("six_metre")
        for sortie_en_touche in range(150):
            probabilites_evenements.append("sortie_en_touche")
        for i in range(460):
            probabilites_evenements.append(None)

        return probabilites_evenements

    def handle_event(self):
        pass
    def play_full_match(self, auto=True, log=True):
        evenement_forcer = None
        if log: print(f"Début du match {self.equipe1} contre {self.equipe2}")
        while True:

            if (self.minute > 90 and not self.temps_additionel) or (self.minute > 90+self.minutes_temps_additionel):
                if not self.temps_additionel:

                    self.temps_additionel = True
                    for k, v in self.occurences_evenements.items():
                        if k is not None and k!="tir_cadré":
                            self.minutes_temps_additionel += v/10
                    self.minutes_temps_additionel = random.randint(2, int(self.minutes_temps_additionel))
                    if log : print(f"Le temps additionnel est de {self.minutes_temps_additionel} minutes.")
                if log: print("Le match est terminé !")
                if self.scores[0] > self.scores[1]:
                    if log: print(f"{self.equipe1} gagne le match ! L'histoire est en marche")
                    if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
                elif self.scores[1] > self.scores[0]:
                    if log: print(f"{self.equipe2} gagne le match ! L'histoire est en marche")
                    if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
                else:
                    if log: print("Match nul !")
                    if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
                break
            if not evenement_forcer:
                # Générer un événement aléatoire à chaque minute
                evenement = random.choice(
                    self.evenements_possibles)
            else:
                evenement = evenement_forcer
                evenement_forcer = None
            if not auto and evenement is not None:
                input()
                if log: print(evenement)

            if evenement is None and auto:
                if log: print('\n\n')
            self.occurences_evenements[evenement]+=1
            if evenement == "tir_cadré":
                if random.randint(0, 100) < 35:
                    if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                        self.scores[0] += 1
                        if log: print(f"Minute {self.minute}: But pour {self.equipe1} !")
                        if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")

                    else:
                        self.scores[1] += 1
                        if log: print(f"Minute {self.minute}: But pour {self.equipe2} ! ")
                        if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
                else:
                    if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                        if log: print(f"Minute {self.minute}: Tir cadré manqué pour {self.equipe1}.")
                    else:
                        if log: print(f"Minute {self.minute}: Tir cadré manqué pour {self.equipe2}.")


            elif evenement == "occasion_ratee":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Occasion ratée pour {self.equipe1}.")
                else:
                    if log: print(f"Minute {self.minute}: Occasion ratée pour {self.equipe2}.")
            elif evenement == "carton_jaune":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Carton jaune pour {self.equipe1}.")
                else:
                    if log: print(f"Minute {self.minute}: Carton jaune  pour {self.equipe2}.")
            elif evenement == "carton_rouge":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Carton rouge pour {self.equipe1}.")
                else:
                    if log: print(f"Minute {self.minute}: Carton rouge  pour {self.equipe2}.")
            elif evenement == "changement":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Changement pour {self.equipe1}")
                else:
                    if log: print(f"Minute {self.minute}: Changement pour {self.equipe2}")

            elif evenement == "sortie_en_touche":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Touche pour {self.equipe1}")
                else:
                    if log: print(f"Minute {self.minute}: Touche pour {self.equipe2}")

            elif evenement == "corner":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Corner pour {self.equipe1}")
                    if random.randint(0, 100) < 5:
                        if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                            self.scores[0] += 1
                            if log: print(f"Minute {self.minute}: But grâce pour {self.equipe1} !")
                            if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
                        else:
                            self.scores[1] += 1
                            if log: print(f"Minute {self.minute}: But grâce pour {self.equipe2} ! ")
                            if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
                else:
                    if log: print(f"Minute {self.minute}: Corner pour {self.equipe2}")
            elif evenement == "six_metre":
                if random.choice((self.equipe1,self.equipe2)) == self.equipe1:
                    if log: print(f"Minute {self.minute}: Six-Mètres pour {self.equipe1}")
                else:
                    if log: print(f"Minute {self.minute}: Six-Mètres pour {self.equipe2}")

            self.minute +=1
        return self.scores, self.occurences_evenements

    def play_single_minute(self, log=True):
        pass


