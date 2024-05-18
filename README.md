# StudyTime Tasks and Notes CRUD

This is a FastAPI project that provides CRUD operations for my [StudyTime Discord bot](https://github.com/f-andrei/StudyTime).

## Project Structure

The project is structured as follows:

- `app/`: Contains the main application code.
  - `models/`: Contains the database models.
  - `repos/`: Contains the CRUD operations for notes and tasks.
  - `routers/`: Contains the FastAPI routers for the application.
  - `schemas/`: Contains the Pydantic models for data validation.
- `testing.py`: Contains testing code for the application.

## Setup

1. Clone the repository.
2. Install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

3. Set up your environment variables in a .env file. Refer to app/settings.py for the required variables.

## Running the Application
To run the application, use the following command:
```sh
uvicorn app.routers.main:app --reload
```

## API Endpoints
The application provides the following endpoints:

 - Task CRUD operations: /tasks/
 - Note CRUD operations: /notes/
 - User CRUD operations: /users/

Refer to the routers in app/routers/ for more details on the API endpoints.

## Testing
To run the tests, use the following command:
```sh
python testing.py
```