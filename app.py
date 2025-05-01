#!/usr/bin/env python3
import aws_cdk as cdk
from hello_world_cdk.hello_world_cdk_stack import HelloWorldCdkStack

app = cdk.App()
HelloWorldCdkStack(app, "HelloWorldCdkStack")
app.synth() 