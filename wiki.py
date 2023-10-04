from fastapi import FastAPI, Query
import wikipedia
from datasets import Dataset, load_dataset
import uvicorn
import os
import json

app = FastAPI()
