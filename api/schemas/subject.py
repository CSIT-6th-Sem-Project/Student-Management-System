from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from api.schemas.base import MBase,PyObjectId
from api.schemas.course import CourseModel
from api.schemas.teacher import TeacherModel

class SubjectModel(MBase):
    name:str = Field(...)
    # course:PyObjectId = Field(...)
    # teacher:PyObjectId = Field(...)
    course: CourseModel
    teacher: TeacherModel
    
    model_config = ConfigDict(
		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example": {
                "id":"665ad42f5ad9a098cee6257c",
				"name":"Advanced DataBase",
				"course":CourseModel.model_config.get("json_schema_extra").get("example"),
                "teacher":TeacherModel.model_config.get("json_schema_extra").get("example")
			}
		}
	)

class InsertSubjectModel(BaseModel):
    name:str = Field(...)
    course: PyObjectId = Field(...)
    teacher: PyObjectId = Field(...)

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_schema_extra={
            "example":{
                "name":"Advanced DataBase",
                "course":"665ab84a5ad9a098cee6257a",
                "teacher":"665ad42f5ad9a098cee6257c"
            }
        }
    )
class UpdateSubjectModel(BaseModel):
    name: Optional[str] = None
    course: Optional[PyObjectId] = None
    teacher: Optional[PyObjectId] = None
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra = SubjectModel.model_config.get("json_schema_extra"),
    )

class SubjectCollection(BaseModel):
    teachers: List[SubjectModel]