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

meow()
hiss()