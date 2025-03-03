#!/usr/bin/python3
"""This module initializes the models package"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
