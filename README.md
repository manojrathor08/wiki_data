# FastAPI Wikipedia summary Scrapper 
This project uses FastAPI to get the summaries of the Wikipedia pages based on the user-provided titles and summary length. The summary is then converted into the Hugging Face dataset format.

## Project Structure
The project consists of the following components:
- 'wiki.py': This file contains the FastAPI code and includes two decorator functions:
  - '@app.get("/wiki/")': This function allows users to pass the Wikipedia title and summary length as a query and retrieve the summary.
  - '@app.get("/retrieve")': This function retrieves the saved dataset.
- 'run_wiki.py': This Python script interacts with the FastAPI application to allow users to provide the Wikipedia title and summary length interactively. It makes a GET request to the FastAPI server.
- 'retrieve.py': Another Python script that makes a GET request to the FastAPI server to retrieve the saved JSON dataset.

## Usage 
### Running the FastAPI Application
To start the FastAPI application, use the following command in your project directory:
python3 wiki.py
The FastAPI application is now running and ready to accept requests.

### Scraping Wikipedia Summaries
To get the Wikipedia summaries and convert them into the HuggingFace dataset format, follow these steps:
Use run_wiki.py to provide the desired Wikipedia title and summary length interactively.

Run the script as follows
python3 run_wiki.py
The script will prompt the user to enter the Wikipedia title and summary length.

The summary data is then converted into the HuggingFae dataset format and saved. The summaries of the Wikipedia pages are saved in this format.

### Retrieving the Saved Dataset
To retrieve the saved dataset, use the retrieve.py script:
Run the script as follows:
python retrieve.py
This script makes  a GET request to the FastAPI server to retrieve the saved JSON dataset, which contains the Wikipedia page summaries in HuggingFace dataset format.

This allows users to interact with the FastAPI application, scrape and save Wikipedia page summaries, and retrieve them in JSON format saved in HuggingFae dataset format.
