'''
JAVA: Aidan Wong, Vedant Kothari
SoftDev
K35: Now Again for the First Time
2024-03-12
Time Spent: 2
'''

# filepath: c:\Users\Aidan\Documents\SOFTDEV\SOFTDEV\collaborative-storytelling-app\instance\config.py
import os

class Config:
    SECRET_KEY = os.urandom(32)
    DEBUG = True  # Set to False in production
    # Additional configuration settings can be added here as needed.