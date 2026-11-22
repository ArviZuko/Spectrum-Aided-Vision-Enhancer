# Spectrum-Aided Vision Enhancer (SAVE)

SAVE is a research project for turning a conventional **white-light image (WLI)** into a simulated **narrow-band-imaging-like image** and using both views in computer-aided image analysis. The project combines spectral reconstruction and color calibration with classification and detection experiments for endoscopic, bladder, and skin images. It also includes two Windows desktop applications that display the original video, the SAVE conversion, and model output side by side.

This repository preserves the supplied applications, documentation, spectral-processing sources, and model artifacts. Large installers, dependencies, and model artifacts are available from GitHub Releases. The corresponding folder notes link to the files and show their original names.

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
    Installer/            Windows installer download link
  Detection App/          same structure for object detection
Documentation/
  SAVE.docx               method and evaluation write-up
  SAVE PPT.pptx           experiment overview and results
  video.md                demonstration download link
SRC/
  NBI/                    spectral/color-transfer notebooks and scripts
  Latest_NBI/             later calibration, conversion, and evaluation notebooks
  SAVE/                   lookup-table generation and SAVE notebooks/assets
Models/
  README.md              model information and oversized-file download notes
  Bladder Cancer/         classification models
  Endoscopic Images/      endoscopic-image classifiers
  Esophageal Cancer/      classification and detection models
  Skin Cancer/            lesion and cancer model groups
  Kvasir/                 ulcer-model weights and notebooks
```

The [`SRC/NBI`](SRC/NBI), [`SRC/Latest_NBI`](SRC/Latest_NBI), and [`SRC/SAVE`](SRC/SAVE) directories contain exploratory notebooks rather than one packaged training pipeline. Some notebooks and scripts reference paths from the original research machines, so update those paths and install the imports used by the notebook before rerunning an experiment.

## Model artifacts

Model folders contain the supplied artifacts and notes for Release-hosted files. Where a model has both **WLI** and **SAVE** versions, see its folder for the corresponding files. The [model index](Models/README.md) also links to instructions for oversized archives.

Model formats vary (`.pt`, `.pth`, `.pkl`, `.h5`, `.keras`). Use the notebook in the relevant model folder to see that experiment's preprocessing, labels, and framework. There is no single loader or common input contract for every model.

## Get the files

Clone the repository for the tracked files. For Release-hosted files, use the download links in the corresponding folders and save the files under the names shown there. The [remaining-models Release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.1-remaining-models) contains additional model archives. See the [model index](Models/README.md) for extraction instructions for oversized archives.


## Use the applications

On Windows, use the [classification installer](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.0-large-files/SAVE_Classification_App_Installer.exe) or [detection installer](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.0-large-files/SAVE_Detection_App_Installer.exe), or download the files listed in the corresponding application folder notes and start the packaged application from its own `Dependency App` directory:

```powershell
cd "Applications\Classification App\Dependency App"
.\App.exe
```

For detection, use `Applications\Detection App\Dependency App` in the same way. The interfaces provide **Load Video**, **Start Camera**, **Pause**, and **Save** controls; the classification app also provides **Load Image Folder** and a result summary. The apps use files relative to the current working directory, including the conversion table and encrypted model. They prompt for the model password, which is **not included in this repository**. The installers have not been independently tested as part of this upload.

The editable PyQt entry points are [`Classification App/Source Code/App.py`](Applications/Classification%20App/Source%20Code/App.py) and [`Detection App/Source Code/App.py`](Applications/Detection%20App/Source%20Code/App.py). To run them from source, use an environment with the imports shown in those files (including OpenCV, NumPy, PyTorch, Ultralytics, Numba, and PyQt5), run from the relevant `Source Code` directory, and supply the model password. No pinned dependency or installation file is supplied, so source setup may require adapting versions and paths.

## Research use and scope

The documentation covers image calibration, SAVE synthesis, and experiments across multiple datasets. This repository preserves the supplied artifacts; it does not include every original training dataset. Oversized model files are preserved in Releases. The models and applications have not been independently tested for diagnostic accuracy or clinical use as part of this upload.
