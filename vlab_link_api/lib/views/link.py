# -*- coding: UTF-8 -*-
"""
Defines API for '/api/1/link' end point
"""
import hashlib
from collections import deque

import ujson
from flask import redirect, request, url_for
from flask_classy import route
from vlab_api_common import BaseView, describe, get_logger, validate_input
from vlab_api_common.http_auth import requires

from vlab_link_api.lib import const

logger = get_logger(__name__, loglevel=const.LINK_LOG_LEVEL)



class LinkView(BaseView):
    """End point for the Links URL shortner"""
    route_base = '/api/1/link'
    STORED_LINKS = deque(maxlen=const.LINK_MAX_COUNT)
    POST_SCHEMA = {"$schema" : "http://json-schema.org/draft-04/schema#",
                   "type" : "object",
                   "properties" : {
                       "url" : {
                         "type" : "string",
                         "description" : "The URL you'd like a shorter version of"
                       }
                    },
                    "required" : [ "url" ]
                  }

    @requires(verify=False)
    @describe(post=POST_SCHEMA)
    def get(self, *args, **kwargs):
        """This end point only exists so users can obtain the API schema"""
        token = kwargs.get('token')
        return ujson.dumps({'error': 'GET method is only used with param describe',
                            'next': [url_for('LinkView:get', describe=True)],
                            'user': token.get('username')}), 405

    @route('/<lid>', methods=['GET'])
    def get_link(self, lid, *args, **kwargs):
        """End point for URL link redirects

        If a supplied Link ID (lid) is within the ring buffer, this end point
        will issue a perminate redirect to the assocaited URL.
        """
        resp = {}
        LINK_ID = 0
        LINK = 1
        # STORED_LINKS is a deque of tuples
        for item in self.STORED_LINKS:
            if item[LINK_ID] == lid:
                url = item[LINK]
                return redirect(url, code=301)
        else:
            resp['error'] = 'Unknown or expired link'
            resp['params'] = {'lid' : lid}
            return ujson.dumps(resp), 404

    @requires(verify=False)
    @validate_input(schema=POST_SCHEMA)
    def post(self, *args, **kwargs):
        """Create a new shortend URL"""
        resp = {'user' : kwargs['token']['username']}
        link_hash = hashlib.md5()
        link_hash.update(kwargs['body']['url'].encode('utf-8'))
        link_id = link_hash.hexdigest()
        self.STORED_LINKS.append((link_id, kwargs['body']['url']))
        new_link = const.VLAB_URL + self.route_base + '/' + link_id
        resp['content'] = {'url' : new_link, 'lid' : link_id}
        return ujson.dumps(resp)
