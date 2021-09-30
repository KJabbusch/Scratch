class PotentialWife:
    def __init__(self, name = "", birthday = "", cuteness_factor = int, eats_hot_chip = bool,  lies = bool, watches_anime = True):
        self.name = name
        self.birthday = birthday
        self.cuteness_factor = cuteness_factor
        self.eats_hot_chip = eats_hot_chip
        self.lies = lies
        self.watches_anime = watches_anime

    def measures_cuteness_factor(self):
        if self.cuteness_factor == 10:
            return "10/10? You are Soobin wife material. Match made in heaven."
        else:
            return "Better choose another bias."

    def requires_hot_chip_no_lying(self):
        if self.eats_hot_chip == True and self.lies == False:
            return "All my yeobo does is eat hot chip and not lie <3"
        else:
            return "Moments of Alwaysness? More like Moments of NEVER."

kristel = PotentialWife("Kristel Jabbusch", "March 10, 1994", 10, True, False, True)
print(kristel.name)
print(kristel.measures_cuteness_factor())
print(kristel.requires_hot_chip_no_lying())