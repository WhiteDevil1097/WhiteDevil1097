import flask
from flask import request, jsonify
import sqlite3
import re
import colorama
from colorama import Fore,Style

# some decorations for giving it a good look and feel.
colorama.init()
print(Fore.GREEN + Style.BRIGHT)
print()
print(r'     _______     ')
print(r'    /        \   ')
print(r'   /  #cloud  \  ')
print(r'  |   __  __  |  ')
print(r'  | _| |  | |_|  ')
print(r'     | |__| | |  ')
print(r'     |_____  | | ')
print(r'          | | |  ')
print(r'          |_|_|  ')

print(r'[+]Cloudflare for Termux[+]')
print(r'[#]Coder By White_Devil[#]')
app = flask.Flask(__name__)

# Database connection
conn = sqlite3.connect('cloudflare.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS blocked_ips (
        ip TEXT PRIMARY KEY
    );
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS allowed_ips (
        ip TEXT PRIMARY KEY
    );
''')
conn.commit()

# Load blocked IP addresses from database
blocked_ips = [row[0] for row in cursor.execute('SELECT ip FROM blocked_ips')]

# Load allowed IP addresses from database
allowed_ips = [row[0] for row in cursor.execute('SELECT ip FROM allowed_ips')]

# Define the reverse proxy server
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    # Check if the request is from a blocked IP address
    if request.remote_addr in blocked_ips:
        return 'Access denied', 403

    # Check if the request is from an allowed IP address
    if request.remote_addr in allowed_ips:
        return flask.redirect(f'http://{request.host}/{path}')

    # Check for SQL injection attacks
    if re.search(r'union|select|insert|update|delete|drop|create|alter|truncate', request.query_string):
        return 'SQL injection attack detected', 403

    # Check for XSS attacks
    if re.search(r'<script|<iframe|<object|<embed|<applet', request.query_string):
        return 'XSS attack detected', 403

    # Rate-limit incoming traffic
    if request.remote_addr in [ip for ip, count in cursor.execute('SELECT ip, count(*) FROM requests WHERE timestamp > datetime("now", "-1 minute") GROUP BY ip HAVING count(*) > 100')]:
        return 'Rate limit exceeded', 429

    # Proxy the request to the origin server
    origin_server = 'http://example.com'  # Replace with the origin server URL
    response = requests.get(f'{origin_server}/{path}', headers=request.headers)
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(debug=True)
