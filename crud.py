from sqlalchemy.orm import Session
import datetime
import models, schemas
import hashlib


def get_url(db: Session, user_url: str):
    return db.query(models.Url).filter(models.Url.hash_url == user_url).first()


def create_url(db: Session, user: schemas.Item):
	url = user.url
	date_time = datetime.datetime.now()
	short_url = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
    
	find_db = db.query(models.Url).filter(models.Url.hash_url == short_url).first()
	if find_db:
		return find_db

	db_column = models.Url(hash_url=short_url, og_url=url, 
    					date_time=date_time)
	db.add(db_column)
	db.commit()
	db.refresh(db_column)
	return db_column