class Student: 
    # konstruktor az osztály példányosításához
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = 10

    def introduce(self):
        print(f"\nNév: {self.name} \nKor: {self.age} \nPontszám: {self.score} \n")
        
    def studied(self, points):
        self.score += points

tivadar = Student("El Tivadar", 16, "male")

tivadar.introduce()
tivadar.studied(12)
tivadar.introduce()