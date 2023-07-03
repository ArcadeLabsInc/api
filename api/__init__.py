"""App entry point"""
from flask import Flask, jsonify, request
from api.conversations import new_message

application = Flask(__name__)


@application.route('/')
def index():
    """Placeholder route"""
    return 'Hello, World!'


@application.route('/message', methods=['POST'])
def message():
    """Handle sending a new message to a conversation."""
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        return new_message()
    else:
        return jsonify({"success": False, "error": "Invalid content type"}), 400
