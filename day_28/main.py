class Person:
    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio) and self.verify_age(age) and self.verify_weight(weight) and self.verify_ps(passport):
            self.__fio = fio
            self.__age = age
            self.__weight = weight
            self.__passport = passport

    @staticmethod
    def verify_fio(fio):
        err = '''\n- ФИО должно быть строкой\n- Неверный формат записи ФИО
- В ФИО должен быть хотя бы один символ\n- В ФИО можно использовать только буквенные символы'''
        if type(fio) is not str \
                or list(filter(lambda i: len(fio.split()) != 3 or i.isalpha() is False or len(i) < 1, fio.split())):
            raise TypeError(err)
        return True

    @staticmethod
    def verify_age(age):
        err = '''Возраст должен быть целым числом от 14 до 150'''
        if type(age) is not int or age < 14 or age > 150:
            raise TypeError(err)
        return True

    @staticmethod
    def verify_weight(weight):
        err = '''Вес должен быть вещественным числом от 25 и выше'''
        if type(weight) is str or weight < 25:
            raise TypeError(err)
        return True

    @staticmethod
    def verify_ps(passport):
        err = '''\n- Паспорт должен быть строкой\n- Неверный формат паспорта
- Серия и номер паспорта должны содержать только числа'''
        if type(passport) is not str or passport.replace(' ', '').isdigit() is False or len(passport.split()) != 2 \
                or len(passport.split()[0]) != 4 or len(passport.split()[1]) != 6:
            raise TypeError(err)
        return True

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @property
    def passport(self):
        return self.__passport

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p1 = Person('Иванов Иван Иванович', 50, '0000 000000', 85.0)
p1.fio = 'ffff fff fffff'
print(p1.fio)
p1.age = 80
print(p1.age)
p1.passport = '1000 555555'
print(p1.passport)
p1.weight = 71.2
print(p1.weight)
