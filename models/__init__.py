#!/usr/bin/python3
"""
Contains Packages and modules for models
"""

from models.engine.file_storage import FileStorage
import json

storage = FileStorage
storage.reload()