from sqlmodel import SQLModel, Field
from pydantic import BaseModel

from sqlmodel import SQLModel, Field, Relationship


class Personality(SQLModel, table=True):
    user_id: int = Field(primary_key=True, foreign_key="user.id")
    Openness: float
    Conscientiousness: float
    Extraversion: float
    Agreeableness: float
    Neuroticism: float

    user: "User" = Relationship(back_populates="personality")


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str

    personality: "Personality" = Relationship(back_populates="user")


class ContentRequest(BaseModel):
    user_id: int
    topic: str
    emotion: str
