class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.team_members = []

    def add_team_member(self, employee):
        if isinstance(employee, Employee):
            self.team_members.append(employee)
        else:
            print("ininstance team_member")

    def display_team(self):
        print(f"Manager: {self.name}'s Team Members:")
        for member in self.team_members:
            member.display_info()

emp = Employee("경남대", 50000)
emp2 = Employee("인공지능학과", 55000)

manager = Manager("이영호", 80000)
manager.add_team_member(emp1)
manager.add_team_member(emp2)
manager.display_info()
manager.display_team()