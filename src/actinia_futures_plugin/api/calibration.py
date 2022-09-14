###############################################################################
# Filename: calibration.py                                                    #
# Project: OpenPlains                                                         #
# File Created: Wednesday September 14th 2022                                 #
# Author: Corey White (smortopahri@gmail.com)                                 #
# Maintainer: Corey White                                                     #
# -----                                                                       #
# Last Modified: Wed Sep 14 2022                                              #
# Modified By: Corey White                                                    #
# -----                                                                       #
# License: GPLv3                                                              #
#                                                                             #
# Copyright (c) 2022 OpenPlains                                               #
#                                                                             #
# actinia-futures-plugin is an Actinia plugin designed to                     #
# interactively run the FUTURES urban growth model developed at the           #
#  Center for Geospatial Analytics at North Carolina State Universtiy.        #
#                                                                             #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.      #
#                                                                             #
###############################################################################


__license__ = "GPLv3"
__author__ = "Corey White"
__copyright__ = "Copyright 2022 OpenPlains"
__maintainer__ = "OpenPlains"


from flask import request, make_response
from flask_restful_swagger_2 import swagger
from flask_restful_swagger_2 import Resource

from actinia_futures_plugin.apidocs import helloworld
from actinia_futures_plugin.model.response_models import (
    SimpleStatusCodeResponseModel,
)
from actinia_futures_plugin.core.example import transform_input


class Calibration(Resource):
    """Returns 'Hello world!'"""

    def __init__(self):
        self.msg = "Hello world!"

    @swagger.doc(helloworld.describeHelloWorld_get_docs)
    def get(self):
        """Get 'Hello world!' as answer string."""
        return SimpleStatusCodeResponseModel(status=200, message=self.msg)

    @swagger.doc(helloworld.describeHelloWorld_post_docs)
    def post(self):
        """Hello World post method with name from postbody."""

        req_data = request.get_json(force=True)
        if isinstance(req_data, dict) is False or "name" not in req_data:
            return make_response("Missing name in JSON content", 400)
        name = req_data["name"]
        msg = transform_input(name)

        return SimpleStatusCodeResponseModel(status=200, message=msg)
