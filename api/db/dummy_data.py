from .schemas import *

import random
from faker import Faker
import os

fkr = Faker()

DATA_SIZE  = range(10)

GENDER = ["M","F"]

# SESSION_DATA = [

# 	Session(id = fkr.uuid4(), start_year = fkr.date(), end_year = fkr.date()) for _ in DATA_SIZE
# ]

# COURSE_DATA = [

# 	Course(id = fkr.uuid4() , name = fkr.bban()) for _ in DATA_SIZE
# ]


# TEACHER_DATA = [

# 	Teacher(id = fkr.uuid4(), first_name = fkr.first_name() ,
# 	 last_name = fkr.last_name(), gender = random.choice(GENDER),
# 	 email = fkr.email(), 
# 	 address = fkr.address(), course = random.choice(COURSE_DATA)) for _ in DATA_SIZE
# ]


# STUDENT_DATA = [

# 	Student(id = fkr.uuid4(), first_name = fkr.first_name(), last_name = fkr.last_name(), 
# 		email = fkr.email(), gender = random.choice(GENDER), address = fkr.address(),
# 		course = random.choice(COURSE_DATA), session = random.choice(SESSION_DATA) ) for _ in DATA_SIZE
# ]



# SUBJECT_DATA = [

# 	Subject(id = fkr.uuid4(), 
# 		name = fkr.bban(),
# 		course = random.choice(COURSE_DATA), 
# 		teacher = random.choice(TEACHER_DATA)) for _ in DATA_SIZE
# ]