from distutils.core import setup

setup(
    name='hipku',
    version='1.0',
    packages=['hipku', 'local.lib.python2.7.distutils', 'local.lib.python2.7.encodings',
              'local.lib.python2.7.site-packages.pip', 'local.lib.python2.7.site-packages.pip.vcs',
              'local.lib.python2.7.site-packages.pip._vendor', 'local.lib.python2.7.site-packages.pip._vendor.distlib',
              'local.lib.python2.7.site-packages.pip._vendor.distlib._backport',
              'local.lib.python2.7.site-packages.pip._vendor.colorama',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.trie',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.filters',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.serializer',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.treewalkers',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.treeadapters',
              'local.lib.python2.7.site-packages.pip._vendor.html5lib.treebuilders',
              'local.lib.python2.7.site-packages.pip._vendor.requests',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.chardet',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.util',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'local.lib.python2.7.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'local.lib.python2.7.site-packages.pip._vendor._markerlib',
              'local.lib.python2.7.site-packages.pip.commands', 'local.lib.python2.7.site-packages.pip.backwardcompat',
              'local.lib.python2.7.site-packages._markerlib', 'local.lib.python2.7.site-packages.setuptools',
              'local.lib.python2.7.site-packages.setuptools.tests',
              'local.lib.python2.7.site-packages.setuptools.command'],
    url='https://github.com/Drakekin/hipku',
    license='MIT License',
    author='Connor Shearwood',
    author_email='drake@lifein2d.co.uk',
    description='Convert IPv4 and IPv6 addresses into haiku'
)
