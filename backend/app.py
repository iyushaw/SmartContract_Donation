from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Donation App API"}

@app.post("/donate/")
def create_donation(donor: str, amount: float):
    donation = {"donor": donor, "amount": amount}
    donations.append(donation)
    return {"message": "Donation created successfully"}

@app.get("/donations/")
def get_donations():
    return donations

@app.get("/total_donated/")
def get_total_donated():
    total_donated = sum(donation["amount"] for donation in donations)
    return {"total_donated": total_donated}