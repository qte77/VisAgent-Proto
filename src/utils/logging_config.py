"""
# Logging configuration

This module configures the logger for the application.
"""

from loguru import logger

logger.add("vision_processing.log", rotation="10 MB")
