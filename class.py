class student:
    '''this is version 1.0'''
   
    def __init__(self,name,roll,marks):
        self.name = 'John'
        self.roll = 101
        self.marks = 78.25
    def __str__(self):
        return 'This is student Class'
    def display(self):
        print('student Name:',self.name)
        print('roll number:',self.roll)
        print('marks:',self.marks)
S =[student("aaa",102,43.67),
    student("bbb", 101,67),
    student("ccc",105,87.12)]
for i in S:
    i.display()