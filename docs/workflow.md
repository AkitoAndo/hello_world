# AWS CDK Hello World プロジェクト作業記録

## 0. 前提条件

- Python 3.8 以上がインストールされていること
- AWS CLI がインストールされていること
- 適切な AWS 認証情報を持っていること

## 1. プロジェクトの初期化

- プロジェクトディレクトリの作成
  ```bash
  # プロジェクトルートディレクトリに移動
  cd /d D:\ProjectList\hello_world
  ```
- 必要なパッケージのインストール
  ```bash
  # 仮想環境の作成
  python -m venv .venv
  # 仮想環境の有効化
  .venv\Scripts\activate
  # 必要なパッケージのインストール
  pip install -r requirements.txt
  ```

## 2. プロジェクト構造の設定

- `hello_world_cdk`ディレクトリの作成
  ```bash
  # CDKアプリケーションのメインディレクトリを作成
  mkdir hello_world_cdk
  ```
- `static`ディレクトリの作成
  ```bash
  # 静的ファイル用ディレクトリを作成
  mkdir static
  ```
- 必要なファイルの作成:
  - `app.py`
  - `hello_world_cdk_stack.py`
  - `index.html`
  - `requirements.txt`
  - `cdk.json`

## 3. AWS 認証情報の設定

- AWS CLI のインストール
  ```bash
  # AWS CLIのインストール
  winget install Amazon.AWSCLI
  ```
- IAM ユーザーの作成
  - AWS マネジメントコンソールで IAM ユーザーを作成
  - アクセスキーとシークレットキーを取得
- 必要なポリシーの設定:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:*", "cloudformation:*", "iam:*", "ssm:*", "ecr:*"],
        "Resource": "*"
      }
    ]
  }
  ```
- `.env`ファイルの作成と認証情報の設定
  ```bash
  # .envファイルの作成
  echo "AWS_ACCESS_KEY_ID=your_access_key" > .env
  echo "AWS_SECRET_ACCESS_KEY=your_secret_key" >> .env
  echo "AWS_DEFAULT_REGION=ap-northeast-1" >> .env
  ```

## 4. CDK のセットアップ

- 依存関係のインストール
  ```bash
  # 仮想環境が有効化されていることを確認
  pip install -r requirements.txt
  ```
- CDK のブートストラップ
  ```bash
  # --no-container-assets: コンテナアセットを無効化し、最小限のリソースでブートストラップ
  cdk bootstrap --no-container-assets
  ```

## 5. インフラストラクチャのデプロイ

- スタックのデプロイ
  ```bash
  # スタックのデプロイ
  cdk deploy
  ```
- S3 バケットの作成と設定
- 静的ウェブサイトのホスティング設定

## 6. コンテンツのデプロイ

- `index.html`の S3 バケットへのアップロード
  ```bash
  # バケット名はデプロイ時の出力を確認
  aws s3 cp static/index.html s3://helloworldcdkstack-helloworldbucketd435d97f-exmkxgnrymxf/index.html
  ```

## 7. アクセス確認

- ウェブサイト URL: http://helloworldcdkstack-helloworldbucketd435d97f-exmkxgnrymxf.s3-website-ap-northeast-1.amazonaws.com

## 8. トラブルシューティング

### よくある問題と解決方法

1. S3 バケットが既に存在する場合

   ```bash
   # 既存のバケットを削除
   aws s3 rb s3://<bucket-name> --force
   ```

2. 権限不足の場合

   - IAM ポリシーを確認し、必要な権限を追加
   - 特に以下の権限が必要:
     - s3:\*
     - cloudformation:\*
     - iam:\*
     - ssm:\*
     - ecr:\*

3. Node.js のバージョン警告
   - v18 は 2025 年 4 月 30 日にサポート終了
   - v20 または v22 へのアップグレードを推奨

## 注意点

- Node.js のバージョンに関する警告が表示される場合があります（v18 は 2025 年 4 月 30 日にサポート終了）
- 必要に応じて、より新しいバージョン（v20 または v22）へのアップグレードを検討してください
- 本番環境では、より厳密な IAM ポリシーを設定することを推奨
