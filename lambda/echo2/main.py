from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext
from aws_lambda_powertools.utilities.data_classes import event_source, SNSEvent


@event_source(data_class=SNSEvent)
def handler(event: SNSEvent, context: LambdaContext):
    print("The incoming SNS event is:")
    print(event)
    return
