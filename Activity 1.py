class dog:

    species = "dog"

    def __init__(self, breed, age, colour):

        self.breed = breed
        self.age = age
        self.colour = colour

Chihuahua = dog("Chihuahua",23 ,"White, Fawn, Chocolate")
Poodle = dog("Poodle",25 ,"White, Apricot")

print("Chihuahua is {}".format(Chihuahua.species))
print("Poodle is {}".format(Poodle.species))

print("{} is {} years old".format(Chihuahua.breed, Chihuahua.age))
print("{} is {} years old".format(Poodle.breed, Poodle.age))

print("The colour of the chihuahua is {}".format(Chihuahua.colour))
print("The colour of the poodle is {}".format(Poodle.colour))