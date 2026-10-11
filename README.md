# MoE-3DGS Dataset

Multi-view image sequences for dynamic scene reconstruction, used in MoE-3DGS experiments. The scenes feature human motion and interaction with tabletop objects against a white background.

The full dataset consists of **18 sequences**. Following acceptance of the associated paper, the remaining sequences will be progressively released for public use.

![Representative images from Action_09, Action_15 and Action_16](assets/previews/overview.jpg)

[Sequences](#sequences) · [Download](#download) · [Data format](#data-format)

## Sequences

The three sequences listed below contain **5,311 temporal frames and 169,951 PNG images**. Each sequence has 32 camera views at **4096 × 3000** resolution. Frame and camera indices are retained in the image filenames and directory structure.

| Sequence | Frames | Views | Images | Size | Download |
| --- | ---: | ---: | ---: | ---: | --- |
| Action_09 | 966 | 32 | 30,911 | 130.37 GiB | [Release](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action09-v1) |
| Action_15 | 2,155 | 32 | 68,960 | 132.23 GiB | [Release](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action15-v1) |
| Action_16 | 2,190 | 32 | 70,080 | 191.90 GiB | [Release](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action16-v1) |

Sizes refer to the original image files.

<details>
<summary>Action_09: temporal and multi-view previews</summary>

![Action_09: three frame indices from camera views 00 and 16](assets/previews/Action_09.jpg)

</details>

<details>
<summary>Action_15: temporal and multi-view previews</summary>

![Action_15: three frame indices from camera views 00 and 16](assets/previews/Action_15.jpg)

</details>

<details>
<summary>Action_16: temporal and multi-view previews</summary>

![Action_16: three frame indices from camera views 00 and 16](assets/previews/Action_16.jpg)

</details>

Previews are resized for display. The release archives contain the original PNG files.

## Download

Data are distributed through the sequence releases linked above. A Python downloader retrieves the archives, verifies SHA-256 checksums and extracts the sequence directories.

```bash
git clone https://github.com/AimerReol/MoE-3DGS-Dataset.git
cd MoE-3DGS-Dataset
python tools/download_dataset.py --sequence Action_15 --output ./data
```

Requires Python 3.9 or newer; no additional packages are needed. Set `--sequence` to the desired released sequence. See the [download guide](docs/DOWNLOAD.md) for partial downloads, resuming downloads and manual extraction.

## Data format

```text
data/
├── Action_09/
│   └── WhiteBg/
│       ├── 000000/
│       │   ├── 00.png
│       │   ├── ...
│       │   └── 31.png
│       ├── 000001/
│       └── ...
├── Action_15/
│   └── WhiteBg/...
└── Action_16/
    └── WhiteBg/...
```

Six-digit directory names identify temporal frames, starting at `000000`. Filenames `00.png` through `31.png` identify camera views. Archives preserve this layout and the original image bytes.

