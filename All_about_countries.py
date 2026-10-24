class India():
    def capitel(self):
        print("New Delih is the capitel of India")

    def language(self):
        print("Hindi is the most widely spoken language in India")

    def type(self):
        print("India is a developing country")

class USA():
    def capitel(self):
        print("Washington, DC is the capitel of the USA")

    def language(self):
        print("English is primarly language in the USA ")

    def type(self):
        print("The USA is a developing country")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capitel()
    country.language()
    country.type()