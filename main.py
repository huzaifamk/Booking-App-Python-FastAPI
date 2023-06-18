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
    Rating: Optional[float] = None


temp_booking = Booking(Hotel_Name="Taj", Address="Mumbai", Price=10000, Is_Available=True, Rating=4.5), Booking(Hotel_Name="Oberoi", Address="Delhi", Price=15000, Is_Available=True, Rating=4.8), Booking(Hotel_Name="Taj", Address="Bangalore",
                                                                                                                                                                                                           Price=12000, Is_Available=True, Rating=4.7), Booking(Hotel_Name="Taj", Address="Chennai", Price=11000, Is_Available=True, Rating=4.6), Booking(Hotel_Name="Taj", Address="Kolkata", Price=9000, Is_Available=True, Rating=4.4)


@app.get("/")
async def root():
    return {"message": "Ping Successful, server is up and running..."}

@app.get("/bookings/{id}")
async def bookings(id: int):
    return {"data": temp_booking[id]}

@app.get("/bookings")
async def bookings():
    return {"data": temp_booking}


@app.post("/create-booking")
async def create_booking(payload: Booking):
    print(payload.dict())
    return {"Title": f"Booking for {payload.Hotel_Name} is created successfully with price {payload.Price} and address {payload.Address} and rating {payload.Rating}"}
