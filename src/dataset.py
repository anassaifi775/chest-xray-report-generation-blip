"""Dataset Class for Chest X-rays"""

from torch.utils.data import Dataset
from PIL import Image
import pandas as pd
import os

class ChestXrayDataset(Dataset):
    """Dataset for chest X-ray images and reports"""
    
    def __init__(self, csv_file, image_dir, processor, max_length=256):
        self.data = pd.read_csv(csv_file)
        self.image_dir = image_dir
        self.processor = processor
        self.max_length = max_length
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        image_path = os.path.join(self.image_dir, row['image_path'])
        image = Image.open(image_path).convert('RGB')
        report = str(row['report'])
        
        encoding = self.processor(
            images=image,
            text=report,
            return_tensors="pt",
            padding="max_length",
            max_length=self.max_length,
            truncation=True
        )
        return {k: v.squeeze(0) for k, v in encoding.items()}
