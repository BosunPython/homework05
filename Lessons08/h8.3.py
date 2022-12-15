""" Напишите программу с классом Student, в котором есть четыре атрибута: firstName, lastName, groupNumber и age.
        Установить им любые значения по умолчанию. Необходимо создать пять методов: getFullName, getAge, getGroupNumber, setNameAge, setGroupNumber.
        Метод getFullName нужен для получения данных об полном имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, метод GetGroupNumber нужен для получения данных о номере группы конкретного студента.
        Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
        В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы."""
class Student:
    def __init__(self, firstName: str, lastName: str, groupNumber: int , age):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age
    def getFullName(self):
        print(f'{self.firstName} {self.lastName}')

    def getAge(self):
        print(f'Возраст {self.firstName} {self.age}')

    def getGroupNumber(self):
        print(f'{self.firstName} учится в {self.groupNumber} группе.')

    def SetNameAge(self):
        new_name = input("Введите новое имя")
        new_age = input("Введите новый возраст")
        self.firstName = new_name
        self.age = new_age
        print(f'{self.firstName} возраст {self.age}')
    def setGroupNumber(self):
        new_group = input("Введите новую группу")
        self.groupNumber = new_group
        print(f'{self.groupNumber}')

ob1 = Student("Andrey", "U", 35, 34)
ob2 = Student("Lionel", "Messi", 36, 35)
ob3 = Student("Kylian", "Mbappé", 20, 23)
ob4 = Student("Erling", "Haaland", 14, 22)
ob5 = Student("Antoine", "Griezmann", 55, 31)

ob1.getFullName()
ob1.getGroupNumber()
ob1.getAge()
ob1.SetNameAge()
ob1.setGroupNumber()

ob2.getFullName()
ob2.getGroupNumber()
ob2.getAge()
ob2.SetNameAge()
ob2.setGroupNumber()

ob3.getFullName()
ob3.getGroupNumber()
ob3.getAge()
ob3.SetNameAge()
ob3.setGroupNumber()

ob4.getFullName()
ob4.getGroupNumber()
ob4.getAge()
ob4.SetNameAge()
ob4.setGroupNumber()

ob5.getFullName()
ob5.getGroupNumber()
ob5.getAge()
ob5.SetNameAge()
ob5.setGroupNumber()
