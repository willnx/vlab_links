# -*- coding: UTF-8 -*-
from flask import Flask
from vlab_links_api.lib.views import LinksView, HealthView

app = Flask(__name__)
LinksView.register(app)
HealthView.register(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
