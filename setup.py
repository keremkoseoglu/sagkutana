""" Setup module """
import setuptools
import sagkutana

setuptools.setup(
    name="sagkutana-keremkoseoglu",
    version=sagkutana.__version__,
    author=sagkutana.AUTHOR,
    author_email=sagkutana.EMAIL,
    description=sagkutana.DESCRIPTION,
    long_description="Encryption toolkit",
    long_description_content_type="text/markdown",
    url="https://github.com/keremkoseoglu/sagkutana",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=sagkutana.PYTHON_VERSION,
    install_requires=[],
    include_package_data=True
)