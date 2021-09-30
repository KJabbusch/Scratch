class Cat:
    def __init__(self, name, weight, age = 0, has_shots = False, outdoor_cat = False):
        self.name = name
        self.weight = weight
        self.age = age
        self.has_shots = has_shots
        self.outdoor_cat = outdoor_cat

    def gets_food_serving(self):
        # for every 1 pound of cat, feed 0.5 gram of food
        if self.weight > 15:
            food_serving = self.gets_diet_plan()
        else:
            food_serving = self.weight * 0.5
        return food_serving

    def gets_diet_plan(self):
        # for every 1 pound of cat, feed 0.25 grams of food!
        food_serving = self.weight * 0.25
        return food_serving

    def classifies_age(self):
        if self.age < 0.5:
            life_stage = "Kitten"
        elif self.age < 10:
            life_stage = "Adult"
        else:
            life_stage = "Senior"
        return life_stage

nathan = Cat("Nathan", 15.7, 10, True)
print(nathan.weight)
print(nathan.age)
print(nathan.has_shots)
print(nathan.outdoor_cat)
print(nathan.gets_food_serving())
print(nathan.classifies_age())