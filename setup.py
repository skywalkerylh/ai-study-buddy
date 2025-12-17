from setuptools import setup,find_packages


# setup.py 不是用來「跑專案」的，它是用來讓「別人安裝你的程式」的。
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="LLMOPS-3",
    version="0.1",
    author="skywalkerylh, BunnyEricMarcus",
    packages=find_packages(),
    install_requires = requirements,
    python_requires=">=3.8,<3.13"
)