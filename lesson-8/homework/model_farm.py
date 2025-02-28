class Animal:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
   
    def movement():
       return "running on the farm"

class Horse(Animal):
    def feed_time():
        return "at 1 p.m"
class Cow(Animal):
    def feed_time():
        return "at 00.30 p.m"
class Rabbit(Animal):
    def feed_time():
        return "at 2 p.m"
class Goat(Animal):
    def feed_time():
        return "at 1.30 p.m"

Horse.name="John"
Rabbit.name="Andy"
Goat.name="Fast"
Cow.name="Josepher"
print(Rabbit.feed_time())
print(Horse.name)
print(Goat.feed_time())
print(Cow.movement())

    