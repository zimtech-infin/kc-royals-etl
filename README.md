# KC Royals Backend Project

## Project Overview

The **KC Royals Backend Project** is a Django-based backend system designed to manage Kansas City Royals player data, including statistics, team rosters, and historical performance. It includes an **ETL (Extract, Transform, Load) pipeline** to process raw player data and a **RESTful API** for data retrieval.

This project provides a **structured and efficient backend** for data storage, retrieval, and management, ensuring **clean and organized player data** in an **SQLite database**.

## Project Objective

- Develop a **scalable backend** for managing Kansas City Royals player data.
- Implement an **ETL pipeline** to extract and load player statistics from external sources.
- Provide **RESTful API endpoints** for frontend applications.
- Enable **Django Admin support** for data management.
- Ensure **structured data storage** in SQLite.

## Tech Stack

- **Backend Framework:** Django (Django REST Framework)
- **Database:** SQLite
- **ETL Processing:** Python, Django ORM
- **Authentication:** JWT (JSON Web Tokens)
- **Admin Dashboard:** Django Admin
- **Testing:** Django Test Framework, Postman

## Development Approach

### Backend API Development

- Django REST Framework is used to expose API endpoints.
- JWT authentication is implemented for secure access.
- Django Admin provides direct data management.

### ETL Pipeline for Data Processing

- **Extract**: Reads player data from `players.json`.
- **Transform**: Cleans and structures data.
- **Load**: Inserts structured records into SQLite.

### Data Storage & Management

- SQLite is used for lightweight, embedded storage.
- Data models efficiently handle **batting and pitching stats**.
- Admin panel allows manual data entry and modifications.

## Usage Instructions

### Setup the Project

1. create a directory and unzip the attached file
2. navigate to that directory.
3. start front end
   - navigate to frontend dir and run: npm start
4. start backend
   - navigate to backend dir and run: python manage.py runserver

Django backend credentials:
-username : admin
-password : pass
