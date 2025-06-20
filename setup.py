from setuptools import setup, find_packages

setup(
    name="saxs_assistant",
    version="0.1.0",
    description="SAXS Assistant: Automated analysis of SAXS data including Guinier, PDDF, and ML-based Dmax prediction",
    author="Cesar Ramirez",
    author_email="youremail@example.com",  # Update this
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"saxs_assist": ["models/*.joblib"]},
    install_requires=[
        # This reads from requirements.txt
        line.strip()
        for line in open("requirements.txt")
        if line and not line.startswith("#")
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or your chosen license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
