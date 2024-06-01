from bson import ObjectId
from fastapi import Body
from pymongo import ReturnDocument


from api.db.dbconnection import (db)
from api.schemas.subject import *

class SubjectOperation:
     
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
                    'from': 'teacher',
                    'localField': 'teacher',
                    'foreignField': '_id',
                    'as': 'teacher'
                }
            },
            {
                '$unwind': {
                    'path': '$teacher',
                    'preserveNullAndEmptyArrays': True
                }
            },
            {
                '$lookup': {
                    'from': 'course',
                    'localField': 'teacher.course',
                    'foreignField': '_id',
                    'as': 'teacher.course'
                }
            },
            {
                '$unwind': {
                    'path': '$teacher.course',
                    'preserveNullAndEmptyArrays': True
                }
            },
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    'name': 1,
                    'course.id': {'$toString': '$course._id'},
                    'course.name': '$course.name',
                    'teacher.id': {'$toString': '$teacher._id'},
                    'teacher.first_name': '$teacher.first_name',
                    'teacher.last_name': '$teacher.last_name',
                    'teacher.email': '$teacher.email',
                    'teacher.gender': '$teacher.gender',
                    'teacher.address': '$teacher.address',
                    'teacher.course.id': {'$toString': '$teacher.course._id'},
                    'teacher.course.name': '$teacher.course.name'
                }
            }
        ]
   
    def __init__(self,*args,**kwargs):
        self.__collection = db.get_collection("subject")
        assert self.__collection is not None, "[!] subject collection object cannot be none"

    async def list(self,limit:int = 1000) -> SubjectCollection:
        """
            fetch all the subjects
        """
        return SubjectCollection(teachers= await self.__collection.aggregate(self.pipeline).to_list(limit))
    
    
    async def fetch_one(self,id:str) -> SubjectModel | None:
        """
            fetch one session from collection
        """
        find_one_pipeline = self.pipeline.copy()
        find_one_pipeline.insert(0,{'$match': {'_id': ObjectId(id)}})

        subject = await self.__collection.aggregate(find_one_pipeline).to_list(None)
        if subject:
            return subject[0]
        return None
    
    async def create_one(self,subject: InsertSubjectModel = Body(...)) -> SubjectModel | None:
        """
            create a subject
        """
        new_subject = {} 
        for k,v in subject.model_dump(by_alias=True,exclude=["id"]).items():
            if k.__eq__("course") or k.__eq__("teacher"):
                new_subject[k] = ObjectId(v)
            else:
                new_subject[k] = v

        
        new_subject = await self.__collection.insert_one(new_subject)

        created_subject = await self.fetch_one(id = str(new_subject.inserted_id))

        return created_subject

    async def delete_one(self,id: str) -> int:
        """
            delete a subject
        """
        deleted_items = await self.__collection.delete_one({"_id":ObjectId(id)})
        
        return deleted_items.deleted_count
    
    async def update_one(self,id:str,subject: UpdateSubjectModel = Body(...)) -> SubjectModel | None:
        """
            update a subject
        """
        subject_dict = {}
    
        for k, v in subject.model_dump(by_alias=True).items():
            if v is not None:
                if k.__eq__("course") or k.__eq__("teacher"):
                    subject_dict[k] = ObjectId(v)
                else:
                    subject_dict[k] = v

        if len(subject_dict) >= 1:
            updated_result = await self.__collection.find_one_and_update(
                 {"_id": ObjectId(id)},
                 {"$set": subject_dict},
                 return_document=ReturnDocument.AFTER,
                 )
            return updated_result
        else:
            return self.fetch_one(id=id)
        

    # Singleton architecture
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SubjectOperation, cls).__new__(cls)
        return cls.instance
    
    @classmethod
    def get_connection(cls):
        return cls()