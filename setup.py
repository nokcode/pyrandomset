import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="pyrandomset",
    version="0.1.2",
    author="Rafael Ribeiro",
    description="Generate random characters based on character set.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nokcode/pyrandomset",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
