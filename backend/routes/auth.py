from fastapi import APIRouter, HTTPException, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.user import UserCreate, UserLogin, User, Token, UserInDB
from auth.security import verify_password, get_password_hash, create_access_token
from datetime import timedelta
import os

router = APIRouter(prefix="/auth", tags=["authentication"])

# Get database dependency
from server import db

@router.post("/register", response_model=dict)
async def register(user_data: UserCreate):
    """
    Register a new user
    """
    # Check if user already exists
    existing_user = await db.users.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user with hashed password
    user_dict = user_data.dict()
    password = user_dict.pop("password")
    hashed_password = get_password_hash(password)
    
    user_in_db = UserInDB(
        **user_dict,
        hashed_password=hashed_password
    )
    
    # Insert into database
    await db.users.insert_one(user_in_db.dict())
    
    # Create access token
    access_token = create_access_token(
        data={"sub": user_data.email}
    )
    
    # Return user and token
    user_response = User(**user_in_db.dict())
    return {
        "token": access_token,
        "user": user_response.dict()
    }

@router.post("/login", response_model=dict)
async def login(credentials: UserLogin):
    """
    Login user and return JWT token
    """
    # Find user by email
    user_doc = await db.users.find_one({"email": credentials.email})
    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    user_in_db = UserInDB(**user_doc)
    
    # Verify password
    if not verify_password(credentials.password, user_in_db.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Create access token
    access_token = create_access_token(
        data={"sub": credentials.email}
    )
    
    # Return user and token
    user_response = User(**user_in_db.dict())
    return {
        "token": access_token,
        "user": user_response.dict()
    }

@router.get("/me", response_model=User)
async def get_current_user(token: str):
    """
    Get current logged in user
    """
    from auth.security import verify_token
    
    email = verify_token(token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    
    user_doc = await db.users.find_one({"email": email})
    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return User(**user_doc)
