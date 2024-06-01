from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from api.schemas.base import MBase,PyObjectId
from api.schemas.course import CourseModel

class TeacherBaseModel(MBase):
	first_name:str = Field(...)
	last_name:str = Field(...)
	email:EmailStr = Field(...)
	gender:str = Field(...)
	address:str = Field(...)
	

class TeacherModel(TeacherBaseModel):
	# first_name:str = Field(...)
	# last_name:str = Field(...)
	# email:EmailStr = Field(...)
	# gender:str = Field(...)
	# address:str = Field(...)
	course: CourseModel

	model_config = ConfigDict(
		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example": {
				"first_name":"Dhiraj",
				"last_name":"Jha",
				"email":"dhirajcsit@oic.edu.np",
				"gender": "M",
				"address":"Gaushala,Kathmandu",
				"course": CourseModel.model_config.get("json_schema_extra").get("example"),
				# "course":"987a7ad18adjk91"
			}
		}
		)

class InsertTeacherModel(TeacherBaseModel):
	course:PyObjectId = Field(...)

	model_config = ConfigDict(
		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example": {
				"first_name":"Dhiraj",
				"last_name":"Jha",
				"email":"dhirajcsit@oic.edu.np",
				"gender": "M",
				"address":"Gaushala,Kathmandu",
				"course": "6eg2sd2131ikl",
			}
		}
		)

class UpdateTeacherModel(BaseModel):
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	email: Optional[EmailStr] = None
	gender: Optional[str] = None
	address: Optional[str] = None
	course: Optional[PyObjectId] = None
	
	model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra = InsertTeacherModel.model_config.get("json_schema_extra"),
    )
	
class TeacherCollection(BaseModel):
    teachers: List[TeacherModel]