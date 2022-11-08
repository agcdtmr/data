class Techie:

    def __init__(self, name, age, profession, location):
        self.name = name
        self.age = age
        self.profession = profession
        self.location = location


    def get_name(self):
        return f"You can call me {self.name}"


    def get_age(self):
        return f"I am {self.age} years old"


    def get_profession(self):
        return f"I am a/an {self.profession}"


    def get_location(self):
        return f"I joined Techlabs {self.location}"
