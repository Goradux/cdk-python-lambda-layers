poetry export --without-hashes -f requirements.txt -o requirements.txt
mkdir lambda_dependencies
mkdir lambda_dependencies/python
# important that the packages reside in a folder called python!!!
# https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html
pip install -r requirements.txt -t lambda_dependencies/python --upgrade
