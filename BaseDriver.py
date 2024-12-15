import json
from datetime import datetime
import re


class BaseDriver:
    def __init__(self, last_name, first_name,  sur_name, phone_number, birthday,  driver_id=None):
        self.driver_id = driver_id
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
#
    @staticmethod
    def validate_birthday(birthday) -> bool:
        return isinstance(birthday, datetime)

    @staticmethod
    def validate_phone_number(phone_number):
        return isinstance(phone_number, str) and (re.fullmatch(r"^89\d{9}$", phone_number))

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


    def set_last_name(self, last_name):
        if not self.validate_string(last_name):
            raise ValueError(f"{last_name} не должно быть пустым.")
        self.__last_name = last_name

    def set_first_name(self, first_name):
        if not self.validate_string(first_name):
            raise ValueError(f"{first_name} не должно быть пустым.")
        self.__first_name = first_name

    def set_sur_name(self, sur_name):
        if not self.validate_string(sur_name):
            raise ValueError(f"{sur_name} не должно быть пустым.")
        self.__sur_name = sur_name

    def set_phone_number(self, phone_number):
        if not self.validate_phone_number(phone_number):
            raise ValueError("Номер телефона введен неверно(Номер телефона должен начинаться с 89 и содержать 11 цифр).")
        self.__phone_number = phone_number

    def set_birthday(self, birthday):
        if self.validate_birthday(birthday):
            raise ValueError("Дата рождения не может быть пустой.")
        self.__birthday = birthday

    def __repr__(self):
        return (f"Driver(last_name='{self.get_last_name()}', "
                f"first_name='{self.get_first_name()}', sur_name='{self.get_sur_name()}', "
                f"phone_number={self.get_phone_number()})")

    def __str__(self):
        return (f"Driver Name: {self.get_last_name()} {self.get_first_name()} {self.get_sur_name()}, "
                f"phone_number: {self.get_phone_number()} ,birthday: {self.get_birthday()} ")

    @property
    def short_version(self):
        return f"Driver({self.get_first_name()} {self.get_last_name()})"

    @property
    def full_version(self):
        return (f"Driver(Driver:{self.get_first_name()} {self.get_last_name()} {self.get_sur_name()}, "
                f"birthday:{self.get_birthday()}, "
                f"phone_number:{self.get_phone_number()})")

    def __eq__(self, other):
        if isinstance(other, BaseDriver):
            return (self.get_phone_number() == other.get_phone_number())
        return False


class Driver(BaseDriver):
    def __init__(self, last_name, first_name, sur_name, phone_number, birthday, experience, insurance_policy,
                 driver_license, vehicle_passport, driver_id=None):
        super().__init__(last_name, first_name, sur_name, phone_number, birthday, driver_id)
        self.set_experience(experience)
        self.set_insurance_policy(insurance_policy)
        self.set_driver_license(driver_license)
        self.set_vehicle_passport(vehicle_passport)

    @classmethod
    def from_json(cls, data_json):
        try:
            data = json.loads(data_json)
            birthday = datetime.strptime(data['birthday'].strip(), "%Y-%m-%d").date()
            return cls(
                last_name=data['last_name'],
                first_name=data['first_name'],
                sur_name=data['sur_name'],
                phone_number=data['phone_number'],
                birthday=birthday,
                experience=data['experience'],
                insurance_policy=data['insurance_policy'],
                driver_license=data['driver_license'],
                vehicle_passport=data['vehicle_passport'],
            )
        except Exception as e:
            raise ValueError("Данные JSON не верны")

    def get_experience(self):
        return self.__experience

    def get_insurance_policy(self):
        return self.__insurance_policy

    def get_driver_license(self):
        return self.__driver_license

    def get_vehicle_passport(self):
        return self.__vehicle_passport

    @staticmethod
    def validate_experience(year):
        if not isinstance(year, int) or year < 0:
            return False
        return True

    @staticmethod
    def validate_document(document, value):
        return isinstance(document, int) and re.fullmatch(rf"^\d{{{value}}}$", str(document))

    def set_experience(self, experience: int):
        if not self.validate_experience(experience):
            raise ValueError("Стаж не может быть отрицательным значением.")
        self.__experience = experience


    def set_insurance_policy(self, insurance_policy: int):
        if not self.validate_document(insurance_policy, 10):
            raise ValueError("Неверно введены данные")
        self.__insurance_policy = insurance_policy

    def set_driver_license(self, driver_license: int):
        if not self.validate_document(driver_license, 6):
            raise ValueError("Неверно введены данные")
        self.__driver_license = driver_license

    def set_vehicle_passport(self, vehicle_passport: int):
        if not self.validate_document(vehicle_passport, 15):
            raise ValueError("Неверно введены данные")
        self.__vehicle_passport = vehicle_passport
    @property
    def short_description(self):
        return self.get_last_name(), self.get_phone_number()
