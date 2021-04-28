class Guitar:
    def __init__(self,name = "",year=0,cost=0):
        self.name= name
        self.year= year
        self.cost= cost
    def get_age(self):
        age = 2021 - self.year
        print(age)
        return age
    def is_vintage(self):
        age = 2021 - self.year
        if age >= 50:
            print("TRUE")
        else:
            print("False")


    def __str__(self):
        return "{}({}){}".format(self.name,self.year,self.cost)