from pydantic import BaseModel, EmailStr,Field
from pydantic.functional_validators import BeforeValidator
from typing import List,Optional,Annotated

# from api.db.dbcollections import (CourseCollection)
PyObjectId = Annotated[str,BeforeValidator(str)]

class MBase(BaseModel):
	id: Optional[PyObjectId] = Field(alias="_id",default = None)



# class StudentBase(BaseModel):
# 	first_name: str 
# 	last_name: str 
# 	email: str 
# 	gender: str 
# 	address: str 
# 	course_id: str
# 	session_id: str

# class StudentCreate(StudentBase):
# 	pass

# class Student(Base,StudentBase):
	
# 	class Config:
# 		orm_mode = True





