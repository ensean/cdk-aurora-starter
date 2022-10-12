#!/usr/bin/env python3

import aws_cdk as cdk

from aurora_bootstraper.aurora_bootstraper_stack import Aurora



app = cdk.App()
Aurora(app, "Aurora1013", env={"region":"ap-northeast-1"}, description="Aurora Cluster",
  vpc_id    = "vpc-0b8477f7051dc667e",
  subnet_ids=["subnet-02364a28c0eb3b0a9", "subnet-0da1ebe977855f2ab", "subnet-03791d25a4abf4332"]
)

app.synth()
