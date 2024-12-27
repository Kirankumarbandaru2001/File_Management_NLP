import datetime

from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int] = Field(default=None, description="User ID")
    username: str = Field(..., description="Username of the user")
    email: str = Field(..., description="Email address of the user")
    hashed_password: str = Field(..., description="Hashed password for the user")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="User creation timestamp")
