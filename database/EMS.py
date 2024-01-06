"""
Employee Management system
___________________________

class HR:
1. Add employees
   emp_id,name,department,place,salary(private)
   store this data in CSV file.

2. List employee details
   fetch from csv file

class Employee

1. filter the employee details by emp_id
"""
import csv as c
import os as o


class HR:
    def __init__(self, id, name, dpt, salary, exp):
        self.id = id
        self.name = name
        self.dpt = dpt
        self.salary = salary
        self.exp = exp

    def Insert(self):
        file_exist = o.path.exists('Employee.csv')
        with open('Employee.csv', 'a', newline='') as file:
            headers = ['Id', 'Name', 'dept', 'salary', 'exp']
            emp = c.DictWriter(file, fieldnames=headers)
            if not file_exist:
                emp.writeheader()
            emp = c.writer(file)
            emp.writerow([self.id, self.name, self.dpt, self.salary, self.exp])
            file.close()
            print('Recorded successfully')

    def Update(self):
        with open('Employee.csv', 'r', newline='') as file:
            employee = list(c.DictReader(file))
            for i in employee:
                if i['Id'] == self.id:
                    # print(i)
                    i['Name'] = self.name
                    i['dept'] = self.dpt
                    i['salary'] = self.salary
                    i['exp'] = self.exp
                # updating the employee details
            with open('Employee.csv', 'w', newline='') as csvfile:
                headers = ['Id', 'Name', 'dept', 'salary', 'exp']
                employe = c.DictWriter(csvfile, fieldnames=headers)
                employe.writeheader()
                for i in employee:
                    employe.writerow(i)
                print('Updated successfully')


class Employee:
    def __init__(self, id):
        self.id = id

    def ViewNosecure(self, ):
        with open('Employee.csv', 'r', newline='') as file:
            emp = list(c.DictReader(file))
            for line in emp:
                if line['Id'] == self.id:
                    print(f'User ID : {line["Id"]}')
                    print(f'Name : {line["Name"]}')
                    print(f'Department : {line["dept"]}')
                    # print(f'Salary : {line["salary"]}')
                    print(f'Experience : {line["exp"]}')

    def ViewSecure(self, ):
        with open('Employee.csv', 'r', newline='') as file:
            emp = list(c.DictReader(file))
            for line in emp:
                if line['Id'] == self.id:
                    print(f'User ID : {line["Id"]}')
                    print(f'Name : {line["Name"]}')
                    print(f'Department : {line["dept"]}')
                    print(f'Salary : {line["salary"]}')
                    print(f'Experience : {line["exp"]}')


def Remove(id):
    with open('Employee.csv', 'r', newline='') as file:
        emp = list(c.DictReader(file))
        for i in emp:
            # print(i)
            if i['Id'] == id:
                emp.remove(i)
                # print(emp)
        with open('Employee.csv', 'w', newline='') as csvfile:
            headers = ['Id', 'Name', 'dept', 'salary', 'exp']
            employe = c.DictWriter(csvfile, fieldnames=headers)
            employe.writeheader()
            for i in emp:
                employe.writerow(i)


def mainHR():
    selector = input('Enter the option you want to select\n'
                     '1 . Insert a employee...\n'
                     '2 . Update employee details...\n'
                     '3 . Remove a employee...\n'
                     '4 . View employee details...\n'
                     '5 . View all employee details...\nEnter your option from above...')
    if selector == '1':
        employee_id = input('Enter employee id :')
        employee_name = input('Enter employee name :')
        employee_dpt = input('Enter employee department :')
        employee_salary = input('Enter employee salary :')
        employee_exp = input('Enter employee experience :')
        obj = HR(employee_id, employee_name, employee_dpt, employee_salary, employee_exp)
        obj.Insert()
        x = input('Do you want to continue...?(y/n)')
        if x == 'y':
            mainHR()
        elif x == 'n':
            pass

    elif selector == '2':
        id = input('Enter the id of employee which you want to update :')
        emp_name = input('Enter the name :')
        emp_dpt = input('Enter the department :')
        emp_salary = input('Enter the salary :')
        emp_exp = input('Enter the Experience :')
        obj = HR(id, emp_name, emp_dpt, emp_salary, emp_exp)
        obj.Update()
        x = input('Do you want to continue...?(y/n)')
        if x == 'y':
            mainHR()
        elif x == 'n':
            pass
    elif selector == '3':
        employee_id = input('Enter the id of employee to be removed :')
        Remove(employee_id)
        x = input('Do you want to continue...?(y/n)')
        if x == 'y':
            mainHR()
        elif x == 'n':
            pass
    elif selector == '4':
        emp_id = input('Enter the id of the employee')
        with open('Employee.csv', 'r', newline='') as file:
            emp = list(c.DictReader(file))
            for line in emp:
                if line['Id'] == emp_id:
                    print(f'User ID : {line["Id"]}')
                    print(f'Name : {line["Name"]}')
                    print(f'Department : {line["dept"]}')
                    print(f'Salary : {line["salary"]}')
                    print(f'Experience : {line["exp"]}')

    elif selector == '5':
        with open('Employee.csv', 'r', newline='') as file:
            emp = c.reader(file)
            for i in emp:
                print(i)
    else:
        print('Invalid option, please choose one valid option from the above...')


def mainEM(name):
    selector = input('Enter your choice\n'
                     '1 . View\n')
    if selector == '1':
        employee_id = input('Enter the id :')
        with open('Employee.csv', 'r', newline='') as file:
            emp = list(c.DictReader(file))
            for i in emp:
                if i['Name'] == name and i['Id'] == employee_id:
                    obj = Employee(employee_id)
                    obj.ViewSecure()

                elif i['Name'] != name and i['Id'] == employee_id:
                    obj = Employee(employee_id)
                    obj.ViewNosecure()

    else:
        print('Invalid option')
    x = input('Do you want to continue...(y/n)\n')
    if x == 'y':
        mainEM(name)
    else:
        pass


def authentification():
    admin_name = 'admin'
    admin_pass = 'password'
    # employee_name = 'employee'
    employee_pass = 'password'
    x = int(input('You want to join as\n1. HR\n2. Employee\nSelect from the above options :'))
    if x == 1:
        ad_name = input('Enter the username :')
        ad_pass = input('Enter the password :')
        if ad_name == admin_name and ad_pass == admin_pass:
            mainHR()
        else:
            print('Invalid username or password')
    elif x == 2:
        emp_name = input('Enter your username :')
        emp_pass = input('Enter your password :')
        if emp_pass == employee_pass:
            mainEM(emp_name)
        else:
            print('Invalid username or password')


authentification()
