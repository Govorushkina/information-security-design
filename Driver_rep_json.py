import json
import os


class Driver_rep_json:

    def __init__(self, json_file):
        self.json_file = json_file

#a
    def read(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                data = json.load(f)
                return data
        return []

#b
    def write(self, data):
        with open(self.json_file, 'w') as f:
            json.dump(data, f)
        return "ок"

#c
    def get_entity_id(self, id):
        data = self.read()
        for key in data:
           if key['id'] == id:
               return key
        return None

#d
    def get_k_n_short_list(self, k, n):
        data = self.read()
        start = (n-1)*k
        end = start + k
        return data[start:end]

#e
    def sort_elem(self, attribute):
        data = self.read()
        return data.sort(key=lambda p: p[f'{attribute}'])

#f
    def add_entity(self, last_name, first_name, sur_name, phone_number, driver_license, experience, insurance_policy,
                 vehicle_passport):
        data = self.read()
        new_id = -1
        for entity in data:
            new_id = max(entity['id'])+1
            new_entity = {
                'driver_id': new_id,
                'last_name': last_name,
                'first_name': first_name,
                'sur_name': sur_name,
                'phone_number': phone_number,
                'driver_license': driver_license,
                'experience': experience,
                'insurance_policy': insurance_policy,
                'vehicle_passport': vehicle_passport
            }
            data.append(new_entity)
            self.write(data)
#g
    def replace_elem(self, id, last_name, first_name, sur_name, phone_number, driver_license, experience, insurance_policy,
                 vehicle_passport):
        data = self.read()
        entity = self.get_entity_id(id)
        if last_name:
            entity['last_name']=last_name,
        if first_name:
            entity['first_name'] = first_name,
        if sur_name:
            entity['sur_name']=sur_name,
        if phone_number:
            entity['phone_number'] = phone_number,
        if driver_license:
            entity['driver_license'] = driver_license,
        if experience:
            entity['experience'] = experience,
        if insurance_policy:
            entity['insurance_policy'] = insurance_policy,
        if vehicle_passport:
            entity['vehicle_passport'] = vehicle_passport
        self.write(data)

#h
    def del_elem(self, id):
        data = self.read()
        entity = self.get_entity_id(id)
        data.remove(entity)
        self.write(data)

#i
    def get_count(self):
        data = self.read()
        return len(data)
