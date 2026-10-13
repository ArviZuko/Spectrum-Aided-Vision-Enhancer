# svc_polynomial

This folder points to the remaining files for `Skin Cancer/BCC, SCC, SK, AK/Classification/svc_polynomial` from the original SAVE project. The package contains **4 files** (11.16 GiB before compression). It is stored in the [remaining-models Release](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/tag/v1.1-remaining-models) because it was not included in the curated Git tree.

## Download

- [model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip.part001](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.1-remaining-models/model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip.part001) — 1.68 GiB; SHA-256 `311ae1ec544eb7e39d12c72a96c43c7937969661acaa5c7a600f07fcdcf3422a`
- [model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip.part002](https://github.com/ArviZuko/Spectrum-Aided-Vision-Enhancer/releases/download/v1.1-remaining-models/model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip.part002) — 260.4 MiB; SHA-256 `65d4a4bfafcad2c897ecdd1472f9aecb63d47d0bca1014545270ba106e9a1f26`

The ZIP stores paths beginning with `Models/`. Extract it **at the root of the cloned repository** to restore the original model location. All parts are needed for a multipart ZIP.

For a multipart archive, put every part in one folder and join them with PowerShell before extracting:

```powershell
$parts = Get-ChildItem -File -Filter 'model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip.part*' | Sort-Object Name
$output = [System.IO.File]::Create('model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip')
try {
    foreach ($part in $parts) {
        $inputFile = [System.IO.File]::OpenRead($part.FullName)
        try { $inputFile.CopyTo($output) } finally { $inputFile.Dispose() }
    }
} finally { $output.Dispose() }
```

Then extract `model-skin-cancer-bcc-scc-sk-ak-classification-svc-polynomial-d93ab9af.zip` at the repository root. The parts must be combined in the listed order; an individual part cannot be opened as a ZIP.
