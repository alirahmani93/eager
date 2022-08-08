from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
    list_students,

)

from server.models.student import (
    UpdateStudentModel,
    studentSchema,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()


@router.post("/c", response_description="ADD student")
async def add_student_data(student: studentSchema = Body(...)):
    stu = jsonable_encoder((student))
    new_student = await add_student((stu))
    return ResponseModel(new_student, "added successfily")


@router.get("/all", response_description="ALL Student", tags=["list_all"])
async def get_list():
    all_stu = await retrieve_students()
    if all_stu:
        return ResponseModel(all_stu, "see them")
    return ResponseModel(all_stu, "You are sarekari")


@router.get("/stu/{id}", response_description="Spacial STUDEnT")
async def select_student(id: str):
    target_student = await retrieve_student(id)
    if target_student:
        return ResponseModel(target_student, "inam az hamooni k mikhasti")
    return ErrorResponseModel("!!! BOOOM !!!", 404, "nadarim ini k migi ro")


@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )
