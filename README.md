# Data Processing in AWS

This repository showcases the capabilities of serverless stacks for data
processing on AWS. It demonstrates a theoretical service acting as a log
aggregator. Other services can send logs through an API endpoint, which this
service aggregates using Lambdas and Athena. This allows for querying the
logs, generating alarms, and performing data analysis.

## Pre-commit config

The aim of this configuration is to have some automatic code format check
every time we run the git commit command.


- Install pre-commit:

  ```
  pip install pre-commit
  ```

- Update the repositories:

  ```
  pre-commit autoupdate
  ```

- Install the git hooks:

  ```
  pre-commit install
  ```

## Deployment

```
sam build
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```
