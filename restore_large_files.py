"""Restore large SAVE files from the GitHub Release into their original paths."""

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

REPO = "ArviZuko/Spectrum-Aided-Vision-Enhancer"


def digest(path):
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            checksum.update(block)
    return checksum.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads((root / "large-files.json").read_text(encoding="utf-8"))
    url = f"https://api.github.com/repos/{REPO}/releases/tags/{manifest['release_tag']}"
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "SAVE-restore"})
    with urllib.request.urlopen(request) as response:
        release = json.load(response)
    assets = {asset["name"]: asset["browser_download_url"] for asset in release["assets"]}

    for number, item in enumerate(manifest["files"], 1):
        target = (root / item["path"]).resolve()
        if not target.is_relative_to(root):
            raise ValueError(f"Unsafe path in manifest: {item['path']}")
        if target.exists() and target.stat().st_size == item["bytes"] and digest(target) == item["sha256"]:
            print(f"[{number}/{len(manifest['files'])}] Already verified: {item['path']}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + ".download")
        if item["asset"] not in assets:
            raise FileNotFoundError(f"Release asset missing: {item['asset']}")
        print(f"[{number}/{len(manifest['files'])}] Downloading {item['path']}", flush=True)
        request = urllib.request.Request(assets[item["asset"]], headers={"User-Agent": "SAVE-restore"})
        with urllib.request.urlopen(request) as response, temporary.open("wb") as output:
            while block := response.read(8 * 1024 * 1024):
                output.write(block)
        if temporary.stat().st_size != item["bytes"] or digest(temporary) != item["sha256"]:
            temporary.unlink(missing_ok=True)
            raise ValueError(f"Download verification failed: {item['path']}")
        temporary.replace(target)
    print("All release files verified.")


if __name__ == "__main__":
    main()
