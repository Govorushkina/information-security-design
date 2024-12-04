import json
from datetime import datetime
import re


class BaseDriver:
    def __init__(self, driver_id, last_name, first_name,  sur_name, phone_number, birthday):
        self.__driver_id = driver_id
        self.set_last_name(last_name)
        self.set_first_name(first_name)
        self.set_sur_name(sur_name)
        self.set_phone_number(phone_number)
        self.set_birthday(birthday)

    @staticmethod
    def validate_string(value: str):
        if not isinstance(value, str) or len(value.strip()) == 0:
            return False
        return True

    # @staticmethod
    # def validate_driver_id(driver_id: int):
    #     if not isinstance(driver_id, int) or driver_id <= 0:
    #         return False
    #     return True

    @staticmethod
    def validate_phone_number(phone):
        return isinstance(phone, str) and re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}', phone)

    @staticmethod
    def validate_birthday(birthday) -> bool:
        return isinstance(birthday, datetime)

    # Классовый метод создания клиента из JSON
    @classmethod
    def from_json(data_json):
        try:
            data = json.loads(data_json)
            birthday = datetime.strptime(data['birthday'].strip(), "%Y-%m-%d").date()
            return BaseDriver(
                driver_id=data['driver_id'],
                last_name=data['last_name'],
                first_name=data['first_name'],
                sur_name=data['sur_name'],
                phone_number=data['phone_number'],
                birthday=birthday
            )
        except Exception as e:
            raise ValueError("Данные JSON не верны")

    # Getters
    # def get_driver_id(self):
    #     return self.__driver_id

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_sur_name(self):
        return self.__sur_name

    def get_phone_number(self):
        return self.__phone_number

    def get_birthday(self):
        return self.__birthday

    # Setters с валидацией
    # def set_driver_id(self, driver_id: int):
    #     # self.validate_driver_id(driver_id)
    #     self.__driver_id = driver_id

    def set_last_name(self, last_name: str):
        if not self.validate_string(last_name):
            raise ValueError(f"{last_name} не должно быть пустым.")
        self.__last_name : str = last_name

    def set_first_name(self, first_name: str):
        if not self.validate_string(first_name):
            raise ValueError(f"{first_name} не должно быть пустым.")
        self.__first_name = first_name

    def set_sur_name(self, sur_name: str):
        if not self.validate_string(sur_name):
            raise ValueError(f"{sur_name} не должно быть пустым.")
        self.__sur_name = sur_name

    def set_phone_number(self, phone_number):
        if not self.validate_phone_number(phone_number):
            raise ValueError("Номер телефона введен неверно(поле не может быть пустым).")
        self.__phone_number = phone_number

    def set_birthday(self, birthday):
        if self.validate_birthday(birthday):
            raise ValueError("Дата рождения не может быть пустой.")
        self.__birthday = birthday

    # def __repr__(self):
    #     return (f"Driver(driver_id={self.__driver_id}, last_name='{self.__last_name}', "
    #             f"first_name='{self.__first_name}', sur_name='{self.__sur_name}', "
    #             f"phone_number={self.__phone_number})")

    def __str__(self):
        return (f"Driver ID: {self.__driver_id}, Name: {self.__last_name} {self.__first_name} {self.__sur_name}, "
                f"phone_number: {self.__phone_number} ,birthday: {self.__birthday} ")

    @property
    def short_version(self):
        return f"Driver({self.get_first_name()} {self.get_last_name()})"

    # Представление для полной версии объекта
    @property
    def full_version(self):
        return (f"Driver(Driver:{self.get_first_name()} {self.get_last_name()} {self.get_sur_name()}, "
                f"birthday={self.get_birthday()}, "
                f"phone_number={self.get_phone_number()})")

    # Сравнение объектов на равенство
    def __eq__(self, other):
        if isinstance(other, BaseDriver):
            return (self.get_first_name() == other.get_first_name() and
                    self.get_last_name() == other.get_last_name()and
                    self.get_sur_name() == other.get_sur_name()and
                    self.get_phone_number() == other.get_phone_number()and
                    self.get_birthday() == other.get_birthday())
        return False

# class BaseDriver(BaseDriver):
#     def __init__(self, driver: BaseDriver, inn: str, ogrn: str):
#         super().__init__(driver.get_driver_id(), driver.get_last_name(),
#                          driver.get_first_name(), driver.get_sur_name(),
#                          driver.get_phone_number())
#         self.inn = inn
#         self.ogrn = ogrn
#
#     def __str__(self):
#         return (f"Driver Summary: {self.get_last_name()} {self.get_first_name()[0]}. {self.get_sur_name()[0]}., "
#                 f"INN: {self.inn}, OGRN: {self.ogrn}")
#
#     def short_description(self):
#         return f"{self.get_last_name()} {self.get_first_name()[0]}. {self.get_sur_name()[0]}."
#
#
# # Пример использования
# driver = BaseDriver(1, "Ivanov", "Ivan", "Ivanovich", "8999999998", "10-03-00")
# driver2 = BaseDriver(1, "Ivanov", "Ivan", "Ivanovich", "8999999999", "10-03-00")
# print(driver)
# print(driver.full_version)
# print(driver.short_version)
# print(driver == driver2)

# summary = BaseDriver(driver, inn="123456789012", ogrn="1234567891234")
#
# # Вывод полной информации
# print(repr(driver))
#
# # Вывод краткой информации
# print(summary)  # Полная информация о кратком представлении
# print(summary.short_description())  # Краткое описание
#
# # Сравнение объектов
# print(driver == summary)  # False, так как это разные классы
