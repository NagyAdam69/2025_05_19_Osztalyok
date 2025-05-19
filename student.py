class Student: 
    # konstruktor az osztály példányosításához
    def __init__(self, name, sex, mood, age = "Nincs megadva"):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = 10
        self.mood = mood

    def introduce(self):
        print(f"\nNév: {self.name} \nKor: {self.age} \nPontszám: {self.score} \nHangulat: {self.mood}\n")
        
    def studied(self, points):
        self.score += points

tivadar = Student("El Tivadar", "male", "Stresszelt", 16)
leila = Student("Leila hercegnő", "female", "Tired")

tivadar.introduce()
tivadar.studied(12)
tivadar.introduce()

leila.introduce()
leila.studied(-2)
leila.introduce()