from aws_cdk import (
    Stack,
    aws_s3 as _s3
)
from constructs import Construct

class MyNewProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(self,"MyNewBuckect",
                   bucket_name="demosuserdata123"
                   ,versioned=True,encryption=_s3.BucketEncryption.S3_MANAGED)
        
