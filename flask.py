
import nest_asyncio
nest_asyncio.apply()

from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)
