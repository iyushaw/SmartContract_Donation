from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database import Base

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Donation App API"}

@app.post("/donate/")
def create_donation(donor_name: str, ethereum_address: str, amount: float):
    db = SessionLocal()
    
    # Check if the donor exists or create a new one
    donor = db.query(Donor).filter(Donor.ethereum_address == ethereum_address).first()
    if not donor:
        donor = Donor(name=donor_name, ethereum_address=ethereum_address)
        db.add(donor)
        db.commit()
        db.refresh(donor)
    
    # Create a donation
    donation = Donation(donor_id=donor.id, amount=amount)
    db.add(donation)
    db.commit()
    db.close()
    
    return {"message": "Donation created successfully"}

@app.get("/donations/")
def get_donations():
    return donations

@app.get("/total_donated/")
def get_total_donated():
    total_donated = sum(donation["amount"] for donation in donations)
    return {"total_donated": total_donated}