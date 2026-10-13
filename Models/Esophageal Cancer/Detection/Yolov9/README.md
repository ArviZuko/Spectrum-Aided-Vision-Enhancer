# Yolov9

This folder points to the remaining files for `Esophageal Cancer/Detection/Yolov9` from the original SAVE project. The package contains **1017 files** (2.05 GiB before compression). It is stored in the [remaining-models Release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.1-remaining-models) because it was not included in the curated Git tree.

## Download

- [model-esophageal-cancer-detection-yolov9-8dcd960a.zip.part001](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.1-remaining-models/model-esophageal-cancer-detection-yolov9-8dcd960a.zip.part001) — 1.68 GiB; SHA-256 `95acb5fc3c06b0e1cdf01d3e3a31e08a95c716179f4ae53a235b9227d806a1c8`
- [model-esophageal-cancer-detection-yolov9-8dcd960a.zip.part002](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.1-remaining-models/model-esophageal-cancer-detection-yolov9-8dcd960a.zip.part002) — 225.5 MiB; SHA-256 `76618703006b6a9150d1e25ada86afc17a652c5d7860e49cdd80a297bda760c9`

The ZIP stores paths beginning with `Models/`. Extract it **at the root of the cloned repository** to restore the original model location. All parts are needed for a multipart ZIP.

For a multipart archive, put every part in one folder and join them with PowerShell before extracting:

```powershell
$parts = Get-ChildItem -File -Filter 'model-esophageal-cancer-detection-yolov9-8dcd960a.zip.part*' | Sort-Object Name
$output = [System.IO.File]::Create('model-esophageal-cancer-detection-yolov9-8dcd960a.zip')
try {
    foreach ($part in $parts) {
        $inputFile = [System.IO.File]::OpenRead($part.FullName)
        try { $inputFile.CopyTo($output) } finally { $inputFile.Dispose() }
    }
} finally { $output.Dispose() }
```

Then extract `model-esophageal-cancer-detection-yolov9-8dcd960a.zip` at the repository root. The parts must be combined in the listed order; an individual part cannot be opened as a ZIP.
