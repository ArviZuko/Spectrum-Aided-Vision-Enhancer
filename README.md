# Spectrum-Aided Vision Enhancer (SAVE)

This repository is a curated upload of `D:\Projects\SAVE`. It retains the complete `Applications/`, `Documentation/`, and `SRC/` directories and three compact model choices for each available cancer or endoscopy group. The original local folder was not changed.

## Included models

| Group | Selected models |
| --- | --- |
| Bladder cancer | GoogLeNet, YOLOv5, ResNet34 |
| Endoscopic images | Inception V3, logistic regression, augmented logistic regression |
| Esophageal cancer | Random forest, MobileNetV2, YOLOv8 detection |
| Skin cancer: Acrodon | YOLOv10, YOLOv5, YOLOv8 |
| Skin cancer: ALM/MIS/SSM | SGD ResNet34, Inception XGBoost, ResNet34 LightGBM |
| Skin cancer: BCC/SCC/SK/AK | Random forest, logistic regression, SGD SVM |
| Kvasir ulcer | YOLOv8n, EfficientNetB2, Keras `Model.keras` |

The `Models/Glaucoma/` image collection is also included. It contains images and spreadsheets, not saved model weights. Other model folders, including the 5–8 GB SVM weights, are deliberately omitted to keep this repository manageable. These selections favor the smallest complete model folders within each group; both SAVE and WLI variants are retained where present in those folders.

## Large files

GitHub rejects regular Git files over 100 MiB. Eleven files from the included folders, including installers and the documentation video, are stored individually in the [large-files release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.0-large-files). [`large-files.json`](large-files.json) maps each asset to its original path, byte count, and SHA-256 checksum. Restore them after cloning with Python 3.9 or newer:

```bash
python restore_large_files.py
```

Pass `--root PATH` to restore into another copy of the repository. The script verifies every download before placing it at its original path. There is no Git LFS dependency or LFS storage charge for this layout.

Code, application binaries, and model artifacts are preserved as supplied; they have not been independently run or validated as part of this upload.
