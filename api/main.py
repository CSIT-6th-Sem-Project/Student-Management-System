from fastapi import FastAPI

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
    }

]

app = FastAPI(title = "Student Management System",openapi_tags = tags_metadata)

@app.get("/",tags = ["base"])
async def root():

    return {"message":"Student Management System Project - 8th Sem Project"}

########### STUDENT CRUD OPERATION ############################

@app.get("/student/",tags = ["student"])
async def student():
    return {"message":"CRUD Student"}

@app.post("/student/add", tags = ["student"])
async def add_student():
    return {"message","Endpoint to add a new student"}

@app.post("/student/delete",tags = ["student"])
async def delete_student():
    return {"message","Endpoint to delete a student"}

@app.post("/student/update",tags = ["student"])
async def update_student():
    return {"message","Endpoint to update a student"}

########### COURSE CRUD OPERATION ############################

@app.get("/course/",tags = ["course"])
async def course():
    return {"message":"CRUD Course"}

@app.post("/course/add", tags = ["course"])
async def add_course():
    return {"message","Endpoint to add a new course"}

@app.post("/course/delete",tags = ["course"])
async def delete_course():
    return {"message","Endpoint to delete a course"}

@app.post("/course/update",tags = ["course"])
async def update_course():
    return {"message","Endpoint to update a course"}


########### SESSION CRUD OPERATION #########################

@app.get("/session/",tags = ["session"])
async def session():
    return {"message":"CRUD Session"}


@app.post("/session/add", tags = ["session"])
async def add_session():
    return {"message","Endpoint to add a new session"}

@app.post("/session/delete",tags = ["session"])
async def delete_session():
    return {"message","Endpoint to delete a session"}

@app.post("/session/update",tags = ["session"])
async def update_session():
    return {"message","Endpoint to update a session"}

########### TEACHER CRUD OPERATION #########################

@app.get("/teacher/",tags = ["teacher"])
async def teacher():
    return {"message":"CRUD Teacher"}


@app.post("/teacher/add", tags = ["teacher"])
async def add_teacher():
    return {"message","Endpoint to add a new session"}

@app.post("/teacher/delete",tags = ["teacher"])
async def delete_teacher():
    return {"message","Endpoint to delete a teacher"}

@app.post("/teacher/update",tags = ["teacher"])
async def update_teacher():
    return {"message","Endpoint to update a teacher"}


