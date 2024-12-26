#!/usr/bin/python3
"""
Contains Packages and modules for models
"""

import json
from models import BaseModel
from models import FileStorage

storage = FileStorage
storage.reload()