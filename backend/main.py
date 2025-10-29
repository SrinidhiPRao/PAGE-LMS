from fastapi import FastAPI, HTTPException, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from .models import Personality, User
from .database import get_session, engine
from .templates import router as templates_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

app.include_router(templates_router)


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/personality")
async def save_personality(request: Request, db: Session = Depends(get_session)):
    data = await request.json()
    user = db.exec(select(User).order_by(User.id.desc())).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found or not logged in")

    personality = Personality(
        user_id=user.id,
        Openness=data["Openness"],
        Conscientiousness=data["Conscientiousness"],
        Extraversion=data["Extraversion"],
        Agreeableness=data["Agreeableness"],
        Neuroticism=data["Neuroticism"],
    )

    db.add(personality)
    db.commit()
    db.refresh(personality)

    return {"message": "Personality saved", "user_id": user.id}


@app.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    with Session(engine) as session:
        existing_user = session.exec(
            select(User).where(User.username == username)
        ).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {"message": "User registered successfully", "user_id": new_user.id}


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user or user.password != password:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        return {"message": "Login successful", "user_id": user.id}
