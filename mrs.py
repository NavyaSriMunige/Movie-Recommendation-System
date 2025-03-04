from setuptools import mrs
with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()
AUTHOR_NAME="NavyaSri"
SRC_REPO='src'
LIST_OF_REQUIREMENTS=['streamlit']

mrs(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='navyasrimunige2003.com',
    description='A simple python package to make a simple web app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)