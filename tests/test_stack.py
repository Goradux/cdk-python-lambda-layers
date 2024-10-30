import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.stack import (
    CdkPythonLambdaLayersStack,
)


def test_lambda_created():
    app = core.App()
    stack = CdkPythonLambdaLayersStack(app, "cdk-python-lambda-layers")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {"Runtime": "python3.12"})
