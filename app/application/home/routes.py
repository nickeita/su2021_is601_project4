from flask import Blueprint, render_template
from flask import current_app as app


home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')


@home_bp.route('/', methods=['GET'])
def home():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    return render_template('home.html', title="House Listing Central", description="Your Resource For House Listings")
