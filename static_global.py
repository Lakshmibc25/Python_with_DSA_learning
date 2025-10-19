class Student:
    
    def __init__(myself,name,roll,marks):
        myself.name = name
        myself.roll = roll
        myself.marks = marks
    
    def display(abc):
        print('Student Name: ',abc.name)
        print('Student Roll No: ',abc.roll)
        print('Student Marks: ',abc.marks)
        college = 'UCLA'
        print('college Name: ', college)
        print()

S1 = Student('aaa',101,78.25)
S2 = Student('bbb',102,56.25)


S1.display()
S2.display()