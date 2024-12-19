import json
import random
import os
import klasses
import matplotlib.pyplot as plt

# Laad vragen uit het JSON-bestand
with open('vragen.json') as f:
    data = json.load(f)

# Laad of initialiseer de database voor scores
if os.path.exists('scores.json') and os.path.getsize('scores.json') > 0:
    with open('scores.json') as f:
        scores_db = json.load(f)
else:
    scores_db = {}

# Lijst voor het opslaan van vraagobjecten
vragen_lijst = []
for i in data:
    vraag_type = i.get("type")
    if vraag_type == "multiple_choice":
        vragen_lijst.append(klasses.Meerkeuze(i["vraag"], i["opties"], i["antwoord"]))
    elif vraag_type == "waar_niet_waar":
        vragen_lijst.append(klasses.WaarOfNietWaarVraag(i["vraag"], i["antwoord"]))
    elif vraag_type == "open":
        vragen_lijst.append(klasses.OpenVraag(i["vraag"], i["antwoord"]))

# Functie om een vraag te stellen
def vraag_stellen(vraag):
    vraag.geef_Vraag()
    antwoord = input("Jouw antwoord: ").strip()
    return vraag.controleer_antwoord(antwoord)

# Functie om high scores weer te geven en grafisch weer te geven
def toon_high_scores():
    if scores_db:
        print("Top 10 Scores:")
        top_scores = sorted(scores_db.items(), key=lambda x: x[1], reverse=True)[:10]
        for speler, score in top_scores:
            print(f"{speler}: {score}")

        # Toon de high scores in een grafiek
        namen = [item[0] for item in top_scores]
        scores = [item[1] for item in top_scores]

        plt.figure(figsize=(10, 6))
        plt.barh(namen[::-1], scores[::-1], color='skyblue')
        plt.xlabel('Score')
        plt.ylabel('Speler')
        plt.title('Top 10 Scores')
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    else:
        print("Er zijn nog geen scores.")


# Functie om een nieuwe vraag toe te voegen
def vraag_toevoegen():
    vraag_type = input("Wat voor type vraag wil je toevoegen? (multiple_choice, waar_niet_waar, open): ").strip().lower()
    vraag_tekst = input("Voer de vraag in: ").strip()

    if vraag_type == "multiple_choice":
        opties = [input(f"Optie {i+1}: ").strip() for i in range(4)]  # Vier opties
        antwoord = input("Wat is het juiste antwoord?: ").strip()
        nieuwe_vraag = klasses.Meerkeuze(vraag_tekst, opties, antwoord)
    elif vraag_type == "waar_niet_waar":
        antwoord = input("Wat is het juiste antwoord (waar/niet waar)?: ").strip()
        nieuwe_vraag = klasses.WaarOfNietWaarVraag(vraag_tekst, antwoord)
    elif vraag_type == "open":
        antwoord = input("Wat is het juiste antwoord?: ").strip()
        nieuwe_vraag = klasses.OpenVraag(vraag_tekst, antwoord)
    else:
        print("Ongeldig type vraag!")
        return

    # Voeg de nieuwe vraag toe aan de vragenlijst en het JSON-bestand
    vragen_lijst.append(nieuwe_vraag)
    with open('vragen.json', 'w') as f:
        json.dump([vraag.__dict__ for vraag in vragen_lijst], f)

    print("Vraag succesvol toegevoegd!")

# Keuzemenu voordat het spel begint
def keuze_menu():
    while True:
        keuze = input("Wil je starten met spelen, de high scores zien, een vraag toevoegen, of stoppen? (starten/highscores/toevoegen/stoppen): ").strip().lower()
        if keuze == "starten":
            return
        elif keuze == "highscores":
            toon_high_scores()
        elif keuze == "toevoegen":
            vraag_toevoegen()
        elif keuze == "stoppen":
            print("Tot ziens!")
            exit()
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

# Vraag naar het aantal spelers
def start_spel():
    while True:
        try:
            aantal_spelers = int(input("Hoeveel spelers? (1 of 2): "))
            if aantal_spelers in [1, 2]:
                break
            else:
                print("Geef een geldig getal (1 of 2).")
        except ValueError:
            print("Voer een geldig getal in.")

    if aantal_spelers == 1:
        speler = input("Wat is je naam? ").strip()
        scores_db.setdefault(speler, 0)  # Zet de score op 0 als speler nog niet bestaat
        score = 0

        while True:
            vraag = random.choice(vragen_lijst)
            if vraag_stellen(vraag):
                score += 1
                print("Goed!")
            else:
                print(f"Fout! Je score is: {score}")
                scores_db[speler] = max(scores_db.get(speler, 0), score)

                # Controleer of de speler een nieuwe high score heeft
                top_scores = sorted(scores_db.items(), key=lambda x: x[1], reverse=True)[:10]
                if top_scores[0][0] == speler or top_scores[-1][0] == speler:
                    toon_high_scores()

                break

        # Sla de scores op
        with open('scores.json', 'w') as f:
            json.dump(scores_db, f)

    elif aantal_spelers == 2:
        if len(vragen_lijst) < 20:
            print("Niet genoeg vragen voor een duel!")
            exit()

        speler1 = input("Naam van speler 1: ").strip()
        speler2 = input("Naam van speler 2: ").strip()
        score1 = 0
        score2 = 0

        for ronde in range(10):
            print(f"Ronde {ronde + 1}: {speler1} is aan de beurt.")
            vraag = random.choice(vragen_lijst)
            if vraag_stellen(vraag):
                score1 += 1
                print("Goed!")
            else:
                print("Fout!")

            print(f"Ronde {ronde + 1}: {speler2} is aan de beurt.")
            vraag = random.choice(vragen_lijst)
            if vraag_stellen(vraag):
                score2 += 1
                print("Goed!")
            else:
                print("Fout!")

        print(f"{speler1} scoorde: {score1}, {speler2} scoorde: {score2}")
        if score1 > score2:
            print(f"{speler1} wint met {score1} punten!")
        elif score2 > score1:
            print(f"{speler2} wint met {score2} punten!")
        else:
            print("Het is gelijkspel!")

# Hoofdprogramma
keuze_menu()
start_spel()
