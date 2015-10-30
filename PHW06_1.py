class Animal:
    def __init__(self, name, hints):
        self.name=name
        self.hints=hints

    def guess_who_am_i(self):
        print("\n\nI will give you 3 hints, guess what animal I am")
        for i in range(len(self.hints)):
            print(self.hints[i])
            a=input("Who am I?: ")
            if a==self.name:
                print("You got it! I am",self.name)
                break
            else:
                if i<len(self.hints)-1:
                    print("Nope,try again!")
                else:
                    print("Nope!")
                    print("I'm out of hints! The answer is:", self.name)


e=Animal("elephant",["I have exceptional memory","I am the largest land-living mammal in the world","I have a long nose"])
t=Animal("tiger",["I am the biggest cat","I come in black and white or orange and black","I like to eat meat"])
b=Animal("bat",["I use use echo-location","I can fly","I see well in dark"])

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()

