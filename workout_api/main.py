from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(
    title='WorkoutApi',
    version="0.1.0",
    description="Esta é uma API de competição de crossfit",
)
app.include_router(api_router)
