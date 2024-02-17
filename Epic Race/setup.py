from setuptools import setup, find_packages

setup(
    name='Epic Race',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'play-epic-race=epicrace.play_epic_race:cli',
        ],
    },
)
