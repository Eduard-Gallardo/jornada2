from flask import Blueprint, render_template
from utils.conexion_db import get_db_connection

alquiler_bp = Blueprint('alquiler', __name__)

@alquiler_bp.route('/alquiler')
def alquiler():
    return render_template('alquiler.html')