from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, EmailStr

from api.schemas.base import MBase,PyObjectId

from api.schemas.course import CourseModel
from api.schemas.session import SessionModel


class StudentBaseModel(MBase):
	first_name: str = Field(...) 
	last_name: str = Field(...)
	email: EmailStr = Field(...) 
	gender: str = Field(...)
	address: str = Field(...)

class StudentModel(StudentBaseModel):

	course: CourseModel = Field(...)
	session: SessionModel = Field(...)
	
	model_config = ConfigDict(
		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example": {
				"first_name":"Narotsit",
				"last_name":"Karki",
				"email":"narotsitk@oic.edu.np",
				"gender": "M",
				"address":"Baluwatar, Kathmandu",
				"course": CourseModel.model_config.get("json_schema_extra").get("example"),
				"session": SessionModel.model_config.get("json_schema_extra").get("example")
			}
		}
		)
	
class InsertStudentModel(StudentBaseModel):
	course:PyObjectId = Field(...)
	session:PyObjectId = Field(...)

	model_config = ConfigDict(
		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example": {
				"first_name":"Narotsit",
				"last_name":"Karki",
				"email":"narotsitk@oic.edu.np",
				"gender": "M",
				"address":"Baluwatar,Kathmandu",
				"course": "6eg2sd2131ikl",
				"session": "6eg2sd2131ikl"
			}
		}
		)

class UpdateStudentModel(BaseModel):
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	email: Optional[EmailStr] = None
	gender: Optional[str] = None
	address: Optional[str] = None
	course: Optional[PyObjectId] = None
	session: Optional[PyObjectId] = None
	
	model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra = InsertStudentModel.model_config.get("json_schema_extra"),
    )
	
class StudentCollection(BaseModel):
    students: List[StudentModel]
	

