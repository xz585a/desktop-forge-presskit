"""assets/images の原寸から、一覧表示用の縮小版を assets/thumbs へ作る。

原寸（PNG）はダウンロード用、縮小版（WebP）はページ表示用という分担にしている。
原寸を並べるとページが数十MBになり、回線の細い環境では開かれずに閉じられる。

スクリーンショットを差し替えたら、これを実行してからコミットする。

    python build_thumbs.py
"""

import glob
import os

from PIL import Image

SRC = "assets/images"
DST = "assets/thumbs"
WIDTH = 960          # 表示幅の約2倍。高DPI 環境でも粗く見えない
QUALITY = 86
SKIP = {"desktop_forge_icon.png"}


def main() -> None:
    os.makedirs(DST, exist_ok=True)

    # 原寸が消えた分の縮小版を残さない
    keep = set()

    for path in sorted(glob.glob(os.path.join(SRC, "*"))):
        name = os.path.basename(path)
        if name.startswith(".") or name in SKIP:
            continue

        stem = os.path.splitext(name)[0]
        keep.add(stem + ".webp")
        out = os.path.join(DST, stem + ".webp")

        image = Image.open(path).convert("RGB")
        height = round(image.height * WIDTH / image.width)
        image.resize((WIDTH, height), Image.LANCZOS).save(out, "WEBP", quality=QUALITY, method=6)
        print("%6.0f KB -> %5.0f KB  %s" % (
            os.path.getsize(path) / 1024, os.path.getsize(out) / 1024, stem + ".webp"))

    for path in glob.glob(os.path.join(DST, "*.webp")):
        if os.path.basename(path) not in keep:
            os.remove(path)
            print("removed stale thumb:", os.path.basename(path))


if __name__ == "__main__":
    main()
