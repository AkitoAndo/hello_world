# プロジェクト構造

```
hello_world/
├── .venv/                    # Python仮想環境
├── docs/                     # ドキュメント
│   ├── workflow.md          # 作業の流れ
│   └── project_structure.md # プロジェクト構造の説明
├── hello_world_cdk/         # CDKアプリケーションのメインディレクトリ
│   ├── __init__.py
│   └── hello_world_cdk_stack.py  # CDKスタックの定義
├── static/                  # 静的ファイル
│   └── index.html          # ウェブサイトのメインページ
├── .env                     # 環境変数設定
├── app.py                   # CDKアプリケーションのエントリーポイント
├── cdk.json                 # CDK設定ファイル
└── requirements.txt         # Python依存関係
```

## 各ファイルの説明

### メインファイル

- `app.py`: CDK アプリケーションのエントリーポイント
- `cdk.json`: CDK の設定ファイル
- `requirements.txt`: Python パッケージの依存関係

### CDK 関連

- `hello_world_cdk/`: CDK アプリケーションのメインディレクトリ
  - `hello_world_cdk_stack.py`: S3 バケットと CloudFront ディストリビューションの定義
  - `__init__.py`: Python パッケージとして認識させるための空ファイル

### 静的ファイル

- `static/`: ウェブサイトの静的ファイルを格納
  - `index.html`: シンプルな Hello World ページ

### 設定ファイル

- `.env`: AWS 認証情報などの環境変数
- `requirements.txt`: 必要な Python パッケージ
  - aws-cdk-lib
  - constructs

### ドキュメント

- `docs/`: プロジェクトのドキュメント
  - `workflow.md`: 作業の流れと手順
  - `project_structure.md`: プロジェクト構造の説明
