# Dockerized Python ETL Pipeline

This project demonstrates an **ETL (Extract, Transform, Load) pipeline** built with Python and PostgreSQL, fully dockerized. The pipeline extracts data from a source (Pokémon API), transforms it using Python, and loads it into a PostgreSQL database.

---

## Project Overview

The ETL pipeline automates the process of collecting, processing, and storing data:

1. **Extract:** Data is pulled from an external source (API or CSV).
2. **Transform:** The data is cleaned, normalized, and structured into a DataFrame.
3. **Load:** The processed data is inserted into a PostgreSQL database table.

The project also includes a Bash script to orchestrate container management, networking, and ETL execution.

---

## File Structure

```
docker/
│
├── Dockerfile             # Docker image for the ETL pipeline
├── docker_var.sh          # Bash script to build and run containers
├── .env                   # Environment variables for DB credentials and config
├── requirements.txt       # Python dependencies
├── extract.py             # Python script to extract data
├── transform.py           # Python script to transform data
├── load.py                # Python script to load data into Postgres
├── run_pipeline.py        # Main Python script to run the full ETL process
└── README.md              # Project documentation
```

> `.env` is provided as a template. Users should create their own `.env` with credentials and source URLs.

---

## Prerequisites

* Docker installed and running
* Internet access (to download source data)
* Optional: `psql` or DBeaver to inspect the database

---

## Environment Variables

Create a `.env` file in the `docker/` directory:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=024899
POSTGRES_DB=data_bank
DB_NAME=data_bank
DB_USER=postgres
DB_PASSWORD=024899
DB_HOST=db
DB_PORT=5432
POSTGRES_CONTAINER_NAME=postgres_cont
ETL_CONTAINER_NAME=etl_cont
ETL_IMAGE_NAME=etl_pipeline
NETWORK_NAME=etl_network
SOURCE_URL=https://pokeapi.co/api/v2/pokemon
```

> Do **not** commit `.env` to GitHub as it contains sensitive information.

---

## Setup and Run

### 1. Prepare Bash Script

Make the automation script executable:

```bash
cd docker/
chmod +x docker_var.sh
```

### 2. Run the Pipeline

```bash
./docker_var.sh
```

This script will:

* Stop and remove any existing containers/images.
* Remove any existing Docker network.
* Create a Docker network for container communication.
* Build the ETL Docker image.
* Run a PostgreSQL container.
* Run the ETL container connected to the network.

### 3. Verify Containers

```bash
docker ps
```

Expected output:

```
CONTAINER ID   IMAGE          NAMES
xxxxxxx        postgres       postgres_cont
xxxxxxx        etl_pipeline   etl_cont
```

---

## Check ETL Logs

```bash
docker logs etl_cont
```

Example log output:

```
Getting Postgres ready...
Extracting data from API...
Transformation complete
Loaded 20 rows into 'pokemon' table
```

---

## Connect to PostgreSQL

* **Using `psql`:**

```bash
psql -h localhost -p 55432 -U postgres -d data_bank
```

* **Using DBeaver:**

  * Host: `localhost`
  * Port: `55432`
  * Database: `data_bank`
  * Username: `postgres`
  * Password: `024899`

---

## Run ETL Manually

To run the ETL process inside the ETL container:

```bash
docker exec -it etl_cont bash
python3 run_pipeline.py
```

---

## Dockerfile Details

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt extract.py transform.py load.py run_pipeline.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "run_pipeline.py"]
```

* Uses Python 3.12 slim image
* Copies all ETL scripts into `/app`
* Installs Python dependencies
* Runs ETL when the container starts

---

## Bash Script (`docker_var.sh`) Highlights

* Stops/removes existing containers and images
* Removes old Docker network if exists
* Builds ETL image
* Creates Docker network
* Runs PostgreSQL container
* Waits for Postgres to be ready
* Runs ETL pipeline container

---

## Notes

* ETL container depends on PostgreSQL. Ensure Postgres is running before ETL.
* `.env` contains sensitive credentials and should not be committed.
* Containers communicate over a custom Docker network.
* Host port `55432` maps to PostgreSQL for external access.

---

## Data Table

The pipeline creates a table `pokemon` in `data_bank`:

| Column     | Type    |
| ---------- | ------- |
| pokemon_id | INTEGER |
| name       | TEXT    |
| url        | TEXT    |
