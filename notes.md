# Notes
FOIC_venv/Scripts/activate
set FLASK_APP=FOI_Calulator.py

# Flask shell
Flask shell

# Setup database for first time
flask db init

# changes going forward to the models.py, add new fields etc.
flask db migrate -m "whatever"
flask db upgrade

# Email server - error reporting 
export MAIL_SERVER=smtp.office365.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=ddavaris@synergygroup.net.au
export MAIL_PASSWORD=tdrptzejlyhmmhgo