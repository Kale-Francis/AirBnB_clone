#!/usr/bin/python3
"""
Contains the Packages and modules for testing

"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models')))  # Adjust path to models directory

import unittest
from models.base_model import BaseModel  # Correct import after modifying sys.path
