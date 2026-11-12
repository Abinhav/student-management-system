from pydantic import BaseModel, Field, ConfigDict, EmailStr

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)
    email: EmailStr
    course: str = Field(min_length=2, max_length=100)

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
    course: str

    model_config = ConfigDict(from_attributes=True)