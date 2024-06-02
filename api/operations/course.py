from bson import ObjectId
from fastapi import Body
from pymongo import ReturnDocument

from api.db.dbconnection import (db)
from api.schemas.course import *

class CourseOperation:
    
    def __init__(self,*args,**kwargs):
        self.__collection = db.get_collection("course")
        assert self.__collection is not None, "[!] course collection object cannot be none"

    async def list(self,limit:int = 1000) -> CourseCollection:
        """
            fetch all the courses
        """
        return CourseCollection(courses = await self.__collection.find().to_list(limit))
    
    async def fetch_one(self,id:str) -> CourseModel | None:
         """
            fetch one course from collection
         """
         if (course := await self.__collection.find_one({"_id": ObjectId(id)})) is not None:
             return course
         
         return None
    
    async def create_one(self,course: CourseModel = Body(...)) -> CourseModel | None:
        """
            create a course
        """
        new_course = await self.__collection.insert_one(
            course.model_dump(by_alias=True,exclude=["id"])
        )

        created_course = await self.fetch_one(id = str(new_course.inserted_id))

        return created_course

    async def delete_one(self,id: str) -> int:
        """
            delete a course
        """
        deleted_items = await self.__collection.delete_one({"_id":ObjectId(id)})
        return deleted_items.deleted_count
    
    async def update_one(self,id:str,course: UpdateCourseModel = Body(...)) -> CourseModel | None:
        """
            update a course
        """
        course = {
            k: v for k, v in course.model_dump(by_alias=True).items() if v is not None
        }
        if len(course) >= 1:
            updated_result = await self.__collection.find_one_and_update(
                 {"_id": ObjectId(id)},
                 {"$set": course},
                 return_document=ReturnDocument.AFTER,
                 )
            return updated_result
        else:
            return await self.fetch_one(id=id)
        

    # Singleton architecture
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseOperation, cls).__new__(cls)
        return cls.instance
    
    @classmethod
    def get_connection(cls):
        return cls()
