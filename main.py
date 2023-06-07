from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bookings")
async def bookings():
    return {"message": "Bookings"}

@app.post("/create-booking")
async def create_booking(payload: dict = Body(...)):
    print(payload)
    return {"Title": f"Booking for {payload['Hotel_Name']} created successfully"}