# Training Guide

## Quick Start

```bash
python scripts/train.py --config config/training_config.yaml
```

## Configuration

Edit `config/training_config.yaml` to customize:

### Batch Size

```yaml
training:
  batch_size: 32  # Reduce if out of memory
```

### Learning Rate

```yaml
training:
  learning_rate: 5.0e-5  # Increase for faster convergence
```

### Epochs

```yaml
training:
  num_epochs: 20  # More epochs = better results
```

## Training on Google Colab

See `notebooks/BLIP_Training.ipynb` for complete Colab training.

## Monitoring

Training progress is displayed in real-time:

```
Epoch 5/20
------------------------------------------------------------
Epoch 5/20: 100%|████| 2190/2190 [42:15<00:00, loss=1.8234, lr=4.2e-05]
  Train Loss: 1.8234
  Val Loss: 1.7856
  🏆 Best model saved!
```

## Checkpointing

Models are saved to `checkpoints/`:
- `latest_checkpoint.pt` - Resume training
- `best_model/` - Best performing model

## Resume Training

To resume from checkpoint:

```bash
python scripts/train.py --resume checkpoints/latest_checkpoint.pt
```

## Expected Results

With full NIH dataset (20 epochs):
- Training time: 18-20 hours on Colab T4
- BLEU-1: 0.50-0.58
- ROUGE-L: 0.56-0.63
