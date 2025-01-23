from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument

from pydantic import BaseModel

from uuid import Uuuid4

class ListSummary(BaseModel):
    id:str
    name: str