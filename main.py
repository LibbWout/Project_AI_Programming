import json
import random
import klasses

# Open JSON file
with open('vragen.json') as f:
    data = json.load(f)

# Lijst voor het opslaan van alle vraagobjecten
vragen_lijst = []

# Itereren door de json-lijst
for i in data:
    vraag_type = i.get("type")

    if vraag_type == "multiple_choice":
        vraag = klasses.Meerkeuze(i["vraag"], i["opties"], i["antwoord"])
    elif vraag_type == "waar_niet_waar":
        vraag = klasses.WaarOfNietWaarVraag(i["vraag"], i["antwoord"])
    elif vraag_type == "open":
        vraag = klasses.OpenVraag(i["vraag"], i["antwoord"])
    else:
        continue  # Onbekend type, sla deze iteratie over

    # Voeg het object toe aan de lijst
    vragen_lijst.append(vraag)

# Willekeurig een vraag selecteren
willekeurige_vraag = random.choice(vragen_lijst)

# De willekeurige vraag tonen
willekeurige_vraag.geef_Vraag()


