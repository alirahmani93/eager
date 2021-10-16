from typing import Union
from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

students_collection = database.get_collection("students_collection")


# helpers

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "gpa": student["gpa"],
        "phone": student["phone"]
    }


# Retrieve all students in the Database
async def retrieve_students():
    students = []
    async for student in students_collection.find():
        students.append(student_helper(student))

    return students


# Add a new student to the database
async def add_student(student_data: dict) ->dict:
    student = await students_collection.insert_one(student_data)
    new_student = await  students_collection.find_one({"id": student.inserted_id})

    return student_helper(new_student)


# Retrieve student with ID
async def retrieve_student(id: str) -> dict:
    student = await students_collection.find_one({"_id": ObjectId(id)})

    return student_helper(student)


# Update Student with ID
async def update_student(id: str, data: dict) -> Union[bool, str]:
    if len(data) < 1:
        return 'len(DATA) < 1'
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student:
        update = await students_collection.update_one({"_id": ObjectId(id), "$set": data})

        if update:
            return True

        return False
# Delete Student with ID
async def delete_student(id:str)-> Union[bool, str]:
    target_stu = await students_collection.find_one({"_id":ObjectId(id)})
    if target_stu:
        await students_collection.delete_one({"_id":ObjectId(id)})
        # await students_collection.delete_one(target_stu) # ???
        return True
    return "ID is Wrong"

# List all Student
def list_students():
    return students_collection