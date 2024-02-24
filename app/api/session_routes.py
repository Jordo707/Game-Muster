from flask import Blueprint, jsonify, session, request
from app.models import db, user, Session, Campaign
#Add forms here

session_routes = Blueprint('session', __name__)

@session_routes.route('/<campaign_id>')
def campaign_sessions(campaign_id):
    """
    Get all sessions associated with a given campaign
    """
    # Query the database to get the campaign and its associated sessions
    campaign = Campaign.query.get(campaign_id)

    # Check if the campaign exists
    if campaign is None:
        return jsonify({"message": "Campaign not found"}), 404

    # Get all sessions associated with the campaign
    sessions = Session.query.filter_by(campaign_id=campaign_id).all()

    # Prepare the sessions data to be returned in JSON format
    session_data = []
    for session in sessions:
        session_data.append({
            'id': session.id,
            'date_time': session.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            'location': session.location,
            'summary': session.summary
            # Add more session attributes as needed
        })

    return jsonify(session_data), 200
