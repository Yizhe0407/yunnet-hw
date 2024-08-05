from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error
import logging

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignUpData(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class SignInData(BaseModel):
    email: EmailStr
    password: str

# 連接數據庫
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rafe47max",
            database="user"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

@app.post("/submit")
def submit_data(data: SignUpData):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Check if the email already exists
        cursor.execute("SELECT * FROM AccountPassword WHERE email = %s", (data.email,))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO AccountPassword (name, email, password) VALUES (%s, %s, %s)",
                (data.name, data.email, data.password)
            )
            connection.commit()
            return {"status": "success"}
        else:
            return {"status": "info", "detail": "此 email 已注册"}
    except Error as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to insert data")
    finally:
        cursor.close()
        connection.close()
        
@app.post("/signin")
def sign_in(data:SignInData):
    connection = get_db_connection()
    cursor=connection.cursor()
    try:
        cursor.execute("SELECT * FROM AccountPassword WHERE email = %s AND password = %s", (data.email, data.password))
        user = cursor.fetchone()
        if user:
            logging.info(user)
            return {"status": "success", "name": user[1], "email": user[2], "detail": "Sign-in successful"}
        else:
            return {"status": "error", "detail": "Invalid email or password"}
    except Error as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch data")
    finally:
        cursor.close()
        connection.close()

# To run the FastAPI app, use: uvicorn main:app --reload