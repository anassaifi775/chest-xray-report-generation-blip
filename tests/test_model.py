"""Tests for model module"""

import pytest
from src.model import BLIPModel

def test_model_initialization():
    """Test model can be initialized"""
    model = BLIPModel()
    assert model is not None
    assert model.processor is not None
    assert model.model is not None

def test_model_generation():
    """Test model can generate text"""
    from PIL import Image
    import numpy as np
    
    model = BLIPModel()
    
    # Create dummy image
    dummy_image = Image.fromarray(np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8))
    
    # Generate
    output = model.generate(dummy_image)
    
    assert output is not None
    assert isinstance(output, str)
    assert len(output) > 0
