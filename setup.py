from setuptools import setup, find_packages

setup(
    name="token_manager",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=5.0',
        'djangorestframework>=3.14.0',
        'python-decouple>=3.8',
        'gunicorn>=21.2.0',
        'whitenoise>=6.6.0',
    ],
    python_requires='>=3.13',
)
