from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Video(Base):
    __tablename__ = "videos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    hashtags = Column(String(500), nullable=True)
    streamtape_url = Column(String(500), nullable=False)
    streamtape_id = Column(String(100), nullable=False)
    banner_path = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def hashtag_list(self):
        """Return hashtags as a list"""
        if not self.hashtags:
            return []
        return [tag.strip() for tag in self.hashtags.split(',') if tag.strip()]
    
    @property
    def embed_url(self):
        """Generate embed URL for Streamtape"""
        return f"https://streamtape.com/e/{self.streamtape_id}/"
    
    def __repr__(self):
        return f"<Video(id={self.id}, title='{self.title}')>"