from fastapi import Body, FastAPI , status, Depends, HTTPException,Response
from typing import Any


from api.schemas.session import *
from api.schemas.teacher import *
from api.schemas.course import *
from api.schemas.subject import *

from api.operations.session import (SessionOperation)
from api.operations.teacher import (TeacherOperation)
from api.operations.course import (CourseOperation)
from api.operations.subject import(SubjectOperation)


# from .dummy_data import (STUDENT_DATA, COURSE_DATA, SESSION_DATA, SUBJECT_DATA, TEACHER_DATA)

tags_metadata = [
    {
        "name":"base",
        "description":"Base api endpoint"
    },

    {
        "name": "student",
        "description": "CRUD operations with students",
    },

    {
        "name":"course",
        "description": "CRUD operations with course",
    },

    {
        "name":"session",
        "description": "CRUD operations with sessions",
    },

    {
        "name":"teacher",
        "description":"CRUD operations with teachers"
    },
    {
        "name": "subject",
        "description": "CRUD operations with subjects"
    }

]

app = FastAPI(title = "Student Management System",openapi_tags = tags_metadata, debug = True)

@app.get("/",tags = ["base"])
async def root():

    return {"message":"Student Management System Project - 8th Sem Project"}

########### STUDENT CRUD OPERATION ############################

# @app.get("/student/",tags = ["student"], response_model = list[Student])
# async def student() -> Any:
#     return STUDENT_DATA

# @app.get("/student/{id}", tags =["student"], response_model = Student)
# async def get_student_by_id(id:str):
#     return random.choice(STUDENT_DATA)

# @app.post("/student/add", tags = ["student"], status_code = status.HTTP_201_CREATED )
# async def add_student(student:StudentCreate):
#     return {"message","Endpoint to add a new student"}

# @app.post("/student/delete/{id}",tags = ["student"])
# async def _student(id:str):
#     return {"message","Endpoint to delete a student"}

# @app.put("/student/update/{id}",tags = ["student"], response_model = Student)
# async def update_student(id:str, student:Student):
#     return {"message","Endpoint to update a student"}

########### COURSE CRUD OPERATION ############################

@app.get("/course/",tags = ["course"], 
         response_model = CourseCollection, 
         response_description="List of all courses", 
         response_model_by_alias=False)
async def course(dbo: CourseOperation = Depends(CourseOperation.get_connection) ):
    return await dbo.list(limit = 10)


@app.get("/course/{id}", tags = ["course"], 
         response_model = CourseModel, 
         response_description= "Fetch a single course",
         response_model_by_alias=False,)
async def get_course_by_id(id:str,
                           dbo: CourseOperation = Depends(CourseOperation.get_connection)):
    course = await dbo.fetch_one(id = id)

    if course is not None:
        return course
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Course with id: {id} not found")
    

@app.post("/course/add" 
          ,tags = ["course"],
          response_model = CourseModel,
          response_description= "Add a single course",
          status_code = status.HTTP_201_CREATED,
          response_model_by_alias= False)
async def add_course(course: CourseModel = Body(...), 
                     dbo:CourseOperation = Depends(CourseOperation.get_connection)):
    created_course = await dbo.create_one(course=course)
    
    if created_course:
        return created_course
    
    raise HTTPException(status_code=500, detail= "New course couldn't be added")

@app.put("/course/update/{id}",
         tags=["course"],
         response_description="Update a course",
         response_model_by_alias= False,
         response_model= CourseModel)
async def update_course(id:str,course: UpdateCourseModel=Body(...), 
                        dbo: CourseOperation = Depends(CourseOperation.get_connection)):
    updated_course = await dbo.update_one(id = id, course = course)

    if updated_course is not None:
        return updated_course
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id: {id} not found")

@app.delete("/course/delete/{id}",
          tags = ["course"],
          response_description="Delete a single course")
async def delete_course(id:str, 
                        dbo: CourseOperation = Depends(CourseOperation.get_connection)):
    deleted_items_count = await dbo.delete_one(id)

    if deleted_items_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Course with id: {id} not found")

########### SESSION CRUD OPERATION #########################

@app.get("/session/",tags = ["session"], 
         response_model = SessionCollection, 
         response_description="List of all session", 
         response_model_by_alias=False)
async def session(dbo: SessionOperation = Depends(SessionOperation.get_connection) ):
    return await dbo.list(limit = 10)


@app.get("/session/{id}", tags = ["session"], 
         response_model = SessionModel, 
         response_description= "Fetch a single session",
         response_model_by_alias=False,)
async def get_session_by_id(id:str,
                           dbo: SessionOperation = Depends(SessionOperation.get_connection)):
    session = await dbo.fetch_one(id = id)

    if session is not None:
        return session
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Session with id: {id} not found")
    

@app.post("/session/add" 
          ,tags = ["session"],
          response_model = SessionModel,
          response_description= "Add a single session",
          status_code = status.HTTP_201_CREATED,
          response_model_by_alias= False)
async def add_session(session: SessionModel = Body(...), 
                     dbo:SessionOperation = Depends(SessionOperation.get_connection)):
    created_session = await dbo.create_one(session=session)
    
    if created_session:
        return created_session
    
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= "New session couldn't be added")

@app.put("/session/update/{id}",
         tags=["session"],
         response_description="Update a session",
         response_model_by_alias= False,
         response_model= SessionModel)
async def update_session(id:str,session: UpdateSessionModel =Body(...), 
                        dbo:SessionOperation = Depends(SessionOperation.get_connection)):
    
    updated_session = await dbo.update_one(id = id, session = session)

    if updated_session is not None:
        return updated_session
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Session with id: {id} not found")

@app.delete("/session/delete/{id}",
          tags = ["session"],
          response_description="Delete a single session")
async def delete_course(id:str, 
                        dbo: SessionOperation = Depends(SessionOperation.get_connection)):
    deleted_items_count = await dbo.delete_one(id)

    if deleted_items_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Session with id: {id} not found")

########### TEACHER CRUD OPERATION #########################
@app.get("/teacher/",tags = ["teacher"], 
         response_model = TeacherCollection, 
         response_description="List of all teachers", 
         response_model_by_alias=False)
async def teacher(dbo: TeacherOperation = Depends(TeacherOperation.get_connection) ):

    return await dbo.list(limit=10)

@app.get("/teacher/{id}", tags = ["teacher"], 
         response_model = TeacherModel, 
         response_description= "Fetch a single teacher",
         response_model_by_alias=False,)
async def get_teacher_by_id(id:str,
                           dbo: TeacherOperation = Depends(TeacherOperation.get_connection)):
    teacher = await dbo.fetch_one(id = id)

    if teacher is not None:
        return teacher
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Teacher with id: {id} not found")

@app.post("/teacher/add" 
          ,tags = ["teacher"],
          response_model = TeacherModel,
          response_description= "Add a single teacher",
          status_code = status.HTTP_201_CREATED,
          response_model_by_alias= False)
async def add_teacher(teacher: InsertTeacherModel = Body(...), 
                     dbo:TeacherOperation = Depends(TeacherOperation.get_connection)):
    created_teacher = await dbo.create_one(teacher=teacher)
    
    if created_teacher:
        return created_teacher
    
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= "New session couldn't be added")


@app.put("/teacher/update/{id}",
         tags=["teacher"],
         response_description="Update a teacher",
         response_model_by_alias= False,
         response_model= TeacherModel)
async def update_teacher(id:str,teacher: UpdateTeacherModel=Body(...), 
                        dbo:TeacherOperation = Depends(TeacherOperation.get_connection)):
    
    updated_teacher = await dbo.update_one(id=id,teacher=teacher)

    if updated_teacher is not None:
        return updated_teacher
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Teacher with id: {id} not found")


@app.delete("/teacher/delete/{id}",
          tags = ["teacher"],
          response_description="Delete a single teacher")
async def delete_course(id:str, 
                        dbo: TeacherOperation = Depends(TeacherOperation.get_connection)):
    deleted_items_count = await dbo.delete_one(id=id)

    if deleted_items_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Teacher with id: {id} not found")

########### Subject CRUD OPERATION #########################
@app.get("/subject/",tags = ["subject"], 
         response_model = SubjectCollection, 
         response_description="List of all subjects", 
         response_model_by_alias=False)
async def subject(dbo: SubjectOperation = Depends(SubjectOperation.get_connection) ):
    
    return await dbo.list(limit=10)

@app.get("/subject/{id}", tags = ["subject"], 
         response_model = SubjectModel, 
         response_description= "Fetch a single subject",
         response_model_by_alias=False,)
async def get_subject_by_id(id:str,
                           dbo: SubjectOperation = Depends(SubjectOperation.get_connection)):
    subject = await dbo.fetch_one(id = id)

    if subject is not None:
        return subject
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Subject with id: {id} not found")

@app.post("/subject/add" 
          ,tags = ["subject"],
          response_model = SubjectModel,
          response_description= "Add a single subject",
          status_code = status.HTTP_201_CREATED,
          response_model_by_alias= False)
async def add_subject(teacher: InsertSubjectModel = Body(...), 
                     dbo:SubjectOperation = Depends(SubjectOperation.get_connection)):
    created_subject = await dbo.create_one(teacher=teacher)
    
    if created_subject:
        return created_subject
    
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= "New subject couldn't be added")


@app.put("/subject/update/{id}",
         tags=["subject"],
         response_description="Update a subject",
         response_model_by_alias= False,
         response_model= SubjectModel)
async def update_subject(id:str,subject: UpdateSubjectModel=Body(...), 
                        dbo:SubjectOperation = Depends(SubjectOperation.get_connection)):
    
    updated_subject = await dbo.update_one(id=id,teacher=teacher)

    if updated_subject is not None:
        return updated_subject
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Subject with id: {id} not found")


@app.delete("/subject/delete/{id}",
          tags = ["teacher"],
          response_description="Delete a single subject")
async def delete_subject(id:str, 
                        dbo: SubjectOperation = Depends(SubjectOperation.get_connection)):
    deleted_items_count = await dbo.delete_one(id=id)

    if deleted_items_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Subject with id: {id} not found")
