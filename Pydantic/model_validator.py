from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_number(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient above 60 must have emergency contact number')
        return model
        
        
def update_patient_name(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    # print(patient.linkedIn)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

# , 'allergies': ['pollen', 'dust']
patient_info = {'name':"Binod", 'age': 62, 'email': "abc@unt.com", 'weight': 143, 'allergies': ['pollen', 'dust', 'A'], 'married': True, 'contact_details': {'mobile': '12432222', 'email':'abc@gmail.com', 'emergency':'1234343'}}
patient1 = Patient(**patient_info)

update_patient_name(patient1)