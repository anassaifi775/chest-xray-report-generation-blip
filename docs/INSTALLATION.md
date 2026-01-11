# Installation Guide

## Prerequisites

- Python 3.8 or higher
- CUDA 11.7+ (for GPU training)
- 16GB RAM minimum (32GB recommended)
- 100GB free disk space

## Step 1: Clone Repository

```bash
git clone https://github.com/anassaifi775/chest-xray-report-generation-blip.git
cd chest-xray-report-generation-blip
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Step 4: Verify Installation

```bash
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import transformers; print(f'Transformers: {transformers.__version__}')"
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
```

## Troubleshooting

### CUDA Not Available

If CUDA is not detected:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### ImportError

If you get import errors:

```bash
pip install --upgrade transformers accelerate
```

## Next Steps

See [Data Preparation](DATA_PREPARATION.md) to set up your dataset.
