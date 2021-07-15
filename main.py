import uvicorn
import models, crud, schemas

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

DOMAIN = 'http://127.0.0.1:8000/'

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()


@app.get("/{url_hash}")
async  def root(url_hash: str, db: Session = Depends(get_db)):
    db_url = crud.get_url(db, user_url=url_hash)

    if not db_url:
        raise HTTPException(status_code=404, detail="Url not found")
    rd = db_url.og_url

    return RedirectResponse(rd)


@app.post("/convert/")
async def shorten_process(url_s: schemas.ItemCreate, db: Session = Depends(get_db)):
    
    item_dict = url_s.dict()
    if not item_dict['url'].startswith('http'):
        raise HTTPException(status_code=417, detail="Wrong url format")

    db_url = crud.create_url(db, url_s)
    db_url.hash_url = DOMAIN + db_url.hash_url
    return db_url


if __name__ == '__main__':
    uvicorn.run(app)