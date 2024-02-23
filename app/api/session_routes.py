from flask import Blueprint, jsonify, session, request
from app.models import campaign, db, user, session
#Add forms here

session_routes = Blueprint('session', __name__)

@session_routes.route('')
def campaign_sessions():
    """
    Get all sessions associated with a given campaign
    """
    camp_sessions =
