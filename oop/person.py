class Person:
    GENDER_OPTIONS = ("female", "male")

    def __init__(self, gender, age, height, weight, name):
        self.__gender = self.__validate_gender(gender)
        self.age = age
        self.height = height
        self.weight = weight
        self.name = name

    def __validate_gender(self, gender):
        if gender not in self.GENDER_OPTIONS:
            raise ValueError(f"Gender value '{gender}' is not a valid one!")
        return gender

    def __new__(cls, *args, **kwargs):
        print("Creating person")
        return super().__new__(cls)

    def __str__(self):
        return f"I am {self.name}"

    def custom_method(self):
        print("Custom method from Person")

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        raise TypeError('Gender value is unchangeable')

    @classmethod
    def create_person(cls, *args, **kwargs):
        # Do something
        return cls(*args, **kwargs)

    @staticmethod
    def some_static_method(*args, **kwargs):
        # Do something
        pass


# person_ani = Person("female", 23, 165, 55, "Ani")
# print(person_ani)


person_pesho = Person.create_person("male", 31, 180, 75, "Pesho")
print(person_pesho)


class PersonBase:
    """This is simple docstring of Person class."""

    def __init__(self, gender, age, height, weight, name):
        self.__gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.name = name

    def __str__(self):
        """__str__ is meant to return readable information"""
        return f"I am {self.name}"

    def __repr__(self):
        """
        __repr__ on the other side is meant to return more representational information.
        When you call an instance, and you expect some string output if __str__ is missing
        the __repr__ will be tried to be called.
        If __str__ exists it will be the one to use.
        """
        return f"PersonBase(name={self.name})"

    @property
    def gender(self):
        return self.__gender


# alex = PersonBase("male", 26, 180, 85, "Alex")
# print(alex)
# print(alex.__doc__)
# print(alex.gender)
