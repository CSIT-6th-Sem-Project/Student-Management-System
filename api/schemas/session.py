from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field

from api.schemas.base import MBase

class SessionModel(MBase):
	start_year: str = Field(...)
	end_year: str = Field(...)

	model_config = ConfigDict(
		populate_by_name=True,
		arbitrary_types_allowed=True,
		json_schema_extra={
			"example":{
			"start_year":"2024-01-22",
			"end_year":"2024-12-22"
		}
		}
	)

class UpdateSessionModel(BaseModel):
	start_year: Optional[str] = None
	end_year: Optional[str] = None

	model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": 
				{
                	"start_year": "2024-01-02",
					"end_year": "2024-12-24"
				},
        },
    )

class SessionCollection(BaseModel):
    sessions: List[SessionModel]
