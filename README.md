# Desktop Forge — Press Kit

『Desktop Forge』のプレスキット。GitHub Pages で公開している。

**公開 URL: https://xz585a.github.io/desktop-forge-presskit/**

この URL は3回のプレスリリースすべてで使い回す。**変えない。**

## 言語切り替え

ページ右上のボタンで日本語と英語を切り替える。**本文だけでなく、素材のキャプションや
ボタンのラベルも含めて全体が切り替わる。**

- 初期表示はブラウザの言語設定で決まる（日本語環境なら日本語、それ以外は英語）
- 選んだ言語は `localStorage` に保存され、次回以降そちらで開く
- JS が無効な場合は両言語とも表示される（情報が消えないことを優先）

**テキストを追加するときは、必ず日英の両方を書く。** 片方だけ書くと、その言語では
何も表示されない。マークアップは `class="l-ja"` / `class="l-en"` の対で置く。

```html
<figcaption><span class="l-ja">図鑑</span><span class="l-en">The codex</span></figcaption>
```

## 中身

```text
.
├── index.html          プレスキット本体（日英を1ページに併記）
├── fact_sheet_ja.txt   日本語のファクトシート（配布用テキスト）
├── fact_sheet_en.txt   英語のファクトシート
├── assets/
│   ├── images/         スクリーンショット、ロゴ、カプセル画像
│   ├── gifs/           GIF・ループ動画
│   └── video/          トレーラーの mp4  ※Git 管理外
└── downloads/          一括ダウンロード用の zip  ※Git 管理外
```

場面の番号と名前は、ゲーム本体側の `marketing/施策/撮影リスト.md` の表に合わせる。
例: `03_appraisal_en.png` / `loop_appraisal.mp4`。

**言語の書き方だけは手元と違う。**ここは `_en` / `_ja`、手元の素材フォルダは
Steam の言語コードに合わせた `_english` / `_japanese`（`03_鑑定画面_english.png`）。
**ここのファイル名は公開URLとして固定しているので変えない。**持ち込むときにリネームする。

## 現在の収録物

- スクリーンショット **10場面 × 日英 = 20枚**（1920×1080、全て無加工の PNG）
  - 言語切り替えに連動し、日本語表示なら日本語UI、英語表示なら英語UIの画が出る
- ループ動画 **7場面 = 11ファイル**（mp4、無音）
  - 鑑定・個性・冒険者の出撃・冒険ログの4場面は、`_ja` を付けた日本語UI版も置いてあり、言語切り替えに連動する
  - 全体像・工房作業・感情アイコンの3場面は文字が出ないため、日英で同じファイルを使う
- トレーラー（mp4、71MB。2026-08-12 の英語版）
- ファクトシート 日英
- 一括ダウンロード用 zip（47MB。トレーラーは容量の都合で含めない）

不足しているもの。

- **ロゴ（透過PNG）。** 現状はゲームアイコンを流用している

## 配布アセットの置き場

**zip とトレーラーの mp4 は、リポジトリに入れない。** GitHub Releases の `assets`
タグへ置き、ページからはそこへリンクする。

```text
https://github.com/xz585a/desktop-forge-presskit/releases/download/assets/DesktopForge_PressKit.zip
https://github.com/xz585a/desktop-forge-presskit/releases/download/assets/DesktopForge_Trailer.mp4
```

理由は、**この2つだけが繰り返し差し替わるうえに大きい**こと。Git はバイナリの差分を
持てないので、作り直すたびに丸ごと履歴へ積み上がり、あとから減らせない。
実際、zip は4回作り直した時点で履歴に129MB、トレーラーは1回の差し替えで137MB を占めていた。

更新は**同じファイル名で上書き**する。URL が変わらない。

```bash
gh release upload assets downloads/DesktopForge_PressKit.zip --clobber
```

スクリーンショットの PNG とループ動画は、これまでどおり Git で管理する。
配布物そのもので、差し替えの頻度も低いため。**ただしコミットするのは公開する確定版だけ**にする
（撮り直しの途中経過を入れると、上と同じことが起きる）。

### 画像形式と、原寸／縮小版の分担

配布する原寸は **PNG。**ドット絵は輪郭がはっきりしているため、JPEG の圧縮では色の
にじみが出る。編集部は記事用に一部を切り出して拡大するので、そこで粗が見える。
ShareX は「ファイルサイズが一定を超えたら別形式で保存する」設定があるため、
**その閾値を外して常に PNG で保存する。**

原寸を一覧に並べるとページが数十MBになり、回線の細い環境では開かれずに閉じられる。
そこで**表示と配布を分けている。**

| 置き場 | 形式 | 役割 |
| --- | --- | --- |
| `assets/images/` | PNG（原寸 1920×1080） | クリック時のリンク先。zip の中身。**これが配布物** |
| `assets/thumbs/` | WebP（幅960px） | 一覧表示のみ。1枚 50〜150KB |

縮小版は手で作らない。**スクリーンショットを差し替えたら `build_thumbs.py` を実行する。**

```bash
python build_thumbs.py
```

原寸が消えた分の縮小版は自動で削除される。`assets/thumbs/` を直接編集しない。

## zip の作り直し

素材を追加・差し替えたら zip も作り直し、**Releases へ上書きアップロードする**（下のコマンドの最終行）。
zip 自体はコミットされない。

```bash
python - <<'EOF'
import zipfile, os
out = "downloads/DesktopForge_PressKit.zip"
os.path.exists(out) and os.remove(out)
z = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
for f in ["fact_sheet_ja.txt", "fact_sheet_en.txt"]:
    z.write(f, "DesktopForge_PressKit/" + f)
for sub in ["assets/images", "assets/gifs"]:
    for f in sorted(os.listdir(sub)):
        if not f.startswith("."):
            z.write(os.path.join(sub, f), "DesktopForge_PressKit/" + sub.split("/")[1] + "/" + f)
z.close()
EOF
gh release upload assets downloads/DesktopForge_PressKit.zip --clobber
```

## 素材を追加したときの手順

1. ファイルを `assets/images/`（原寸）へ置く。命名は `<番号>_<名前>_<言語>.png`
2. `python build_thumbs.py` を実行して縮小版を作り直す
3. `index.html` の対応する `<figure>` のパスを確認する（拡張子が変わった場合は直す）
4. zip を作り直し、Releases へ上書きアップロードする（下記）
5. コミットして push する。GitHub Pages への反映は数十秒〜数分

ループ動画は `assets/gifs/loop_<場面>.mp4` が英語版、`loop_<場面>_ja.mp4` が日本語版。
**日本語版がある場面は `<video>` を `class="l-ja"` / `class="l-en"` の対で置く**（`figcaption` の
ダウンロードリンクも言語ごとに向き先を変える）。日本語版がない場面は `<video>` 1つのままでよい。

トレーラーを YouTube に公開したら、`index.html` の `#trailer` セクションの `<video>` を
iframe 埋め込みへ差し替える。**mp4 のダウンロードリンクは残す**（編集部が使う）。
再生を YouTube に任せられるので、Releases の mp4 はダウンロード専用になる。

## 制約

- **1ファイル 100MB まで**（Releases 側は 2GB まで）。ページに直接置く mp4 は
  20〜30MB に収め、原寸は Releases か YouTube へ逃がす
- サイト全体で 1GB まで
- **このリポジトリはパブリック。** 未公開の情報を含むファイルを置かない
