class Student: 
    name = ""
    age = 0
    sex = ""
    score = 0

    def introduce():
        print(f"Név: {name} \nKor: {age} \nPontszám: {score}")

tivadar = Student()
print(tivadar)

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

print(f"Név: {tivadar.name} \nKor: {tivadar.age} \nPontszám: {tivadar.score}")

introduce()