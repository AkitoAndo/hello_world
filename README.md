# AWS CDK Hello World プロジェクト

## リポジトリ

- GitHub: [https://github.com/AkitoAndo/hello_world](https://github.com/AkitoAndo/hello_world)

## プロダクト

- ウェブサイト: [http://helloworldcdkstack-helloworldbucketd435d97f-exmkxgnrymxf.s3-website-ap-northeast-1.amazonaws.com](http://helloworldcdkstack-helloworldbucketd435d97f-exmkxgnrymxf.s3-website-ap-northeast-1.amazonaws.com)

このプロジェクトは、AWS CDK を使用してシンプルな Hello World ウェブサイトを構築するためのサンプルプロジェクトです。

## 概要

AWS CDK を使用して、以下の AWS リソースを構築します：

- S3 バケット（静的ウェブサイトホスティング用）
- 必要な IAM ロールとポリシー

## プロジェクト構造

```
hello_world/
├── .venv/                    # Python仮想環境
├── docs/                     # ドキュメント
│   ├── workflow.md          # 作業の流れ
│   ├── project_structure.md # プロジェクト構造の説明
│   └── improvements.md      # 改善点と注意事項
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

## 前提条件

- Python 3.8 以上
- AWS CLI
- 適切な AWS 認証情報
- Node.js v20 以上（推奨）

## セットアップ手順

1. プロジェクトの初期化

   ```bash
   # プロジェクトルートディレクトリに移動
   cd /d D:\ProjectList\hello_world

   # 仮想環境の作成と有効化
   python -m venv .venv
   .venv\Scripts\activate

   # 依存関係のインストール
   pip install -r requirements.txt
   ```

2. AWS 認証情報の設定

   - AWS CLI のインストール
   - IAM ユーザーの作成と必要なポリシーの設定
   - `.env`ファイルの作成

3. CDK のセットアップ

   ```bash
   cdk bootstrap --no-container-assets
   ```

4. デプロイ

   ```bash
   cdk deploy
   ```

5. コンテンツのアップロード
   ```bash
   aws s3 cp static/index.html s3://<bucket-name>/index.html
   ```

## ドキュメント

- [作業の流れ](docs/workflow.md): プロジェクトのセットアップからデプロイまでの詳細な手順
- [プロジェクト構造](docs/project_structure.md): プロジェクトのファイル構成と各ファイルの役割
- [改善点と注意事項](docs/improvements.md): プロジェクトの改善点と注意すべき点

## 注意事項

- 本プロジェクトは学習目的のサンプルです
- 本番環境では、より厳密な IAM ポリシーを設定することを推奨します
- Node.js のバージョンに関する警告が表示される場合があります（v18 は 2025 年 4 月 30 日にサポート終了）

## ライセンス

MIT License
