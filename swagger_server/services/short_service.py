from flask import jsonify, request
from datetime import timedelta
from swagger_server.database.database_models import db, Short, User
from datetime import datetime
from swagger_server.models.create_short_response import CreateShortResponse
from swagger_server.models.short import Short as ShortModel


class ShortService:
    @staticmethod
    def create_short(data, user_id):
        user = User.query.get(user_id)
        if not user.is_admin:
            return None
            

        new_short = Short( 
            category=data.category,
            title=data.title,
            author=data.author,
            publish_date=data.publish_date,
            content=data.content,
            actual_content_link=data.actual_content_link,
            image=data.image,
            upvotes=data.votes.upvote,
            downvotes=data.votes.downvote
        
        )
        db.session.add(new_short)
        db.session.commit()
        return new_short
        

    @staticmethod
    def get_feed():
        shorts = Short.query.order_by(Short.publish_date.desc(), Short.upvotes.desc()).all()
        return shorts

    @staticmethod
    def filter_shorts(filter_params,search_params):  

        query = Short.query

        if 'category' in filter_params:
            query = query.filter(Short.category == filter_params['category'])
        if 'publish_date' in filter_params:
            query = query.filter(Short.publish_date >= datetime.fromisoformat(filter_params['publish_date']))
        if 'upvote' in filter_params:
            query = query.filter(Short.upvotes > int(filter_params['upvote']))

        if 'title' in search_params:
            query = query.filter(Short.title.ilike(f"%{search_params['title']}%"))
        if 'keyword' in search_params:
            query = query.filter((Short.title.ilike(f"%{search_params['keyword']}%")) | 
                                 (Short.content.ilike(f"%{search_params['keyword']}%")))
        if 'author' in search_params:
            query = query.filter(Short.author.ilike(f"%{search_params['author']}%"))

        shorts = query.all()
        
        if not shorts:
            return None
        return shorts