from lion_decorator import Lion

def cat_named_nathan(sound_function):
    def nathan_says():
        print("Nathan says ")
        sound_function()
    return nathan_says

@cat_named_nathan
def meow():
    print("meow")

@cat_named_nathan
def hiss():
    print("hissssss")

#print(Lion.kingdom())
my_friendly_lion = Lion.create_friendly_lion()
print(my_friendly_lion.sound)
print(my_friendly_lion)