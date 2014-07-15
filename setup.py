from setuptools import setup, find_packages

setup(
    name="whitelistaffilmapper",
    version="0.1.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="",
    description="Whitelist Group Affil Mapper for djangowind",
    long_description="Whitelist Group Affil Mapper for djangowind",
    install_requires = [],
    scripts = [],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    package_data = {'' : ['*.*']},
    packages=['whitelistaffilmapper'],
    test_suite='nose.collector',
    )
