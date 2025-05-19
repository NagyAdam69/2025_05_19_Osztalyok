class Student: 
    name = ""
    age = 0
    sex = ""
    score = 0

    def introduce(self):
        print(f"Név: {self.name} \nKor: {self.age} \nPontszám: {self.score}")

tivadar = Student()
print(tivadar)

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

tivadar.introduce()