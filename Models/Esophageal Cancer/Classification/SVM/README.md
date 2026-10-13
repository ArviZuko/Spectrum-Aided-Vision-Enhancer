# SVM

This folder points to the remaining files for `Esophageal Cancer/Classification/SVM` from the original SAVE project. The package contains **4 files** (14.71 GiB before compression). It is stored in the [remaining-models Release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.1-remaining-models) because it was not included in the curated Git tree.

## Download

- [model-esophageal-cancer-classification-svm-f6fb5a87.zip.part001](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.1-remaining-models/model-esophageal-cancer-classification-svm-f6fb5a87.zip.part001) — 1.68 GiB; SHA-256 `de12d7d58a396116f5167a899f2b7033ab8fa595fcf465198ec9a35c30974e83`
- [model-esophageal-cancer-classification-svm-f6fb5a87.zip.part002](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.1-remaining-models/model-esophageal-cancer-classification-svm-f6fb5a87.zip.part002) — 1.14 GiB; SHA-256 `0162f2eabf703a458ddaf20c924bd100e320f397d281a9d45ee75a7ca3962e1e`

The ZIP stores paths beginning with `Models/`. Extract it **at the root of the cloned repository** to restore the original model location. All parts are needed for a multipart ZIP.

For a multipart archive, put every part in one folder and join them with PowerShell before extracting:

```powershell
$parts = Get-ChildItem -File -Filter 'model-esophageal-cancer-classification-svm-f6fb5a87.zip.part*' | Sort-Object Name
$output = [System.IO.File]::Create('model-esophageal-cancer-classification-svm-f6fb5a87.zip')
try {
    foreach ($part in $parts) {
        $inputFile = [System.IO.File]::OpenRead($part.FullName)
        try { $inputFile.CopyTo($output) } finally { $inputFile.Dispose() }
    }
} finally { $output.Dispose() }
```

Then extract `model-esophageal-cancer-classification-svm-f6fb5a87.zip` at the repository root. The parts must be combined in the listed order; an individual part cannot be opened as a ZIP.
