import connexion
import six

from swagger_server.models.create_short_request import CreateShortRequest  # noqa: E501
from swagger_server.models.create_short_response import CreateShortResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.filter_params import FilterParams  # noqa: E501
from swagger_server.models.filtered_short import FilteredShort  # noqa: E501
from swagger_server.models.search_params import SearchParams  # noqa: E501
from swagger_server.models.short import Short  # noqa: E501
from swagger_server import util
from swagger_server.services.short_service import ShortService
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def api_shorts_create_post(body):  # noqa: E501
    """Add a new short

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateShortResponse
    """
    # if connexion.request.is_json:
    #     body = CreateShortRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    if not connexion.request.is_json:
        return ErrorResponse(status="Invalid request format", status_code=400), 400
    
    body = CreateShortRequest.from_dict(connexion.request.get_json())
    try:
        user_id = get_jwt_identity()

        short = ShortService.create_short(body, user_id)
        if not short:
            return ErrorResponse(status="Unauthorized", status_code=401), 401
        return CreateShortResponse(message="Short added successfully", short_id=str(short.id), status_code=200), 200
    except ValueError as e:
        return ErrorResponse(status=str(e), status_code=400), 400


def api_shorts_feed_get():  # noqa: E501
    """Get shorts feed

     # noqa: E501


    :rtype: List[Short]
    """
    # return 'do some magic!'
    shorts = ShortService.get_feed()
    return [Short(short_id=str(short.id), category=short.category, title=short.title, author=short.author, publish_date=short.publish_date, content=short.content, actual_content_link=short.actual_content_link, image=short.image, votes={"upvote": short.upvotes, "downvote": short.downvotes}) for short in shorts], 200


def api_shorts_filter_get(filter=None, search=None):  # noqa: E501
    """Get filtered shorts feed

     # noqa: E501

    :param filter: 
    :type filter: dict | bytes
    :param search: 
    :type search: dict | bytes

    :rtype: List[FilteredShort]
    """
    # if connexion.request.is_json:
    #     filter = FilterParams.from_dict(connexion.request.get_json())  # noqa: E501
    # if connexion.request.is_json:
    #     search = SearchParams.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    filter_params = connexion.request.args.get('filter', {})
    search_params = connexion.request.args.get('search', {})
    
    try:
        shorts = ShortService.filter_shorts(filter_params, search_params)
        if not shorts:
            return ErrorResponse(status="No short matches your search criteria", status_code=400), 400
        return [FilteredShort(short_id=str(short.id), title=short.title, content=short.content, author=short.author, contains_title=filter_params.get('contains_title', False), contains_content=filter_params.get('contains_content', False), contains_author=filter_params.get('contains_author', False)) for short in shorts], 200
    except ValueError as e:
        return ErrorResponse(status=str(e), status_code=400), 400
