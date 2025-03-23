import os
from fastapi import FastAPI
import motor.motor_asyncio
from bson import ObjectId

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo_admin:password@mongo_db:27017")


