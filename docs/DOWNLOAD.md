# Download guide

[Dataset overview](../README.md)

## Download with Python

From the repository root, select a released sequence and an output directory:

```bash
python tools/download_dataset.py --sequence Action_15 --output ./data
python tools/download_dataset.py --sequence Action_16 --output ./data
python tools/download_dataset.py --sequence Action_09 --output ./data
```

Available releases are listed in the [sequence table](../README.md#sequences). A sequence marked **Not yet released** has no public download. Once their releases are available, `--sequence all` downloads the three sequences currently supported by the downloader: Action_09, Action_15 and Action_16.

The downloader uses only the Python standard library (Python 3.9+). It verifies each archive against the manifest before extraction. Successful downloads are recorded in `<output>/.downloads/completed.json`; rerunning the same command skips archives already extracted. Temporary ZIP files are removed after successful extraction unless `--keep-archives` is specified.

### Select a frame range

```bash
python tools/download_dataset.py --sequence Action_15 --end-frame 9 --output ./data
python tools/download_dataset.py --sequence Action_16 --start-frame 100 --end-frame 200 --output ./data
```

Frame-range options select complete archives intersecting the requested interval. The extracted data may therefore contain additional frames outside that interval.

## Archive layout

Each ZIP contains a consecutive range of source frame directories and can be extracted independently. ZIP store mode preserves the original image bytes without recompression. Every archive is smaller than 2 GiB.

| Sequence | Archives | Frame indices |
| --- | ---: | --- |
| Action_09 | 77 | `000000`–`000965` |
| Action_15 | 77 | `000000`–`002154` |
| Action_16 | 112 | `000000`–`002189` |

Each release includes the following metadata:

| File | Contents |
| --- | --- |
| `Action_XX_manifest.json` | Archive filenames, frame ranges, image counts, byte sizes and SHA-256 values. |
| `Action_XX_SHA256SUMS.txt` | SHA-256 checksums for the ZIP archives and manifest. |
| `Action_XX_files.json.gz` | Source image inventory with relative paths and byte sizes. |

The known missing view in Action_09 is documented in its manifest. Existing images and frame folders are preserved without substituting the missing image.

## Manual download

1. Open the sequence release linked in the [README](../README.md#sequences).
2. Download its ZIP archives, manifest and checksum file.
3. Verify archive checksums. On Linux, for example, run `sha256sum -c Action_XX_SHA256SUMS.txt` in the directory containing the archives and manifest.
4. Extract all archives for a sequence into the same output directory. Their paths reconstruct `Action_XX/WhiteBg/<frame>/<camera>.png`.
