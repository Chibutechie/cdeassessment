# Dockerized Python ETL Pipeline

This project demonstrates a fully Dockerized **Python ETL pipeline** connected to a **PostgreSQL database**. The pipeline extracts data, transforms it, and loads it into a Postgres database. Everything is orchestrated using a bash script, without relying on Docker Compose.

---

## Table of Contents

* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)
* [Running the Pipeline](#running-the-pipeline)
* [How It Works](#how-it-works)
* [Cleaning Up](#cleaning-up)
* [Notes](#notes)

---

## Project Structure

All ETL-related files are inside the `etl/` directory:

```
.
├── README.md
└── etl
    ├── Dockerfile         
    ├── extract.py          
    ├── transform.py         
    ├── load.py              
    ├── main.py             
    ├── requirements.txt    
    └── run.sh            
```

---

## Prerequisites

Make sure you have the following installed:

* [Docker](https://docs.docker.com/get-docker/)
* Bash shell (Linux/Mac) or WSL2 (Windows)

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone <YOUR_REPO_URL>
cd <REPO_NAME>/etl
```

2. **Create a `.env` file** in the `etl/` directory with the following content:

```bash
# Postgres configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=024899
POSTGRES_DB=data_bank

# ETL database configuration
DB_NAME=data_bank
DB_USER=postgres
DB_PASSWORD=024899
DB_HOST=db
DB_PORT=5432

# Docker container and network names
POSTGRES_CONTAINER_NAME=etl_postgres
ETL_CONTAINER_NAME=etl_pipeline
ETL_IMAGE_NAME=etl_image
NETWORK_NAME=etl_network
```

3. **Make `run.sh` executable**:

```bash
chmod +x run.sh
```

---

## Running the Pipeline

Run the bash script to start everything:

```bash
./run.sh
```

This script will:

1. Stop and remove any existing containers and images for this project.
2. Remove and recreate the Docker network.
3. Build the ETL Docker image.
4. Start the Postgres container.
5. Wait for Postgres to be ready.
6. Run the ETL container, which executes the ETL pipeline.

Once completed, you will see logs confirming that the rows have been loaded into Postgres.

---

## How It Works

### ETL Steps:

1. **Extract**: `extract.py` fetches data from the source (e.g., API or CSV).
2. **Transform**: `transform.py` processes and cleans the data.
3. **Load**: `load.py` inserts the data into the Postgres database.

The orchestrator `main.py` coordinates these steps sequentially.

### Docker Setup:

* **ETL Container**: Runs the Python ETL scripts.
* **Postgres Container**: Stores the transformed data.
* **Network**: Both containers communicate over a custom Docker bridge network.

---

## Cleaning Up

To remove all containers, images, and network created by this project:

```bash
docker stop $POSTGRES_CONTAINER_NAME $ETL_CONTAINER_NAME || true
docker rm $POSTGRES_CONTAINER_NAME $ETL_CONTAINER_NAME || true
docker rmi $ETL_IMAGE_NAME || true
docker network rm $NETWORK_NAME || true
```

