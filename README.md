Hipku
=====

A tiny python module to encode  IPv6 and IPv4 addresses as haiku.

A port of the javascript library described at http://gabrielmartin.net/projects/hipku

Installation
============

    pip install hipku

Usage
=====

    from hipku import encode
    from ipaddress import ip_address
    
    encode(ip_address(u"254.53.93.114"))
    # 'The weary red dove\nfights in the empty tundra.\nJasmine petals dance.'
    
    decode("Wrong rams and numb wraiths\ndrown proud pink rich ace ace ants.\nAce ants aid ace ants.")
    # ip_address(u"fdae:85fd:579a:8da5:0:0:0:0")

`encode()` takes an `ip_address` object from the `ipaddress` module, available in python 3.3+ in the stdlib or
 available from pip as a backported library (and included in the requirements for python 2.7 - python 3.2.
 
`decode()` takes a string and returns an `ip_address` object. It ignores all punctuation and treats all whitespace 
identically. Both the following invocations return the same result.

    decode("Wrong rams and numb wraiths\ndrown proud pink rich ace ace ants.\nAce ants aid ace ants.")
    # ip_address(u"fdae:85fd:579a:8da5:0:0:0:0")

    decode("Wrong rams and numb wraiths drown proud pink rich ace ace ants Ace ants aid ace ants")
    # ip_address(u"fdae:85fd:579a:8da5:0:0:0:0")


