from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()


conn = MongoClient("mongodb+srv://acharyasmarika56_db_user:hello06677827@cluster0.tlutr1d.mongodb.net/")






