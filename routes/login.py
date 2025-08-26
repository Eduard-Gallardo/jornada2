from flask import blueprint, render_template
from utils.conexion_db import get_db_connection

login_bp = blueprint('login', __name__)
@login_bp.route('/login')
def login():
    return render_template('login.html')