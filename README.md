# Spectrum-Aided Vision Enhancer (SAVE)

SAVE is a research project for turning a conventional **white-light image (WLI)** into a simulated **narrow-band-imaging-like image** and using both views in computer-aided image analysis. The project combines spectral reconstruction and color calibration with classification and detection experiments for endoscopic, bladder, and skin images. It also includes two Windows desktop applications that display the original video, the SAVE conversion, and model output side by side.

This repository is a **curated subset** of the original `SAVE` folder. The application, documentation, and spectral-processing source directories are represented here; selected smaller model families are included for each study group. Files over GitHub's regular Git limit are available separately in a [Release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.0-large-files).

## Idea and novelty

Conventional WLI records three broad RGB channels. The SAVE workflow described in [`Documentation/SAVE.docx`](Documentation/SAVE.docx) uses a 24-patch color chart and measured reflectance spectra to calibrate an imaging system, estimate spectral information from RGB, and select wavelength bands to produce an NBI-like view. It was designed to explore NBI-style visualization on conventional endoscopes and video capsule endoscopy (VCE), where a hardware NBI mode may be unavailable.

The distinctive combination in this project is:

1. **Camera-aware spectral reconstruction:** linearize and calibrate RGB values, relate them to measured spectra in color space, then reconstruct a spectral representation using a reduced spectral basis.
2. **Software-defined band selection:** synthesize a SAVE image from the estimated spectral data rather than requiring a dedicated narrow-band light source. The research documents discuss the familiar blue/green NBI bands alongside additional wavelength regions for color matching.
3. **A practical conversion path:** the application code applies a precomputed RGB-to-SAVE lookup table (`nor_wli_nbi_table.npy`) for frame-by-frame conversion.
4. **WLI-versus-SAVE CAD experiments:** the model folders contain training notebooks and artifacts for comparing classification or detection on original and transformed images; the desktop interfaces show both image streams and predictions together.

These are the project's design and research claims, not an assertion of clinical performance. The supplied report and presentation contain the study's calibration and image-similarity results; this repository has not independently reproduced them.

## Repository structure

```text
Applications/
  Classification App/
    Source Code/          PyQt application source and local assets
    Dependency App/       packaged Windows application and dependencies
    Installer/            download link for the Windows installer
  Detection App/          same structure for object detection
Documentation/
  SAVE.docx               method and evaluation write-up
  SAVE PPT.pptx           experiment overview and results
  Video.mp4               demonstration (download from Release)
SRC/
  NBI/                    spectral/color-transfer notebooks and scripts
  Latest_NBI/             later calibration, conversion, and evaluation notebooks
  SAVE/                   lookup-table generation and SAVE notebooks/assets
Models/
  README.md              links to downloadable model families not in Git
  Bladder Cancer/         selected classification models
  Endoscopic Images/      selected endoscopic-image classifiers
  Esophageal Cancer/      selected classification and detection models
  Skin Cancer/            selected lesion and cancer model groups
  Kvasir/                 three compact ulcer-model weights and notebooks
  Glaucoma/               image/spreadsheet collection (no saved model weights)
```

The [`SRC/NBI`](SRC/NBI), [`SRC/Latest_NBI`](SRC/Latest_NBI), and [`SRC/SAVE`](SRC/SAVE) directories contain exploratory notebooks rather than one packaged training pipeline. Some notebooks and scripts reference paths from the original research machines, so update those paths and install the imports used by the notebook before rerunning an experiment.

## Included model selection

To keep a browsable repository, this upload favors compact model folders. Directory names below match the supplied project, including its spelling.

| Study group | Included model folders or weights |
| --- | --- |
| Bladder cancer | `GOOGLNET`, `YOLOV5`, `RESNET34` |
| Endoscopic images | `Inception_V3`, `Logistic Regression`, `Augumented` |
| Esophageal cancer | `Classification/RF`, `Classification/MobileNetV2`, `Detection/Yolov8` |
| Skin lesions (`Acrodon`) | `YoloV10`, `YoloV5`, `YoloV8` |
| Melanoma (`ALM, MIS, SSM`) | `Classification/SGD_Resnet 34`, `inception-xgb`, `resnet34-lightgbm` |
| Other skin lesions (`BCC, SCC, SK, AK`) | `Classification/rf`, `logistic regression`, `sgd_svm` |
| Kvasir ulcer | `yolov8n-cls.pt`, `efficientnetB2.h5`, `Model.keras`, plus notebooks |

Where a selected folder contains both **WLI** and **SAVE** versions, both are retained. The `Models/Glaucoma/` folder contains images and spreadsheets rather than trained weights. The other model families are available as separate ZIP downloads: browse the [additional-model index](Models/README.md), open a model's folder README, and follow its download and extraction instructions. Several original SVM weights are individually about 5–8 GB, so their archives are split into smaller Release assets.

Model formats vary (`.pt`, `.pth`, `.pkl`, `.h5`, `.keras`). Use the notebook in the relevant model folder to see that experiment's preprocessing, labels, and framework. There is no single loader or common input contract for every model.

## Get the files

Clone the repository with `git clone https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer.git`. GitHub does not include the 11 oversized files in the clone. Download any files you need from the [large-files Release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.0-large-files) and place them at the paths below. The two installer folders contain direct download links to their installers.

| Release asset | Original path in this project |
| --- | --- |
| `Classification-App-best.pt` | `Applications/Classification App/Dependency App/best.pt` |
| `Classification-App-best.pt.encrypted` | `Applications/Classification App/Dependency App/best.pt.encrypted` |
| `Classification-App-internal-best.pt.encrypted` | `Applications/Classification App/Dependency App/_internal/best.pt.encrypted` |
| `Classification-App-torch_cpu.dll` | `Applications/Classification App/Dependency App/_internal/torch/lib/torch_cpu.dll` |
| [Classification installer](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.0-large-files/SAVE_Classification_App_Installer.exe) | `Applications/Classification App/Installer/SAVE_Classification_App_Installer.exe` |
| `Detection-App-torch_cpu.dll` | `Applications/Detection App/Dependency App/_internal/torch/lib/torch_cpu.dll` |
| [Detection installer](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.0-large-files/SAVE_Detection_App_Installer.exe) | `Applications/Detection App/Installer/SAVE_Detection_App_Installer.exe` |
| `SAVE_Demo_Video.mp4` | `Documentation/Video.mp4` |
| `Endoscopic-Augmented-LR-model.pkl` | `Models/Endoscopic Images/Augumented/LR/logistic_regression_model.pkl` |
| `Endoscopic-Logistic-Regression-model.pkl` | `Models/Endoscopic Images/Logistic Regression/logistic_regression_model.pkl` |
| `SRC-SAVE-nor_wli_nbi_table.npy` | `SRC/SAVE/nor_wli_nbi_table.npy` |

The Release assets total about 2.3 GB. No Git LFS setup is needed.

## Use the applications

On Windows, either download the [classification installer](Applications/Classification%20App/Installer/README.md) or [detection installer](Applications/Detection%20App/Installer/README.md), or download the applicable large dependencies from the table above and start the packaged application from its own `Dependency App` directory:

```powershell
cd "Applications\Classification App\Dependency App"
.\App.exe
```

For detection, use `Applications\Detection App\Dependency App` in the same way. The interfaces provide **Load Video**, **Start Camera**, **Pause**, and **Save** controls; the classification app also provides **Load Image Folder** and a result summary. The apps use files relative to the current working directory, including the conversion table and encrypted model. They prompt for the model password, which is **not included in this repository**. The installers have not been independently tested as part of this upload.

The editable PyQt entry points are [`Classification App/Source Code/App.py`](Applications/Classification%20App/Source%20Code/App.py) and [`Detection App/Source Code/App.py`](Applications/Detection%20App/Source%20Code/App.py). To run them from source, use an environment with the imports shown in those files (including OpenCV, NumPy, PyTorch, Ultralytics, Numba, and PyQt5), run from the relevant `Source Code` directory, and supply the model password. No pinned dependency or installation file is supplied, so source setup may require adapting versions and paths.

## Research use and scope

The documentation covers image calibration, SAVE synthesis, and experiments across multiple datasets. This repository preserves the supplied artifacts; it does not include every original training dataset or every trained model. The models and applications have not been independently tested for diagnostic accuracy or clinical use as part of this upload.
