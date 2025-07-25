from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
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

# , 'allergies': ['pollen', 'dust']
patient_info = {'name':"Binod", 'age': '20', 'weight': 143, 'married': True, 'contact_details': {'mobile': '12432222', 'email':'abc@gmail.com'}}
patient1 = Patient(**patient_info)

update_patient_name(patient1)


