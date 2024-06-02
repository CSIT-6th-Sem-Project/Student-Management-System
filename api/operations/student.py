from bson import ObjectId
from fastapi import Body
from pymongo import ReturnDocument


from api.db.dbconnection import (db)
from api.schemas.student import *

class StudentOperation:
    

    pipeline = [
    
            {
                '$lookup': {
                    'from': 'course',
                    'localField': 'course',
                    'foreignField': '_id',
                    'as': 'course'
                }
            },
            {
                '$unwind': {
                    'path': '$course',
                    'preserveNullAndEmptyArrays': True
                }
            },
            {
                '$lookup': {
                    'from': 'session',
                    'localField': 'session',
                    'foreignField': '_id',
                    'as': 'session'
                }
            },
            {
                '$unwind': {
                    'path': '$session',
                    'preserveNullAndEmptyArrays': True
                }
            },
   
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    'first_name': 1,
                    'last_name':1,
                    'email': 1,
                    'gender': 1,
                    'address':1,
                    'course.id': {'$toString': '$course._id'},
                    'course.name': '$course.name',

                    'session.id': {'$toString': '$session._id'},
                    'session.start_year': '$session.start_year',
                    'session.end_year': "$session.end_year"
                }
            }
        ]
   
    def __init__(self,*args,**kwargs):
        self.__collection = db.get_collection("student")
        assert self.__collection is not None, "[!] student collection object cannot be none"

    async def list(self,limit:int = 1000) -> StudentCollection:
        """
            fetch all the students
        """
        return StudentCollection(students= await self.__collection.aggregate(self.pipeline).to_list(limit))
    
    
    async def fetch_one(self,id:str) -> StudentModel | None:
        """
            fetch one students from collection
        """
        find_one_pipeline = self.pipeline.copy()
        find_one_pipeline.insert(0,{'$match': {'_id': ObjectId(id)}})
        
        subject = await self.__collection.aggregate(find_one_pipeline).to_list(None)
        if subject:
            return subject[0]
        
        return None
    
    async def create_one(self,student: InsertStudentModel = Body(...)) -> StudentModel | None:
        """
            create a students  
        """
        new_student = {} 
        for k,v in student.model_dump(by_alias=True,exclude=["id"]).items():
            if k.__eq__("course") or k.__eq__("session"):
                new_student[k] = ObjectId(v)
            else:
                new_student[k] = v

        
        new_student = await self.__collection.insert_one(new_student)

        created_student = await self.fetch_one(id = str(new_student.inserted_id))

        return created_student

    async def delete_one(self,id: str) -> int:
        """
            delete a student
        """
        deleted_items = await self.__collection.delete_one({"_id":ObjectId(id)})
        
        return deleted_items.deleted_count
    
    async def update_one(self,id:str,student: UpdateStudentModel = Body(...)) -> StudentModel | None:
        """
            update a student
        """
        student_dict = {}
    
        for k, v in student.model_dump(by_alias=True).items():
            if v is not None:
                if k.__eq__("course") or k.__eq__("sesssion"):
                    student_dict[k] = ObjectId(v)
                else:
                    student_dict[k] = v

        if len(student_dict) >= 1:
            updated_result = await self.__collection.find_one_and_update(
                 {"_id": ObjectId(id)},
                 {"$set": student_dict},
                 return_document=ReturnDocument.AFTER,
                 )
            return await self.fetch_one(id=str(updated_result["_id"]))
        else:
            return await self.fetch_one(id=id)
        

    # Singleton architecture
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(StudentOperation, cls).__new__(cls)
        return cls.instance
    
    @classmethod
    def get_connection(cls):
        return cls()