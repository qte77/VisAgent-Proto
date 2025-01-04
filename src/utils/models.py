"""
# Pydantic models

This module defines Pydantic models for structured data used in the application.
"""

from pydantic import BaseModel, Field
import numpy as np
from typing import List

class BoundingBox(BaseModel):
    """
    # Bounding Box model
    
    Represents a bounding box with coordinates (x1, y1, x2, y2).
    """
    x1: float
    y1: float
    x2: float
    y2: float

class Detection(BaseModel):
    """
    # Detection model
    
    Represents a detected object with label, score, and bounding box.
    """
    label: str
    score: float
    bbox: BoundingBox

class Segmentation(BaseModel):
    """
    # Segmentation model
    
    Represents a segmented object with label, score, mask, and bounding box.
    """
    label: str
    score: float
    mask: np.ndarray
    bbox: BoundingBox

class ConveyorSectionResult(BaseModel):
    """
    # Conveyor Section Result model
    
    Represents the result of conveyor section detection.
    """
    straight_sections_count: int
    curved_sections_count: int
    total_straight_length: float
    total_curved_length: float
    visualization_path: str

class SegmentationResult(BaseModel):
    """
    # Segmentation Result model
    
    Represents the result of image segmentation and visualization.
    """
    segmentation_results: List[Segmentation]
    visualized_image_path: str

