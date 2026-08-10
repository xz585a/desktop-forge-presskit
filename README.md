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
│   └── video/          トレーラーの mp4（圧縮したもの）
└── downloads/          一括ダウンロード用の zip
```

ファイル名は、ゲーム本体側の `marketing/施策/撮影リスト.md` の命名に合わせる。
例: `desktop_overview_ja.png` / `loop_appraisal.gif`。

## 現在の収録物

- スクリーンショット11枚（1920×1080 PNG、**英語UIのみ**）
- ループ動画5点（mp4、無音）
- トレーラー（mp4、66MB）
- ファクトシート 日英
- 一括ダウンロード用 zip（22MB。トレーラーは容量の都合で含めない）

不足しているもの。

- **日本語UIのスクリーンショット**（国内15媒体向け。海外8媒体には英語版で足りる）
- **冒険ログ・剣の譲渡の画**。プレスリリースの一行目で使っている「渡した剣が帰ってこない」を裏付ける画がまだ無い
- ロゴ（透過PNG）。現状はゲームアイコンを流用している

## zip の作り直し

素材を追加・差し替えたら zip も作り直す。

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
```

## 素材を追加したときの手順

1. ファイルを `assets/` の該当ディレクトリへ置く
2. `index.html` の対応する `<figure>` を、プレースホルダからコメントアウトされている
   実物用のマークアップへ差し替える（各所にコメントで書いてある）
3. コミットして push する。GitHub Pages は数十秒で反映される

トレーラーを YouTube に公開したら、`index.html` の `#trailer` セクションで
placeholder を消し、`video-frame` のコメントを外して `VIDEO_ID` を差し替える。

## 制約

- **1ファイル 100MB まで。** トレーラーの mp4 は圧縮して 20〜30MB に収める。
  原寸の動画はここへ入れず、YouTube の埋め込みで見せる
- サイト全体で 1GB まで
- **このリポジトリはパブリック。** 未公開の情報を含むファイルを置かない
