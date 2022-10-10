#!/usr/bin/env python3

import aws_cdk as cdk

from aurora_bootstraper.aurora_bootstraper_stack import AuroraBootstraperStack


app = cdk.App()
AuroraBootstraperStack(app, "aurora-bootstraper")

app.synth()
