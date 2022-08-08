from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from fastapi.logger import logger


class studentSchema(BaseModel):
    full_name: str = Field(...)
    email: str = Field(...)
    # email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: int = Field(..., le=9)
    phone: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "ali rahmani",
                "email": "ali@test.com",
                "course_of_study": "water resource engineering",
                "year": "2",
                "gpa": "3.3",
                "phone": "12345"
            }
        }


class UpdateStudentModel(BaseModel):
    full_name: Optional[str]
    email: Optional[str]
    # email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[int]
    phone: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "full_name": "ashkan divband",
                "email": "ashkan@test.com",
                "course_of_study": "water resource engineering",
                "year": "8",
                "gpa": "2.1",
                "phone": "98765"
            }
        }


def ResponseModel(data, message) -> dict:
    return {"data": [data],
            "code": 200,
            "message": message,
            # "logger":logger
            }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
