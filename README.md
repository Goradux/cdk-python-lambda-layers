# AWS CDK Python Lambda Layers with Poetry

Check the corresponding Medium article [here](https://medium.com/@goradux/aws-cdk-sharing-python-lambda-dependencies-using-poetry-lambda-layers-61e7dddf6581).

This project demonstrates how to manage and share dependencies across multiple AWS Lambda functions in a Python + AWS CDK stack using Poetry and Lambda Layers.

## Overview
AWS Lambda Layers allow multiple Lambda functions to share the same dependencies, reducing duplication and simplifying dependency management. By using a single pyproject.toml file for dependencies, we avoid maintaining separate dependency files for each Lambda. Dependencies are installed in a dedicated Lambda Layer, which is then attached to each Lambda function within the stack.

### Project Structure

```bash
.
├── lambda/
│   ├── echo/                # Lambda A code
│   │   └── main.py
│   └── echo2/               # Lambda B code
│       └── main.py
├── lambda_dependencies/     # Lambda Layer dependencies (generated)
│   └── python/              # Lambda-compatible dependencies folder
├── script.sh                # Script for exporting dependencies and installing to layer
├── pyproject.toml           # Poetry dependency file
├── app.py                   # CDK app definition
└── cdk.json                 # CDK configuration
```

### Prerequisites
AWS CDK: `npm install -g aws-cdk`
Poetry: Dependency management for Python
Python 3.12+

### Installation and Setup

Install dependencies: Use Poetry to install both runtime and development dependencies.

```bash
poetry install
```

(Optional) Prepare Lambda Layer dependencies: Run the helper script to export dependencies from Poetry and install them in the Lambda Layer folder.

```bash
./script.sh
```

Deploy the stack: The cdk.json file automates the dependency extraction and runs the CDK app.

```bash
cdk deploy
```

### Pros and Cons

#### Pros

* Centralized dependency management in pyproject.toml.
* Automatic updates to Lambda Layers during cdk synth or deploy.

#### Cons

* Applies the same Lambda Layer across functions, even if each function only uses a subset of dependencies.
* Redundant dependency installation (Poetry virtual environment and Lambda Layer).
