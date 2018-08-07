from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='knowledge'
	primary_key= Column(Integer, primary_key=True)
	name=Column(String)
	topic=Column(String)
	article= Column(String)
	rating=Column(Integer)
	
	def __repr__(self):
		return ("Hey {}" \
               ", If you want to learn about {}" \
			   ", you should look at the Wikipedia article called {}.\n"\
			   "We gave this article a rating of {} out of 10.").format(
				   self.name, self.topic,self.article,self.rating)
