from sqlalchemy import Column, String


from database import Base


class Url(Base):
    __tablename__ = "url"

    hash_url = Column(String, primary_key=True, index=True)
    og_url = Column(String, unique=True, index=True)
    date_time = Column(String)


