from flask import Blueprint, jsonify, session, request
from app.models import Campaign, db
#Add forms here

campaign_routes = Blueprint('campaign', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@campaign_routes.route('')
def all_campaigns():
    """
    Get all current campaigns
    """
    campaigns = Campaign.query.all()

    for camp in campaigns:
        campaign_data = {
            'id':camp.id,
            'campaignName':camp.campaign_name,
            'gameMasterId': camp.game_master_id
        }

    return {'campaigns':campaign_data}

@campaign_routes.route('/<campaign_id>')
def single_campaign(campaign_id):
    """
    Get details of given campaign
    """
    curr_campaign = Campaign.query.get(campaign_id)

    campaign_data ={
        "campaign": curr_campaign.to_dict()
    }
    
    return campaign_data
