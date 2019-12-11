from flask import Blueprint

ironman = Blueprint('dentity', __name__)


from ironman.views import index
from ironman.views import suit_read
from ironman.views import suit_read_video
from ironman.views import suit_read_all
from ironman.views import suit_status
