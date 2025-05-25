# 開発ガイド

## 環境セットアップ

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. 開発サーバーの起動
```bash
streamlit run src/main.py
```

### 3. アクセス
ブラウザで `http://localhost:8501` にアクセスしてください。

## 開発ルール

### コーディング規約
- Python: PEP 8に準拠
- JavaScript: ES6+の使用
- ファイル名: スネークケース（Python）、キャメルケース（JavaScript）

### ファイル構成
- **main.py**: アプリケーションのエントリーポイント
- **pages/**: 各ページのPythonファイル
- **components/**: 再利用可能なコンポーネント
- **utils/**: ヘルパー関数とユーティリティ
- **static/**: CSS、JavaScript、画像などの静的ファイル

### コミット規約
- feat: 新機能の追加
- fix: バグ修正
- docs: ドキュメントの更新
- refactor: リファクタリング
- test: テストの追加・修正

## 新機能の追加手順

### 1. ページの追加
1. `src/pages/` に新しいPythonファイルを作成
2. `src/main.py` にページを登録
3. ナビゲーションメニューに追加

### 2. コンポーネントの追加
1. `src/components/` に新しいコンポーネントを作成
2. 必要に応じてドキュメントを更新

### 3. スタイルの追加
1. `static/css/` にCSSファイルを作成
2. `main.py` でスタイルをロード

## デバッグとテスト

### ログ出力
```python
import streamlit as st
st.write("デバッグ情報:", variable)
```

### エラーハンドリング
```python
try:
    # 処理
    pass
except Exception as e:
    st.error(f"エラーが発生しました: {e}")
```

## 本番環境への展開

### 1. 環境変数の設定
必要に応じて環境変数を設定してください。

### 2. 依存関係の確認
```bash
pip freeze > requirements.txt
```

### 3. デプロイ
Streamlit Cloud、Heroku、AWS等へのデプロイが可能です。