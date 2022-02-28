from flask import Flask, session

app = Flask(__name__)

# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = "0fd43ce85c91f99322bc2bd18d3b02b76b4ae71d2855941142fcbfea40a0555f"

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


DATABASE = 'nursechartpro'