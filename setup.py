import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cligon-rogercyyu",  # Replace with your own username
    version="1.0",
    author="Roger Yu",
    author_email="rogeryu27@gmail.com",
    description="A small program to check the status of URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rogercyyu/cligon-url-checker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
