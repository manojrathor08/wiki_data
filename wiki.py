from fastapi import FastAPI, Query
import wikipedia
from datasets import Dataset, load_dataset
import uvicorn
import os
import json

app = FastAPI()
# Initialize the counter by loading it from a file or default to 0 if the file doesn't exist

try:
  with open('counter.txt','r') as counter_file:
    counter = int(counter_file.read())
except FileNotFoundError:
  counter =0
# Specify the output file path for the HuggingFae dataset
file_path = "wiki_huggingface.json"
def append_dataset(data):
  # Check if the dataset file already exists
  if os.path.isfile(file_path):
    # Load the existing dataset
    with open(file_path,"r") as json_file:
      dataset = json.load(json_file)
    combined_id = dataset['id']+data['id']
    combined_title = dataset['title']+ data['tile']
    combined_text = dataset['text']+data['text']
    # Create a new dataset by combining the fields
    dataset = {'id':combined_id,
              'title':combined_title,
              'text':combined_text,}
  else:
    dataset = data
  with open(file_path,'w') as json_file:
    json.dump(dataset,json_file,indent = 4)

@app.get("/wiki/")
def get and save_wikipedia_summary(title:str = Query(...,description='wikipedia_title'),length:int=Query(10, description='Summary length')):
  global counter # Access the counter variable defined outside the function
  summary = wikipedia.summary(title,length)
  if summary is None:
    return {'message':'Invalid Wikipedia title'}
    # Increment the counter to create a unique ID
counter+=1
# COnvert input data into HuggingFace data dict format
data = {'id':[counter],
       'title':[title],
       'text':[summary]
       }
# Append the new  data to the Hugging Face dataset
append_dataset(data)
# Save the updated counter back to the file
with open('counter.txt','w') as counter_file:
  counter_file.write(str(counter))

@app.get("retrieve")
def retrieve_datasets():
  try:
    print('Loading th saved data')
    with open(file_path,'r') as json_file:
      saved_dataset = json.laod(json_file)
  except FileNotFoundError:
    saved_dataset = {"id":[],"title":[],"text":[]}
  return saved_dataset
if __name__ =="__main__":
  uvicorn.run(app,host="0.0.0.0",port = 8000)


    
    
