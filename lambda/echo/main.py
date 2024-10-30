from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext
from aws_lambda_powertools.utilities.data_classes import event_source, SQSEvent


@event_source(data_class=SQSEvent)
def handler(event: SQSEvent, context: LambdaContext):
    print("The incoming SQS event is:")
    print(event)
    return
