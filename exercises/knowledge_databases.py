from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_article(name,topic,article,rating):
	Knowledge_object=Knowledge(
		name=name,
		topic=topic,
		article=article,
		rating=rating
	)
	session.add(Knowledge_object)
	session.commit()
	return(Knowledge_object)
	

def query_all_articles():
	articles=session.query(Knowledge).all()
	return articles

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

x=add_article("Matvey","CS","Hacking", 9)
y=add_article("derin","bio","cells", 8)
print(query_all_articles())
