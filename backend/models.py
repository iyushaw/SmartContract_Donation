from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    donor = Column(String, index=True)
    amount = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    donor_id = Column(Integer, ForeignKey('donor.id'))
    ethereum_address = Column(String, unique=True, index=True)
    don_key = relationship('Donor')


class Donor(Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    donations = relationship("Donation", back_populates="donor")

Base.metadata.create_all(bind=engine)