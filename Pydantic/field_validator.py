from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['unt.com', 'uta.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def name_upper(cls, value):
        return value.upper()
        
        
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
patient_info = {'name':"Binod", 'age': 12, 'email': "abc@unt.com", 'weight': 143, 'allergies': ['pollen', 'dust', 'A'], 'married': True, 'contact_details': {'mobile': '12432222', 'email':'abc@gmail.com'}}
patient1 = Patient(**patient_info)

update_patient_name(patient1)