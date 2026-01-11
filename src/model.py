"""BLIP Model Wrapper"""

from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

class BLIPModel:
    """Wrapper for BLIP model"""
    
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
    
    def generate(self, image, max_length=256):
        """Generate report from image"""
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.processor.decode(outputs[0], skip_special_tokens=True)
