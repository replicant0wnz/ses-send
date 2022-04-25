import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ses-send-replicant0wnz",
    version="0.0.1",
    author="Glenn E. Bailey III",
    author_email="glenn@dronemusic.co",
    description="Simple wrapper to send emails via AWS SES",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/replicant0wnz/ses-send",
    project_urls={
        "Bug Tracker": "https://github.com/replicant0wnz/ses-send/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
