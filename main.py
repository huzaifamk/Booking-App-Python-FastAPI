from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Booking(BaseModel):
    id: int
    Hotel_Name: str
    Address: str
    Price: int
    Is_Available: bool
    Rating: Optional[float] = None


# temp_booking = Booking(id=1, Hotel_Name="Taj", Address="Mumbai", Price=10000, Is_Available=True, Rating=4.5), Booking(id=2, Hotel_Name="Oberoi", Address="Delhi", Price=15000, Is_Available=True, Rating=4.8), Booking(id=3, Hotel_Name="Leela", Address="Bangalore", Price=20000, Is_Available=True, Rating=4.9), Booking(id=4, Hotel_Name="Taj", Address="Chennai", Price=10000, Is_Available=True, Rating=4.5), Booking(id=5, Hotel_Name="Oberoi", Address="Kolkata", Price=15000, Is_Available=True, Rating=4.8), Booking(id=6, Hotel_Name="Leela", Address="Pune", Price=20000, Is_Available=True, Rating=4.9), Booking(id=7, Hotel_Name="Taj", Address="Hyderabad", Price=10000, Is_Available=True, Rating=4.5), Booking(id=8, Hotel_Name="Oberoi", Address="Ahmedabad", Price=15000, Is_Available=True, Rating=4.8), Booking(id=9, Hotel_Name="Leela", Address="Jaipur", Price=20000, Is_Available=True, Rating=4.9), Booking(id=10, Hotel_Name="Taj", Address="Lucknow", Price=10000, Is_Available=True, Rating=4.5), Booking(id=11, Hotel_Name="Oberoi", Address="Kanpur", Price=15000, Is_Available=True, Rating=4.8), Booking(id=12, Hotel_Name="Leela", Address="Noida", Price=20000, Is_Available=True, Rating=4.9)

temp_booking = [Booking(id=1, Hotel_Name="Taj", Address="Mumbai", Price=10000, Is_Available=True, Rating=4.5), Booking(id=2, Hotel_Name="Oberoi", Address="Delhi", Price=15000, Is_Available=True, Rating=4.8), Booking(id=3, Hotel_Name="Leela", Address="Bangalore", Price=20000, Is_Available=True, Rating=4.9), Booking(id=4, Hotel_Name="Taj", Address="Chennai", Price=10000, Is_Available=True, Rating=4.5), Booking(id=5, Hotel_Name="Oberoi", Address="Kolkata", Price=15000, Is_Available=True, Rating=4.8), Booking(id=6, Hotel_Name="Leela", Address="Pune", Price=20000, Is_Available=True, Rating=4.9), Booking(id=7, Hotel_Name="Taj", Address="Hyderabad", Price=10000, Is_Available=True, Rating=4.5), Booking(id=8, Hotel_Name="Oberoi", Address="Ahmedabad", Price=15000, Is_Available=True, Rating=4.8), Booking(id=9, Hotel_Name="Leela", Address="Jaipur", Price=20000, Is_Available=True, Rating=4.9), Booking(id=10, Hotel_Name="Taj", Address="Lucknow", Price=10000, Is_Available=True, Rating=4.5), Booking(id=11, Hotel_Name="Oberoi", Address="Kanpur", Price=15000, Is_Available=True, Rating=4.8), Booking(id=12, Hotel_Name="Leela", Address="Noida", Price=20000, Is_Available=True, Rating=4.9)]


@app.get("/")
async def root():
    return {"message": "Ping Successful, server is up and running..."}

@app.get("/bookings/{id}")
async def bookings(id: int, response: Response):
    for booking in temp_booking:
        if booking.id == id:
            return booking
    raise HTTPException(status_code=404, detail=f"Booking with id {id} not found")

@app.delete("/bookings/{id}")
async def delete_booking(id: int, response: Response):
    for booking in temp_booking:
        if booking.id == id:
            temp_booking.remove(booking)
            return {"message": f"Booking with id {id} is deleted successfully"}
    raise HTTPException(status_code=204, detail=f"Booking with id {id} not found")

@app.put("/bookings/{id}")
async def update_booking(id: int, payload: Booking, response: Response):
    for booking in temp_booking:
        if booking.id == id:
            booking.Hotel_Name = payload.Hotel_Name
            booking.Address = payload.Address
            booking.Price = payload.Price
            booking.Is_Available = payload.Is_Available
            booking.Rating = payload.Rating
            return {"message": f"Booking with id {id} is updated successfully"}
    raise HTTPException(status_code=404, detail=f"Booking with id {id} not found")

@app.get("/bookings")
async def bookings():
    return {"data": temp_booking}


@app.post("/create-booking", status_code=status.HTTP_201_CREATED)
async def create_booking(payload: Booking):
    print(payload.dict())
    return {"Title": f"Booking for {payload.Hotel_Name} is created successfully with price {payload.Price} and address {payload.Address} and rating {payload.Rating}"}
