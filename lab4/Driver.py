from Person import Person


class Driver(Person):
    drive_experience: int

    def __init__(self, fullname: str, age: int, drive_exp: int):
        super().__init__(fullname, age)
        self.drive_experience = drive_exp

    def __str__(self):
        return f'{self.fullname=}, {self.age=}, {self.drive_experience=}'
