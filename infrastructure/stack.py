from aws_cdk import Stack, aws_lambda
from constructs import Construct
import os


class CdkPythonLambdaLayersStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_a = aws_lambda.Function(
            self,
            "LambdaA",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            handler="main.handler",
            code=aws_lambda.Code.from_asset(os.path.join("lambda", "echo")),
        )

        # Define the Lambda for function B
        lambda_b = aws_lambda.Function(
            self,
            "LambdaB",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            handler="main.handler",
            code=aws_lambda.Code.from_asset(os.path.join("lambda", "echo2")),
        )

        shared_layer = aws_lambda.LayerVersion(
            self,
            "SharedLayer",
            code=aws_lambda.Code.from_asset(os.path.join("lambda_dependencies")),
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_12],
            description="A layer with shared dependencies for Lambda functions",
        )

        # Attach the layer to the Lambdas
        lambda_a.add_layers(shared_layer)
        lambda_b.add_layers(shared_layer)
