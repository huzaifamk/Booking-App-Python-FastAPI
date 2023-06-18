from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Booking(BaseModel):
    Hotel_Name: str
    Address: str
    Price: int
    Is_Available: bool
    Rating : Optional[float] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/bookings")
async def bookings():
    return {"message": "Bookings"}


@app.post("/create-booking")
async def create_booking(payload: Booking):
    print(payload)
    return {"Title": f"Booking for {payload.Hotel_Name} is created successfully with price {payload.Price} and address {payload.Address} and rating {payload.Rating}"}
