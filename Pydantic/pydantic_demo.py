from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
def insert_patient_name(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')


def update_patient_name(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')


patient_info = {'name':"Binod", 'age': '20', 'weight': 143, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'mobile': '12432222', 'email':'abc@gmail.com'}}
patient1 = Patient(**patient_info)

update_patient_name(patient1)


