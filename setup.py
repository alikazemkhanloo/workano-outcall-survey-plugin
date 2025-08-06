#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='workano-outcall-survey-plugin',
    version='1.0',
    description='workano otp request plugin',
    author='workano team',
    author_email='info@workano.com',
    packages=find_packages(),
    url='https://workano.com',
    include_package_data=True,
    package_data={
        'workano_outcall_survey_plugin': ['api.yml'],
    },

    entry_points={
        'wazo_confd.plugins': [
            'workano_outcall_survey_plugin = workano_outcall_survey_plugin.plugin:Plugin'
        ]
    }
)
