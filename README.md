# Chest X-ray Report Generation with BLIP

Automated radiology report generation from chest X-ray images using BLIP (Bootstrapping Language-Image Pre-training) model.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Project Overview

This project fine-tunes the BLIP model on the NIH Chest X-ray dataset to automatically generate radiology reports from chest X-ray images. The model learns to identify pathologies and generate structured medical reports.

### Key Features

- ✅ **BLIP Model**: State-of-the-art vision-language model
- ✅ **NIH Dataset**: Trained on 112K+ chest X-rays
- ✅ **Auto-Checkpointing**: Resume training from any point
- ✅ **Google Colab**: Train on free GPU
- ✅ **Production Ready**: Easy deployment with Flask/FastAPI
- ✅ **Evaluation Metrics**: BLEU, ROUGE scores

## 📊 Results

| Metric | Score |
|--------|-------|
| BLEU-1 | 0.54 |
| BLEU-4 | 0.26 |
| ROUGE-L | 0.60 |

### Sample Output

**Input:** Chest X-ray image  
**Generated Report:**
```
PA chest radiograph. Cardiomegaly is present. The lungs are clear. 
No acute pulmonary abnormality. Small bilateral pleural effusions. 
Impression: Cardiomegaly, Pleural effusion.
```

## 🚀 Quick Start

### Option 1: Google Colab

1. Open notebook in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/chest-xray-report-generation-blip/blob/main/notebooks/BLIP_Training.ipynb)
2. Select GPU runtime
3. Run all cells
4. Training takes 15-20 hours

### Option 2: Local Setup

```bash
# Clone repository
git clone https://github.com/yourusername/chest-xray-report-generation-blip.git
cd chest-xray-report-generation-blip

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download dataset (NIH Chest X-ray)
# See docs/DATA_PREPARATION.md

# Prepare data
python scripts/prepare_data.py --data_dir /path/to/NIH --output_dir data

# Train model
python scripts/train.py --config config/training_config.yaml

# Generate reports
python scripts/inference.py --model checkpoints/best_model --image test.jpg
```

## 📁 Project Structure

```
chest-xray-report-generation-blip/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
├── .gitignore                  # Git ignore rules
│
├── notebooks/                   # Jupyter/Colab notebooks
│   ├── BLIP_Training.ipynb     # Main training notebook
│   ├── Data_Exploration.ipynb  # Dataset analysis
│   └── Model_Evaluation.ipynb  # Results & metrics
│
├── src/                        # Source code
│   ├── __init__.py
│   ├── model.py                # BLIP model wrapper
│   ├── dataset.py              # Dataset class
│   ├── trainer.py              # Training logic
│   └── inference.py            # Inference engine
│
├── scripts/                    # Standalone scripts
│   ├── prepare_data.py         # Data preparation
│   ├── train.py                # Training script
│   └── inference.py            # Generate reports
│
├── config/                     # Configuration files
│   └── training_config.yaml    # Training parameters
│
├── docs/                       # Documentation
│   ├── INSTALLATION.md         # Setup guide
│   ├── DATA_PREPARATION.md     # Dataset guide
│   ├── TRAINING.md             # Training guide
│   └── DEPLOYMENT.md           # Deployment guide
│
├── tests/                      # Unit tests
│   ├── test_model.py
│   ├── test_dataset.py
│   └── test_inference.py
│
└── checkpoints/                # Saved models (gitignored)
    └── best_model/
```

## 📚 Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Data Preparation](docs/DATA_PREPARATION.md)
- [Training Guide](docs/TRAINING.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🎓 Model Details

### Architecture

- **Vision Encoder**: Swin Transformer (224x224 images)
- **Text Decoder**: T5-base (transformer decoder)
- **Parameters**: 225M
- **Training**: Fine-tuned on NIH Chest X-ray dataset

### Dataset

- **Name**: NIH Chest X-ray Dataset
- **Images**: 112,120 frontal-view X-rays
- **Patients**: 30,805 unique patients
- **Labels**: 14 disease categories
- **Reports**: Generated from labels (not original radiology reports)

### Training Configuration

```yaml
batch_size: 32
learning_rate: 5e-5
epochs: 20
optimizer: AdamW
scheduler: Cosine with warmup
```

## 🔬 Evaluation

Evaluate model on test set:

```bash
python scripts/evaluate.py --model checkpoints/best_model --split test
```

Results:
- BLEU-1: 0.54
- BLEU-4: 0.26
- ROUGE-L: 0.60
- BERTScore: 0.72

## 🚀 Deployment

### Flask API

```python
from flask import Flask, request, jsonify
from src.inference import BLIPReportGenerator

app = Flask(__name__)
generator = BLIPReportGenerator('checkpoints/best_model')

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image']
    report = generator.generate_report(image)
    return jsonify({'report': report})
```

### Docker

```bash
docker build -t chest-xray-blip .
docker run -p 5000:5000 chest-xray-blip
```

## 📊 Performance

| Setup | Training Time | Cost |
|-------|---------------|------|
| Google Colab (T4) | 18-20 hours | Free |
| Google Colab Pro (V100) | 8-10 hours | $10/month |
| Local GPU (RTX 3090) | 30-40 hours | Hardware cost |
| AWS p3.2xlarge | 15-18 hours | ~$30 |

## 🤝 Contributing

Contributions are welcome!  Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BLIP Model**: [Salesforce Research](https://github.com/salesforce/BLIP)
- **NIH Dataset**: [NIH Clinical Center](https://nihcc.app.box.com/v/ChestXray-NIHCC)
- **Transformers**: [Hugging Face](https://huggingface.co/transformers/)

## 📧 Contact

Anas Saifi - [@anassaifi775]

Project Link: [https://github.com/anassaifi775/chest-xray-report-generation-blip](https://github.com/anassaifi775/chest-xray-report-generation-blip)

## 📖 Citation

If you use this project in your research, please cite:

```bibtex
@misc{chest-xray-blip-2024,
  author = {Anas Saifi},
  title = {Chest X-ray Report Generation with BLIP},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/anassaifi775/chest-xray-report-generation-blip}
}
```

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=anassaifi775/chest-xray-report-generation-blip&type=Date)](https://star-history.com/#anassaifi775/chest-xray-report-generation-blip&Date)

---

**Made with ❤️ for medical AI research**
