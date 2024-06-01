from pydantic import BaseModel, EmailStr,Field
from pydantic.functional_validators import BeforeValidator
from typing import List,Optional,Annotated

# from api.db.dbcollections import (CourseCollection)
PyObjectId = Annotated[str,BeforeValidator(str)]

class MBase(BaseModel):
	id: Optional[PyObjectId] = Field(alias="_id",default = None)





# class SubjectBase(BaseModel):
# 	name: str 
# 	course_id: str 
# 	teacher_id: str

# class SubjectCreate(SubjectBase):
# 	pass

# class Subject(Base,SubjectBase):

# 	class Config:
# 		orm_mode = True 

# class CourseBase(BaseModel):
# 	name: str

# class CourseCreate(CourseBase):
# 	pass

# class Course(Base,CourseBase):
# 	name: str
# 	subjects: List[Teacher]
# 	teachers: List[Subject]

# 	class Config:
# 		orm_mode = True



# class SessionBase(BaseModel):
# 	start_year: str
# 	end_year: str

# class SessionCreate(SessionBase):
# 	pass

# class Session(Base,SessionBase):
	
# 	class Config:
# 		orm_mode = True


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





