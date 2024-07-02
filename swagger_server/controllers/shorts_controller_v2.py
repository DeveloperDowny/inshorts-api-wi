from flask import request
from swagger_server.models import (SignupRequest, SignupResponse, LoginRequest, 
                                   LoginResponse, CreateShortRequest, CreateShortResponse, 
                                   Short, FilteredShort, ErrorResponse)
from swagger_server.services.auth_service import AuthService
from swagger_server.services.short_service import ShortService
from swagger_server.utils.decorators import admin_required, token_required

def signup_post():
    """Controller for user signup"""
    if not request.is_json:
        return ErrorResponse(status="Invalid request format", status_code=400), 400
    
    body = SignupRequest.from_dict(request.get_json())
    try:
        user = AuthService.register_user(body.username, body.email, body.password)
        return SignupResponse(status="Account successfully created", status_code=200, user_id=str(user.id)), 200
    except ValueError as e:
        return ErrorResponse(status=str(e), status_code=400), 400

def login_post():
    """Controller for user login"""
    if not request.is_json:
        return ErrorResponse(status="Invalid request format", status_code=400), 400
    
    body = LoginRequest.from_dict(request.get_json())
    user, token = AuthService.login_user(body.username, body.password)
    if user and token:
        return LoginResponse(status="Login successful", status_code=200, user_id=str(user.id), access_token=token), 200
    else:
        return ErrorResponse(status="Incorrect username/password provided. Please retry", status_code=401), 401

@admin_required
def create_short_post():
    """Controller for creating a new short"""
    if not request.is_json:
        return ErrorResponse(status="Invalid request format", status_code=400), 400
    
    body = CreateShortRequest.from_dict(request.get_json())
    try:
        short = ShortService.create_short(body)
        return CreateShortResponse(message="Short added successfully", short_id=str(short.id), status_code=200), 200
    except ValueError as e:
        return ErrorResponse(status=str(e), status_code=400), 400

def get_shorts_feed():
    """Controller for getting the shorts feed"""
    shorts = ShortService.get_feed()
    return [Short.from_dict(short) for short in shorts], 200

@token_required
def filter_shorts():
    """Controller for filtering and searching shorts"""
    filter_params = request.args.get('filter', {})
    search_params = request.args.get('search', {})
    
    try:
        shorts = ShortService.filter_shorts(filter_params, search_params)
        if not shorts:
            return ErrorResponse(status="No short matches your search criteria", status_code=400), 400
        return [FilteredShort.from_dict(short) for short in shorts], 200
    except ValueError as e:
        return ErrorResponse(status=str(e), status_code=400), 400