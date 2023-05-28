from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bookings")
async def bookings():
    return {"message": "Bookings"}

@app.post("/create-booking")
async def create_booking():
    return {"message": "Create Booking"}