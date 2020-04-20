import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Freds Vietoris Rips",
    version = "0.0.1",
    author="Frederick T. Kaesmann Jr.",
    author_email="fredkaesmannjr@gmail.com",
    description="A Package for Creating Vietoris Rips Diagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ftkjr/FredsVietorisRips_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Liscence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)