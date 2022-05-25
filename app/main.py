import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from fastapi import FastAPI

from app.resources import item, people

app = FastAPI(description="Test Prisma ORM with FastAPI")

item.init_app(app=app)
people.init_app(app=app)
