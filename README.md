# Desktop Forge — Press Kit

『Desktop Forge』のプレスキット。GitHub Pages で公開している。

**公開 URL: https://xz585a.github.io/desktop-forge-presskit/**

この URL は3回のプレスリリースすべてで使い回す。**変えない。**

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
