from setuptools import setup, find_packages
from BardAssistant.__version__ import __core__

with open("requirements.txt") as requirements_txt:
    requirements = requirements_txt.read().splitlines()

setup(
    name="BardAssistant",
    version=__core__,
    author="d3m0n@demonkingswarn",
    author_email="demonkingswarn@protonmail.com",
    description="Google Bard based Voice Assistant",
    packages=find_packages(),
    url="https://github.com/DemonKingSwarn/BardAssistant",
    keywords=[
        "bard",
        "voice assistant",
        "generative AI"
    ],
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        BardAssistant=BardAssistant.__main__:__bard__
    """,
    include_package_data=True,
)
