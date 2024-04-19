class Worker:
    def __init__(self, name, position, salary):
        self._name = name
        self.position = position
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def __str__(self):
        return f'Worker: {self.name}, Position: {self.position}, Salary: ${self.salary}'

# Example usage:
worker1 = Worker("Vasya", "Cleaner", 300)
print(worker1)

worker1.name = "Petya"
print(worker1)
