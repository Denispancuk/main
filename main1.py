import random
class Student: 
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True
        self.money = 300
        self.hunger = 10
        self.thirst = 20

    def study(self):
        print("Вчиться")
        self.gladness -= 5
        self.progress += 10
        self.hunger += 10
        self.thirst += 15

    def sleep(self):
        print("спить")
        self.gladness += 10
        self.hunger += 10
        self.thirst += 15
    def shop(self):
        print("Купляє продукти")
        if self.hunger > self.thirst:
            self.money -= 150
            self.hunger -= 20
        if self.hunger < self.thirst:
            self.money -= 100
            self.thirst -= 15
            
    def chill(self):
        print("Релаксує")
        self.gladness += 5
        self.progress -= 5
    def work(self):
        print("Працює")
        self.gladness -= 10
        self.progress -= 5
        self.money += 250
    def is_alive(self):
        if self.progress < -10:
            print("Відрахований")
            self.alive = False
        if self.gladness <= 0:  
            print("Депресія")
            self.alive = False
        if self.hunger >= 90:
            print("Голод")
            self.alive = False
        if self.thirst >= 90:
            print("спрага")
            self.alive = False
        if self.money <= -100:
            print("Банкрот")
            self,alive = False

    def student_info(self):
        print(f"Студент {self.name}, Успішність: {self.progress}, енергія: {self.gladness}, гроші: {self.money}, Голод: {self.hunger}, Спрага: {self.thirst}")
    def live(self,day):
        print(f"день {day}, із життя {self.name}")

        live_choise = random.randint(1,5)

        if live_choise == 1:
            self.study()
        elif live_choise == 2:
            self.chill()
        elif live_choise == 3:
            self.sleep()
        elif live_choise == 4:
            self.work()
        elif live_choise == 5:
            self.shop()

        self.is_alive()
        self.student_info()


student = Student("John")
for day in range(365):
    if student.alive == False:
        break
    student.live(day)




