from bson import ObjectId
from fastapi import Body
from pymongo import ReturnDocument

from api.db.dbconnection import (db)
from api.schemas.session import *

class SessionOperation:
    
    def __init__(self,*args,**kwargs):
        self.__collection = db.get_collection("session")
        assert self.__collection is not None, "[!] session collection object cannot be none"

    async def list(self,limit:int = 1000) -> SessionCollection:
        """
            fetch all the sessions
        """
        return SessionCollection(sessions = await self.__collection.find().to_list(limit))
    
    async def fetch_one(self,id:str) -> SessionModel | None:
         """
            fetch one session from collection
         """
         if (course := await self.__collection.find_one({"_id": ObjectId(id)})) is not None:
             return course
         
         return None
    
    async def create_one(self,session: SessionModel = Body(...)) -> SessionModel | None:
        """
            create a session
        """
        new_session = await self.__collection.insert_one(
            session.model_dump(by_alias=True,exclude=["id"])
        )

        created_session = await self.fetch_one(id = str(new_session.inserted_id))

        return created_session

    async def delete_one(self,id: str) -> int:
        """
            delete a session
        """
        deleted_items = await self.__collection.delete_one({"_id":ObjectId(id)})
        return deleted_items.deleted_count
    
    async def update_one(self,id:str,session: UpdateSessionModel = Body(...)) -> SessionModel | None:
        """
            update a session
        """
        session = {
            k: v for k, v in session.model_dump(by_alias=True).items() if v is not None
        }

        if len(session) >= 1:
            updated_result = await self.__collection.find_one_and_update(
                 {"_id": ObjectId(id)},
                 {"$set": session},
                 return_document=ReturnDocument.AFTER,
                 )
            return updated_result
        else:
            return self.fetch_one(id=id)
        

    # Singleton architecture
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SessionOperation, cls).__new__(cls)
        return cls.instance
    
    @classmethod
    def get_connection(cls):
        return cls()
    