# Data Processing in AWS

This repository showcases the capabilities of serverless stacks for data
processing on AWS. It demonstrates a theoretical service acting as a log
aggregator. Other services can send logs through an API endpoint, which this
service aggregates using Lambdas and Athena. This allows for querying the
logs, generating alarms, and performing data analysis.
