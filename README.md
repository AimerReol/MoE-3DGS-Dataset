# MoE-3DGS-Dataset

把 MoE-3DGS 实验用到的多视角序列整理在这里，先放 Action_09、Action_15 和 Action_16。原始图片都在 Releases 里，下面选了几帧，可以先看看内容。

Action_15 和 Action_16 已经上传。Action_09 正在上传，全部校验完成后会开放下载。

## 序列预览

每张预览选了三个时间点，以及 `00`、`16` 两个相机视角。预览做了缩小，下载包里是原始 PNG。

### Action_09

![Action_09 在三个时间点、两个相机视角下的原始图像预览](assets/previews/Action_09.jpg)

### Action_15

![Action_15 在三个时间点、两个相机视角下的原始图像预览](assets/previews/Action_15.jpg)

### Action_16

![Action_16 在三个时间点、两个相机视角下的原始图像预览](assets/previews/Action_16.jpg)

## 数据和下载

| 序列 | 帧数 | 相机数 | PNG 数量 | 原始大小 | 下载 |
| --- | ---: | ---: | ---: | ---: | --- |
| Action_09 | 966 | 32 | 30,911 | 130.37 GiB | 上传中 |
| Action_15 | 2,155 | 32 | 68,960 | 132.23 GiB | [Release](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action15-v1) |
| Action_16 | 2,190 | 32 | 70,080 | 191.90 GiB | [Release](https://github.com/AimerReol/MoE-3DGS-Dataset/releases/tag/action16-v1) |

图片分辨率都是 **4096 × 3000**。Action_09 的最后一帧（`000965`）缺少 `23.png`：前 965 帧都有 32 个视角，最后一帧有 31 个。这一张在源目录里就没有，下载包也按原样保留。

数据比较大，所以放在 GitHub Releases 里：Action_09 分成 77 包、Action_15 分成 77 包、Action_16 分成 112 包。每包小于 2 GiB，可以单独解压；同一个序列的所有包解压到同一个位置即可。

有 Python 3.9 或更新版本的话，可以用仓库里的下载脚本：

```bash
python tools/download_dataset.py --sequence Action_15 --output ./datasets
python tools/download_dataset.py --sequence Action_16 --output ./datasets
python tools/download_dataset.py --sequence Action_09 --output ./datasets
```

等三个序列都上传好后，也可以把 `--sequence` 换成 `all`，一次下载这三个序列。

想先取少量数据试一下，可以加 `--end-frame 9`。脚本会下载覆盖这些帧的完整分包，校验 SHA-256 后再解压。中断后重新运行同一条命令就能继续，已完成的分包会跳过。临时 ZIP 默认在解压后删除，想保留的话加 `--keep-archives`。

不使用脚本也可以：在对应 Release 下载 ZIP 和 `Action_XX_SHA256SUMS.txt`，核对校验值后解压。Release 里还有 `Action_XX_manifest.json`（分包列表、帧范围和校验值）以及 `Action_XX_files.json.gz`（原始文件清单）。

## 解压后的目录

三个序列使用相同的结构：

```text
Action_XX/
  WhiteBg/
    000000/
      00.png
      ...
      31.png
    000001/
      ...
```

六位数字目录表示帧号，`00.png` 到 `31.png` 对应相机编号。压缩包只做打包，保留了图片的原始字节和目录结构。

这次上传的文件只有 `WhiteBg` 下的图像，暂时没有相机标定、分割掩码或重建模型。源目录也没有提供拍摄帧率。后续如果补充这些文件，会在这里说明。
