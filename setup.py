from setuptools import setup, find_packages

setup(
    name='todo_api',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'annotated-types==0.7.0',
        'blinker==1.9.0',
        'cachelib==0.13.0',
        'click==8.1.8',
        'exceptiongroup==1.2.2',
        'Flask==3.1.0',
        'Flask-Caching==2.3.1',
        'Flask-JWT-Extended==4.7.1',
        'greenlet==3.1.1',
        'iniconfig==2.1.0',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.6',
        'MarkupSafe==3.0.2',
        'packaging==24.2',
        'passlib==1.7.4',
        'pluggy==1.5.0',
        'pydantic==2.11.0',
        'pydantic_core==2.33.0',
        'PyJWT==2.10.1',
        'pytest==8.3.5',
        'python-dotenv==1.1.0',
        'SQLAlchemy==2.0.40',
        'tomli==2.2.1',
        'typing-inspection==0.4.0',
        'typing_extensions==4.13.0',
        'Werkzeug==3.1.3',
        'pydantic-settings==2.2.1'
    ]
)
