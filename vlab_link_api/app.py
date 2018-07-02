# -*- coding: UTF-8 -*-
from flask import Flask
from vlab_link_api.lib.views import LinkView, HealthView

app = Flask(__name__)
LinkView.register(app)
HealthView.register(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
