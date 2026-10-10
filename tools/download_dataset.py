"""Download and extract the original Action_09, Action_15 and Action_16 images."""
import argparse
import hashlib
import json
import os
import shutil
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

BASE = 'https://github.com/AimerReol/MoE-3DGS-Dataset/releases/download'

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.load(response)

def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as file:
        for block in iter(lambda: file.read(8*1024*1024), b''):
            result.update(block)
    return result.hexdigest()

def download(url, path, expected_size, expected_sha):
    if path.exists() and path.stat().st_size == expected_size and digest(path) == expected_sha:
        return
    temp = path.with_suffix(path.suffix + '.download')
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(url, timeout=120) as response, temp.open('wb') as file:
                shutil.copyfileobj(response, file, length=8*1024*1024)
            if temp.stat().st_size != expected_size or digest(temp) != expected_sha:
                raise RuntimeError('Download size or SHA256 verification failed')
            temp.replace(path)
            return
        except (OSError, RuntimeError, urllib.error.URLError) as error:
            if attempt == 5:
                raise RuntimeError(f'Failed to download {path.name}: {error}') from error
            print(f'Retrying {path.name} ({attempt}/5): {error}', flush=True)
            time.sleep(10*attempt)

def extract(path, output, sequence, expected_count):
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        if len(infos) != expected_count:
            raise RuntimeError('Archive file count does not match manifest')
        for info in infos:
            destination = (output / info.filename).resolve()
            if os.path.commonpath([str(output), str(destination)]) != str(output):
                raise RuntimeError('Unsafe archive path')
            if not info.filename.startswith(sequence + '/WhiteBg/'):
                raise RuntimeError('Unexpected archive directory layout')
        archive.extractall(output)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sequence', choices=['Action_09','Action_15','Action_16','all'], default='all')
    parser.add_argument('--output', type=Path, default=Path('datasets'))
    parser.add_argument('--start-frame', type=int, default=0)
    parser.add_argument('--end-frame', type=int)
    parser.add_argument('--keep-archives', action='store_true')
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    cache = output / '.downloads'
    cache.mkdir(exist_ok=True)
    state_path = cache / 'completed.json'
    completed = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {}
    sequences = ['Action_15','Action_16','Action_09'] if args.sequence=='all' else [args.sequence]
    for sequence in sequences:
        tag = sequence.lower().replace('_','') + '-v1'
        try:
            manifest = fetch_json(f'{BASE}/{tag}/{sequence}_manifest.json')
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise SystemExit(f'{sequence}: release is not published yet. Check the repository README for upload status.') from None
            raise
        for part in manifest['archives']:
            if part['end_frame'] < args.start_frame or (args.end_frame is not None and part['start_frame'] > args.end_frame):
                continue
            key = sequence + '/' + part['name']
            if completed.get(key) == part['sha256']:
                print(f'Already extracted: {part["name"]}', flush=True)
                continue
            print(f'Downloading {part["name"]}', flush=True)
            path = cache / part['name']
            download(f'{BASE}/{tag}/{part["name"]}', path, part['bytes'], part['sha256'])
            extract(path, output, sequence, part['file_count'])
            completed[key] = part['sha256']
            temp_state = state_path.with_suffix('.tmp')
            temp_state.write_text(json.dumps(completed, indent=2), encoding='utf-8')
            temp_state.replace(state_path)
            if not args.keep_archives:
                path.unlink()
            print(f'Extracted and verified: {part["name"]}', flush=True)

if __name__ == '__main__':
    main()
