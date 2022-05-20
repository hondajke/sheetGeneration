import sys
import os
from institute import Institute
from main import *

def add(_class, _institute):
    #print(_class)
    if _class == 'student':
        fio = input('ФИО: ')
        code = int(input('Номер студ. билета: '))
        student = Student(code, fio)
        _institute.add_student(student)
        print(_institute.get_student(code))
    if _class == 'spec':
        name = input('Название направления: ')
        spec = Specialization(name)
        _institute.add_spec(spec)
        print(_institute.get_spec(name))
        
def get(_class, _institute):
    #print(_class)
    if _class == 'student':
        code = int(input('Номер студ. билета: '))
        print(_institute.get_student(code))
    if _class == 'spec':
        name = input('Название направления: ')
        print(_institute.get_spec(name))

def main(*args):
    institute = Institute()
    
    stud = Student(123456, 'Филиппов Петр Петрович')
    spec = Specialization('ИВТ')
    institute.add_spec(spec)
    institute.add_student(stud)
    
    data = list(*args)
    #print(len(*args))
    #print(data)
    if len(data) == 3:
        if data[1] == 'add':
            #print('Yes')
            add(data[2], institute)
        if data[1] == 'get':
            get(data[2], institute)
    
    
if __name__ == "__main__":
    main(sys.argv)