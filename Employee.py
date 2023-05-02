class Employee:
    def __init__(self, id, name=None, postion=None, salary=None):
        self.id = id
        self.name = name
        self.position = postion
        self.salary = salary

    def get_employee(self):
        return {"id": self.id, "name": self.name, "position": self.position,
                "salary": self.salary}