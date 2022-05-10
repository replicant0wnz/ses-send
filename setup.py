import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ses-send",
    version=os.environ['BUILD_VERSION'],
    author="Glenn E. Bailey III",
    author_email="glenn@dronemusic.co",
    description="Simple wrapper to send emails via AWS SES",
    install_requires=['boto3', 'pyyaml'],
    license_files=['LICENSE'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/replicant0wnz/ses-send",
    project_urls={
        "Bug Tracker": "https://github.com/replicant0wnz/ses-send/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
