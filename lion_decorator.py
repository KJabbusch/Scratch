class Lion():
    
    kingdom_name = "Animalia"
    phlyum_name = "Chordata"

    @staticmethod
    def kingdom():
        print("Animalia")
    
    @classmethod
    def create_friendly_lion(cls):
        return cls(sound ="meep", size = "medium")

    def __init__(self, size = "big", mane = "fluffy", sound = "roar"):
        self.size = size
        self.mane = mane
        self.sound = sound

    def __str__(self):
        return f"This lion is {self.size}, has a {self.mane} mane and says {self.sound}."

    @classmethod
    def phylum(cls):
        return cls.phlyum_name
    
    @classmethod
    def class_name(cls):
        return "Mammalia"

    @classmethod
    def order(cls):
        return "Carnivora"

    def make_sound(self):
        return self.sound