#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.stack import (
    CdkPythonLambdaLayersStack,
)


app = cdk.App()
CdkPythonLambdaLayersStack(
    app,
    "cdk-python-lambda-layers",
)

app.synth()
