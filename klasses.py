class Vraag:
    def __init__(self, vraag):
        self.vraag = vraag
    
    def geef_Vraag(self):
        print(self.vraag)

    def controleer_antwoord(self, antwoord):
        pass

class Meerkeuze(Vraag):
    def __init__(self, vraag, opties, correct_antwoord):
        self.vraag = vraag
        self.opties = opties
        self.antwoord = correct_antwoord
    
    def geef_Vraag(self):
        super().geef_Vraag()  
        for i, optie in enumerate(self.opties, 1):
            print(f"{i}. {optie}")

    def controleer_antwoord(self, antwoord):
        return antwoord == self.antwoord
    
class WaarOfNietWaarVraag(Vraag):
    def __init__(self, vraag, correct_antwoord):
        self.vraag = vraag
        self.antwoord = correct_antwoord

    def geef_Vraag(self):
        super().geef_Vraag()  
        print("Waar of Niet Waar?")

    def controleer_antwoord(self, antwoord):
        return antwoord == self.antwoord

class OpenVraag(Vraag):
    def __init__(self, vraag, correct_antwoord):
        self.vraag = vraag
        self.antwoord = correct_antwoord

    def controleer_antwoord(self, antwoord):
        return antwoord.lower() == self.antwoord.lower()