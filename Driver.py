import json
from datetime import datetime
import re

from BaseDriver import BaseDriver


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


# Пример использования
summary = Driver("Ivanov", "Ivan", "Ivanovich", "89999999999", "2000-03-10", 3, 3333558756, 546956, 225555555555552)
print(summary.short_description)
