from typing import Optional, Literal

from pydantic import BaseModel, EmailStr, Field

# Pydantic features.
# 1. Basic
# 2. Default values
# 3. Optional fields
# 4. Coerce
# 5. Builtin validation
# 6. Field Function - default values, constraints, description, regex
# 7. Return pydantic object dict/json



class Student(BaseModel):
    first_name: str
    middle_name: Optional[str] = None # Optional
    age: int = 10 # default value
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing CGPA')

student_dict = {'first_name': 'Prashanth'}
# student_dict = {'name': 32} - Error out, Pydantic is able to validate the data, unlike TypedDic which accepetd this.
student_dict = {'first_name': 'Prashanth', 'age': '30'} # If you look at the output it wont be shown in strings unlike TypedDict, instead it will coerce to int automatically.
student_dict = {'first_name': 'Prashanth', 'age': '30', 'email': "abc"} # If you look at the output it says value is not a valid email address: An email address must have an @-sig. This is Builtin validation
student_dict = {'first_name': 'Prashanth', 'age': '30', 'email': "abc@gmail.com", "cgpa": "12"} # If you look at the output it says Input should be less than 10. This is Field validation
student_dict = {'first_name': 'Prashanth', 'age': '30', 'email': "abc@gmail.com"} # If you look at the output it has cgpa. This is Field validations default feature

student = Student(**student_dict)

print(type(student))
print(student)
# Convert to Dict type
stud_dict = dict(student)
print(stud_dict['age'])
#Convert to Json
print(student.model_dump_json())