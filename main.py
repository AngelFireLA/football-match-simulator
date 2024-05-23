import random
from math import floor


class Match:
    evenements_possibles = {
        "tir_cadré": 105,
        "corner": 97,
        "carton_rouge": 2,
        "carton_jaune": 33,
        "changement": 83,
        "six_metre": 70,
        "sortie_en_touche": 150,
        None: 460
    }
    chances_de_marquer_initiales = {"tir_cadré": 35, "corner": 5}

    def __init__(self, equipe1="Equipe 1", equipe2="Equipe 2", scores=None, minute=0):
        self.historique_evenements = []
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        if scores is None:
            self.scores = [0, 0]
        else:
            self.scores = scores
        self.minute = minute
        self.probabilites_evenements = self.generate_initial_odds()
        self.temps_additionel = False
        self.minutes_temps_additionel = 0
        self.occurences_evenements = {equipe1: {event: 0 for event in self.evenements_possibles}, equipe2: {event: 0 for event in self.evenements_possibles}}
        self.chances_de_marquer = {equipe1: self.chances_de_marquer_initiales.copy(),
                                   equipe2: self.chances_de_marquer_initiales.copy()
                                   }

    def generate_initial_odds(self):
        probabilites_evenements = []
        for evenement, probabilite in self.evenements_possibles.items():
            probabilites_evenements.extend([evenement] * probabilite)
        return probabilites_evenements

    def equipe_opposee(self, equipe):
        if equipe == self.equipe1:
            return self.equipe2
        else:
            return self.equipe1

    def generate_dynamic_odds(self, equipe):
        evenements_possibles_dynamiques = self.evenements_possibles.copy()
        if self.occurences_evenements[equipe]["changement"] >= 5:
            evenements_possibles_dynamiques.pop("changement")
        #multiply enemy team to score by amount of red cards
        for key in self.chances_de_marquer_initiales:
            self.chances_de_marquer[equipe][key] = int(self.chances_de_marquer_initiales[key] * (1.7 ** self.occurences_evenements[self.equipe_opposee(equipe)]["carton_rouge"]+floor(self.occurences_evenements[self.equipe_opposee(equipe)]["carton_jaune"]/2)))
        probabilites_evenements = []
        for evenement, probabilite in self.evenements_possibles.items():
            probabilites_evenements.extend([evenement] * probabilite)
        return probabilites_evenements

    def handle_event(self, evenement, team, log=True):
        self.generate_dynamic_odds(team)
        if evenement == "tir_cadré":
            if log: print(f"Minute {self.minute}: Tir cadré pour {team}.")
            if random.randint(0, 100) < self.chances_de_marquer[team][evenement]:
                if team == self.equipe1:
                    self.scores[0] += 1
                else:
                    self.scores[1] += 1
                if log: print(f"Minute {self.minute}: But pour {team} !")
                if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
            else:
                if log: print(f"Tir manqué.")
        elif evenement == "carton_jaune":
            if log: print(f"Minute {self.minute}: Carton jaune pour {team}.")
        elif evenement == "carton_rouge":
            if log: print(f"Minute {self.minute}: Carton rouge pour {team}.")
        elif evenement == "changement":
            if log: print(f"Minute {self.minute}: Changement pour {team}")
        # elif evenement == "sortie_en_touche":
        #     if log: print(f"Minute {self.minute}: Touche pour {team}")
        elif evenement == "corner":
            if log: print(f"Minute {self.minute}: Corner pour {team}")
            if random.randint(0, 100) < self.chances_de_marquer[team][evenement]:
                if team == self.equipe1:
                    self.scores[0] += 1
                else:
                    self.scores[1] += 1
                if log: print(f"Minute {self.minute}: But grâce à un corner pour {team} !")
                if log: print(f"{self.equipe1} {self.scores[0]} - {self.scores[1]} {self.equipe2}")
        elif evenement == "six_metre":
            if log: print(f"Minute {self.minute}: Six-Mètres pour {team}")

    def play_full_match(self, auto=True, log=True, but_en_or=False):
        evenement_forcer = None
        if log: print(f"Début du match {self.equipe1} contre {self.equipe2}")
        while True:

            if (self.minute > 90 and not self.temps_additionel) or (self.minute > 90 + self.minutes_temps_additionel):
                if not self.temps_additionel:
                    self.temps_additionel = True
                    for k, v in self.occurences_evenements.items():
                        if k is not None and k != "tir_cadré":
                            self.minutes_temps_additionel += v / 10
                    self.minutes_temps_additionel = random.randint(1, int(self.minutes_temps_additionel))
                    if log: print(f"Le temps additionnel est de {self.minutes_temps_additionel} minutes.")
                    continue
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
                if not but_en_or or self.scores[0] != self.scores[1]:
                    print(self.scores)
                    break

            if not evenement_forcer:
                evenement = random.choice(self.probabilites_evenements)
            else:
                evenement = evenement_forcer
                evenement_forcer = None

            if not auto and evenement is not None and evenement != "sortie_en_touche":
                input()
                # if log: print(evenement)
            random_team = random.choice([self.equipe1, self.equipe2])
            self.occurences_evenements[random_team][evenement] += 1
            self.historique_evenements.append(evenement)
            self.handle_event(evenement, random_team, log)

            self.minute += 1
        return self.scores, self.occurences_evenements

    def play_single_minute(self, log=True):
        evenement = random.choice(self.probabilites_evenements)
        random_team = random.choice([self.equipe1, self.equipe2])
        self.historique_evenements.append((random_team, evenement))
        self.occurences_evenements[random_team][evenement] += 1
        self.handle_event(evenement, random_team, log)
        self.minute += 1
        return self.scores, self.occurences_evenements

equipe1 = input("équipe 1 : ")
equipe2 = input("équipe 2 : ")
# Example usage
match = Match(equipe1, equipe2)
match.play_full_match(auto=False, but_en_or=True)
