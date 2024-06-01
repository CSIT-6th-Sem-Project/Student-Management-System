from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field
from typing import List

from api.schemas.base import MBase


class CourseModel(MBase):
	
	name: str = Field(...)
	model_config = ConfigDict(

		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example":{
				"id": "665ab84a5ad9a098cee6257a",
				"name":"Bsc.CSIT"
			}
		}
)
	


class UpdateCourseModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    name:str
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "name": "BIM",
            }
        },
    )

	
class CourseCollection(BaseModel):
    courses: List[CourseModel]