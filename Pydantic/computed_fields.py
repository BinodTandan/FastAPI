from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field 
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: int
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
        
        
def update_patient_name(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    # print(patient.linkedIn)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI', patient.bmi)
    print('updated')

# , 'allergies': ['pollen', 'dust']
patient_info = {'name':"Binod", 'age': 62, 'email': "abc@unt.com", 'weight': 143,'height':167, 'allergies': ['pollen', 'dust', 'A'], 'married': True, 'contact_details': {'mobile': '12432222', 'email':'abc@gmail.com', 'emergency':'1234343'}}
patient1 = Patient(**patient_info)

update_patient_name(patient1)