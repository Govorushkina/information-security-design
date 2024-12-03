import json
from datetime import datetime


class BaseDriver:
    def __init__(self, driver_id, last_name=None, first_name=None, sur_name=None, phone_number= None, birthday=None):
        # if isinstance(driver_id, str):
        #     self.initialize_from_string(driver_id)
        # elif isinstance(driver_id, dict):
        #     self.initialize_from_json(driver_id)
        # else:
        self.__driver_id = driver_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__sur_name = sur_name
        self.__phone_number = phone_number
        self.__birthday = birthday

    # def initialize_from_string(self, data_str: str):
    #     data = data_str.split(',')
    #     if len(data) != 5:
    #         raise ValueError(
    #             "String must contain exactly 5 values: driver_id,last_name,first_name,sur_name,phone_number")
    #
    #     driver_id, last_name, first_name, sur_name, phone_number = data
    #     self.set_driver_id(int(driver_id))
    #     self.set_last_name(last_name.strip())
    #     self.set_first_name(first_name.strip())
    #     self.set_sur_name(sur_name.strip())
    #     self.set_phone_number(int(phone_number))

    # def initialize_from_json(self, json_data: dict):
    #     self.set_driver_id(json_data.get('driver_id'))
    #     self.set_last_name(json_data.get('last_name'))
    #     self.set_first_name(json_data.get('first_name'))
    #     self.set_sur_name(json_data.get('sur_name'))
    #     self.set_phone_number(json_data.get('phone_number'))

    # @staticmethod
    # def validate_string(value: str, field_name: str) -> bool:
    #     if not isinstance(value, str) or len(value.strip()) == 0:
    #         raise ValueError(f"{field_name} must be a non-empty string")
    #     return True
    #
    # @staticmethod
    # def validate_driver_id(driver_id: int) -> bool:
    #     if not isinstance(driver_id, int) or driver_id <= 0:
    #         raise ValueError("Driver ID must be a positive integer")
    #     return True
    #
    # @staticmethod
    # def validate_phone_number(phone_number: int) -> bool:
    #     if not isinstance(phone_number, int) or phone_number < 0:
    #         raise ValueError("phone_number must be a non-negative integer")
    #     return True

    # Getters
    def get_driver_id(self):
        return self.__driver_id

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
    def set_driver_id(self, driver_id: int):
        # self.validate_driver_id(driver_id)
        self.__driver_id = driver_id

    def set_last_name(self, last_name: str):
        # self.validate_string(last_name, "Last name")
        self.__last_name = last_name

    def set_first_name(self, first_name: str):
        # self.validate_string(first_name, "First name")
        self.__first_name = first_name

    def set_sur_name(self, sur_name: str):
        # self.validate_string(sur_name, "sur_name")
        self.__sur_name = sur_name

    def set_phone_number(self, phone_number: int):
        # self.validate_birthday(birthday)
        self.__phone_number = phone_number

    def set_birthday(self, birthday: datetime):
        # self.validate_birthday(birthday)
        self.__birthday = birthday

    # def __repr__(self):
    #     return (f"Driver(driver_id={self.__driver_id}, last_name='{self.__last_name}', "
    #             f"first_name='{self.__first_name}', sur_name='{self.__sur_name}', "
    #             f"phone_number={self.__phone_number})")

    def __str__(self):
        return (f"Driver ID: {self.__driver_id}, Name: {self.__last_name} {self.__first_name} {self.__sur_name}, "
                f"phone_number: {self.__phone_number} ," f"birthday: {self.__birthday} ")

    # def __eq__(self, other):
    #     if not isinstance(other, BaseDriver):
    #         return NotImplemented
    #     return (self.__driver_id == other.__driver_id and
    #             self.__last_name == other.__last_name and
    #             self.__first_name == other.__first_name and
    #             self.__sur_name == other.__sur_name and
    #             self.__phone_number == other.__phone_number)


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
# driver = BaseDriver(1, "Ivanov", "Ivan", "Ivanovich", 5)
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
