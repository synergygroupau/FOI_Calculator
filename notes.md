# Notes
FOIC_venv/Scripts/activate
set FLASK_APP=FOI_Calulator.py

# Setup database for first time
flask db init
flask db migrate -m "users table"
flask db upgrade