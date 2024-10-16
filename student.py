class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        if self.marks>=500:
            return "pass"
        else:
            return "fail"
         
