class ProgrammingLanguage:
    def __init__(self,Field= "",Typing="",Reflection="", Year=0  ):
        self.Field = Field
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year
    def is_dynamic(self):
        if self.Typing == "Dynamic":
            print(self.Field)

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.Field,self.Typing,self.Reflection,self.Year)
