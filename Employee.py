# Author: Michael Beaudet
# Title: Program 4 Week 10: Employee Class
# Date: 4/1/25

class Employee:
# Initialize each variable
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
# Display each piece of data
    def employee_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.id_number}")
        print(f"Job Title: {self.job_title}")
        print('-' * 30)

def main():
# Create each employee object
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
# Display each object
    employee1.employee_info()
    employee2.employee_info()
    employee3.employee_info()
            
if __name__ == "__main__":
    main()

