# Reddit-Data-Pipeline-with-Airflow-Streamlit
Reddit Data Pipeline with Airflow &amp; Streamlit

## Component	Tool	Status
- Data Ingestion	Reddit API + Airflow DAG	✅ Done
- Data Storage	PostgreSQL (via Docker)	✅ Done
- Visualization	Streamlit Dashboard	✅ Done (simple)
- Dev Environment	Docker + Local Dev	✅ Smooth

## 🧠 Knowledges
- ETL/ELT pipelines
- work with Docker & Airflow
- Connect APIs, store in a DB, and build front-ends
- Communicate insights visually 

## dashboard streamlit:
![image](https://github.com/user-attachments/assets/13ff3d1b-68cf-4f1a-a55f-9aeb104f582b)

## How to use:
- download docker
- download or git clone this repo
- get your reddit api keys and put them in the daf file
- open a terminal and type:
    - docker-compose down
    - docker-compose up --build
-go to localhost:8080 for airglow ui
- activate the dag to fetch the reddit data
- go to the streamlit dashboard for the visualisation
