class Student:

    def __init__(self,name,roll,marks,age):
        self.name =  name
        self.roll = roll
        self.marks = marks
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.roll,
            "marks": self.marks,
            "age": self.age
         }
    @classmethod
    def from_dict(cls,data):
        return cls(data["roll"],data["name"],data["marks"],data["age"])