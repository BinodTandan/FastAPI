from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zipCode: str
class Pateint(BaseModel):
    name:str
    age: int
    gender: str
    address: Address
    
address_dict = {'city': 'Little Elm', 'state': 'TX', 'zipCode': '76227'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Binod', 'age': 27, 'gender': 'male', 'address': address1}

patient1 = Pateint(**patient_dict)

print(patient1)