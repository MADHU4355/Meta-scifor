from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

# In-memory storage for user profiles
user_profiles: Dict[str, 'UserProfile'] = {}

# Define the UserProfile model
class UserProfile(BaseModel):
    username: str
    email: str
    age: Optional[int] = None

# Route to create a new user profile
@app.post("/profiles/", response_model=UserProfile)
def create_profile(profile: UserProfile):
    if profile.username in user_profiles:
        raise HTTPException(status_code=400, detail="Username already exists")
    user_profiles[profile.username] = profile
    return profile

# Route to retrieve a user profile
@app.get("/profiles/{username}", response_model=UserProfile)
def get_profile(username: str):
    if username not in user_profiles:
        raise HTTPException(status_code=404, detail="User not found")
    return user_profiles[username]

# Route to update a user profile
@app.put("/profiles/{username}", response_model=UserProfile)
def update_profile(username: str, profile: UserProfile):
    if username not in user_profiles:
        raise HTTPException(status_code=404, detail="User not found")
    user_profiles[username] = profile
    return profile

# Route to delete a user profile
@app.delete("/profiles/{username}")
def delete_profile(username: str):
    if username not in user_profiles:
        raise HTTPException(status_code=404, detail="User not found")
    del user_profiles[username]
    return {"detail": "User profile deleted"}
