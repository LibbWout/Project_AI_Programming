class Vraag:
    def __init__(self, vraag):
        self.vraag = vraag
    
    def geef_Vraag(self):
        print(self.vraag)

    def controleer_antwoord(self, antwoord):
        pass

class Meerkeuze(Vraag):
    def __init__(self, vraag, opties, correct_antwoord):
        super().__init__(vraag)
        self.opties = opties
        self.antwoord = correct_antwoord
    
    def geef_Vraag(self):
        super().geef_Vraag()
        for i, optie in enumerate(self.opties, 1):
            print(f"{i}. {optie}")

    def controleer_antwoord(self, antwoord):
        try:
            # Controleer of antwoord een numerieke keuze is
            if antwoord.isdigit():
                index = int(antwoord) - 1
                return self.opties[index] == self.antwoord
            # Controleer als het directe tekst is
            return antwoord == self.antwoord
        except (IndexError, ValueError):
            return False
    
class WaarOfNietWaarVraag(Vraag):
    def __init__(self, vraag, correct_antwoord):
        super().__init__(vraag)
        self.antwoord = correct_antwoord

    def geef_Vraag(self):
        super().geef_Vraag()
        print("Waar of Niet Waar?")

    def controleer_antwoord(self, antwoord):
        return str(antwoord).lower() in ["waar", "true"] if self.antwoord else str(antwoord).lower() in ["niet waar", "false"]

class OpenVraag(Vraag):
    def __init__(self, vraag, correct_antwoord):
        super().__init__(vraag)
        self.antwoord = correct_antwoord

    def controleer_antwoord(self, antwoord):
        return antwoord.strip().lower() == self.antwoord.strip().lower()
