from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    CfnOutput,
)
from constructs import Construct

class HelloWorldCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3バケットの作成（静的ウェブサイトホスティング用）
        bucket = s3.Bucket(
            self, "HelloWorldBucket",
            website_index_document="index.html",
            public_read_access=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # バケットのURLを出力
        CfnOutput(
            self, "WebsiteURL",
            value=bucket.bucket_website_url
        )
