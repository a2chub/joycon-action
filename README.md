# Joycon Action

Streamlitを使用したWebアプリケーションです。

## 概要

このプロジェクトは、Pythonとmini JavaScript を使用してブラウザ内で動作するWebアプリケーションを提供します。Streamlitフレームワークを基盤とし、モジュラーで拡張可能な設計を採用しています。

## 技術スタック

- **バックエンド**: Python 3.8+
- **フロントエンド**: Streamlit + JavaScript
- **データ処理**: Pandas, NumPy
- **可視化**: Plotly, Altair

## プロジェクト構造

```
joycon-action/
├── docs/                    # ドキュメント
│   ├── architecture.md      # アーキテクチャ設計
│   ├── development.md       # 開発ガイド
│   └── api.md              # API仕様
├── src/                     # ソースコード
│   ├── main.py             # メインアプリケーション
│   ├── components/         # 再利用可能コンポーネント
│   └── utils/              # ユーティリティ関数
├── static/                  # 静的ファイル
│   ├── css/                # スタイルシート
│   └── js/                 # JavaScript
├── requirements.txt         # 依存関係
└── README.md               # このファイル
```

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. アプリケーションの起動

```bash
streamlit run src/main.py
```

### 3. アクセス

ブラウザで http://localhost:8501 にアクセスしてください。

## 機能

### 現在の機能
- Hello World表示
- インタラクティブなUI
- ナビゲーションシステム
- レスポンシブデザイン
- チャート表示デモ

### 今後の予定
- ユーザー認証機能
- データベース連携
- API統合
- カスタムコンポーネント

## 開発

### 開発環境の準備

1. Python 3.8以上をインストール
2. 仮想環境の作成（推奨）:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # または
   venv\Scripts\activate  # Windows
   ```
3. 依存関係のインストール:
   ```bash
   pip install -r requirements.txt
   ```

### 新機能の追加

1. `src/components/` に新しいコンポーネントを作成
2. `src/main.py` にページを追加
3. 必要に応じて `docs/` 内のドキュメントを更新

詳細な開発ガイドは `docs/development.md` を参照してください。

## ドキュメント

- [アーキテクチャ設計](docs/architecture.md)
- [開発ガイド](docs/development.md)
- [API仕様](docs/api.md)

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プロジェクトへの貢献を歓迎します。バグレポートや機能要求は、GitHubのIssueを通じてお知らせください。

## サポート

技術的な質問や問題については、開発チームまでお問い合わせください。