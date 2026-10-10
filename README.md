# MoE-3DGS-Dataset

A multi-view video dataset for 3D Gaussian video reconstruction and streaming.

## Available sequences

| Sequence | Synchronized frames | Cameras per frame | PNG images | Resolution | Original size |
| --- | ---: | ---: | ---: | --- | ---: |
| [Action_15](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action15-v1) | 2,155 | 32 | 68,960 | 4096 x 3000 | 132.23 GiB |
| [Action_16](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action16-v1) | 2,190 | 32 | 70,080 | 4096 x 3000 | 191.90 GiB |

These releases contain the original PNG images from the supplied `WhiteBg` directories. Frame numbers and camera filenames are preserved.

```text
Action_15/
  WhiteBg/
    000000/
      00.png
      ...
      31.png
    ...
    002154/
Action_16/
  WhiteBg/
    000000/
      00.png
      ...
      31.png
    ...
    002189/
```

## Download and extract

The sequences are distributed as independent ZIP archives under Releases. Action_15 has 77 archives and Action_16 has 112. Each archive contains a consecutive range of complete synchronized frames. Extract the archives into the same destination directory to reconstruct the directory tree.

The images retain their original bytes. Archives use ZIP store mode because PNG images are already compressed. Every ZIP is below 2 GiB.

Using Python 3.9 or newer:

```bash
python tools/download_dataset.py --sequence Action_15 --output ./datasets
python tools/download_dataset.py --sequence Action_16 --output ./datasets
```

To download both:

```bash
python tools/download_dataset.py --sequence all --output ./datasets
```

The downloader checks SHA-256 before extraction and records completed archives so an interrupted run can continue. It deletes successfully extracted temporary archives by default. Use `--keep-archives` to retain them. For a short trial, use `--end-frame 9`; the downloader selects the complete archive covering the requested frames.

Each release also contains:

- `Action_XX_manifest.json`: archive names, byte sizes, frame ranges, file counts, and SHA-256 values.
- `Action_XX_SHA256SUMS.txt`: checksums for all archives and the manifest.
- `Action_XX_files.json.gz`: the source file inventory with relative paths and original byte sizes.

To download manually, obtain the ZIP files and checksum list from the corresponding release, verify the files, and extract them into a common directory.

## Data details

Camera indices are `00` through `31`. Timestamps are represented by the original six-digit frame directory names. Image counts were checked against all 32 camera filenames in every frame directory.

The supplied sequence folders for this upload contain RGB PNG images. Camera calibration files, segmentation masks, and reconstruction checkpoints can be documented in separate releases if supplied later. The capture frame rate is not specified in these source folders.
