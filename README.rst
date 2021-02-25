.. image:: https://travis-ci.org/willnx/vlab_links.svg?branch=master
    :target: https://travis-ci.org/willnx/vlab_links

.. _link-service:

##############
vLab Links API
##############

The simplest URL *"shortener"* imaginable. This is only *a thing* because of how long
the VMware URLs are for their HTML VM consoles.

*************
Usage Example
*************

Remember, this is a URL *"shortener"*; so unless the supplied URL is extremely
long, the resulting URL might actually be longer.

.. code-block::

   import requests
   header = {'X-Auth': 'asdf.asdf.asdf'}
   to_shorten = 'https://my.vcenter.corp/crazy/long/url'
   resp = requests.post('https://my.vlab.corp/api/1/links',
                        json={'url': to_shorten},
                        headers=header)
   resp.json()
   {'url' : 'https://my.vlab.corp/api/1/links/asdfasdfasfasdfasdfasdfasdf'
    'lid' 'asdfasdfasfasdfasdfasdfasdf' # lid = Link ID
   }
