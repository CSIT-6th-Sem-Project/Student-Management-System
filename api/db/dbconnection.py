import motor
import motor.motor_asyncio

DB_URL = "mongodb://localhost:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)

db = client.get_database("StudentManagementDB")


