from bson import ObjectId
from fastapi import Body
from pymongo import ReturnDocument


from api.db.dbconnection import (db)
from api.schemas.teacher import *

class TeacherOperation:
    
    aggregate_pipeline = [
        { 
           "$lookup":{
                "from":"course",
                "localField":"course",
                "foreignField":"_id",
                "as":"course"
        }},
           {
               "$unwind":"$course"
        }
    ]

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
                '$project': {
                    '_id': {'$toString': '$_id'},
                    'first_name': 1,
                    'last_name': 1,
                    'email': 1,
                    'gender': 1,
                    'address': 1,
                    'course.id': {'$toString': '$course._id'},
                    'course.name': '$course.name',
                }
            }
        ]
   
    def __init__(self,*args,**kwargs):
        self.__collection = db.get_collection("teacher")
        assert self.__collection is not None, "[!] teacher collection object cannot be none"

    async def list(self,limit:int = 1000) -> TeacherCollection:
        """
            fetch all the teachers
        """
        return TeacherCollection(teachers= await self.__collection.aggregate(self.pipeline).to_list(limit))
    
        # return TeacherCollection(teachers = await self.__collection.find().to_list(limit))

    # async def list(self,limit:int = 1000) -> TeacherCollection:
    #     """
    #         fetch all the teachers
    #     """
    #     return TeacherCollection(teachers = await self.__collection.find().to_list(limit))
    
    async def fetch_one(self,id:str) -> TeacherModel | None:
        """
            fetch one session from collection
        """
        find_one_pipeline = self.pipeline.copy()
        find_one_pipeline.insert(0,{'$match': {'_id': ObjectId(id)}})
        # print(find_one_pipeline)
        teacher = await self.__collection.aggregate(find_one_pipeline).to_list(None)
        if teacher:
            return teacher[0]

        # single_aggregate_pipeline.append({ "$limit": 1 })

        # if (teacher := await self.__collection.find_one({"_id":ObjectId(id)})) is not None:
        #      return teacher
        
        return None
    
    async def create_one(self,teacher: InsertTeacherModel = Body(...)) -> TeacherModel | None:
        """
            create a teacher
        """
        new_teacher = {} 
        for k,v in teacher.model_dump(by_alias=True,exclude=["id"]).items():
            if k.__eq__("course"):
                new_teacher[k] = ObjectId(v)
            else:
                new_teacher[k] = v

        
        new_teacher = await self.__collection.insert_one(new_teacher)

        created_teacher = await self.fetch_one(id = str(new_teacher.inserted_id))

        return created_teacher

    async def delete_one(self,id: str) -> int:
        """
            delete a teacher
        """
        deleted_items = await self.__collection.delete_one({"_id":ObjectId(id)})
        
        return deleted_items.deleted_count
    
    async def update_one(self,id:str,teacher: UpdateTeacherModel = Body(...)) -> TeacherModel | None:
        """
            update a teacher
        """
        teacher_dict = {}
    
        for k, v in teacher.model_dump(by_alias=True).items():
            if v is not None:
                if k.__eq__("course"):
                    teacher_dict[k] = ObjectId(v)
                else:
                    teacher_dict[k] = v

        if len(teacher_dict) >= 1:
            updated_result = await self.__collection.find_one_and_update(
                 {"_id": ObjectId(id)},
                 {"$set": teacher_dict},
                 return_document=ReturnDocument.AFTER,
                 )
            return updated_result
        else:
            return self.fetch_one(id=id)
        

    # Singleton architecture
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TeacherOperation, cls).__new__(cls)
        return cls.instance
    
    @classmethod
    def get_connection(cls):
        return cls()