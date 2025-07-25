from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=200, title="Name of a patient", description="Name must be less than 200 characters", 
                               example=['Binod','Rahul'])]
    age: int = Field(gt=0)
    email: EmailStr
    linkedIn: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is a patient married or Not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=3)]
    contact_details: Dict[str, str]

def update_patient_name(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.linkedIn)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

# , 'allergies': ['pollen', 'dust']
patient_info = {'name':"Binod", 'age': 12, 'email': "abc@gmail.com",'linkedIn':'http://linkedin.com/123', 'weight': 143, 'allergies': ['pollen', 'dust', 'A'], 'married': True, 'contact_details': {'mobile': '12432222', 'email':'abc@gmail.com'}}
patient1 = Patient(**patient_info)

update_patient_name(patient1)


