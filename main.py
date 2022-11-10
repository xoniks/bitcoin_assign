from fastapi import FastAPI, Body, Depends
import schemas
import models
from coin import btc_add, eth_add

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.post("/{coin_name}")
def Generate_Address(coin_name: str,item:schemas.Item, session: Session = Depends(get_session)):

    if coin_name.upper()=='BTC':
        value = btc_add()

    elif coin_name.upper()=='ETH':
        value =  eth_add()

    item = models.Item(coin_name = coin_name, coin_add=value )
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@app.get("/")
def List_Address(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def Retrieve_Address(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item







