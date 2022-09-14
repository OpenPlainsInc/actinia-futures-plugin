#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018-present mundialis GmbH & Co. KG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Add endpoints to flask app with endpoint definitions and routes
"""

__license__ = "GPLv3"
__author__ = "Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2022 mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH % Co. KG"


from actinia_futures_plugin.api.calibration import Calibration
from actinia_futures_plugin.api.demand import Demand
from actinia_futures_plugin.api.helloworld import HelloWorld
from actinia_futures_plugin.api.ingest import Ingest
from actinia_futures_plugin.api.predictors import Predictors
from actinia_futures_plugin.api.info import Info
from actinia_futures_plugin.api.potential import Potential
from actinia_futures_plugin.api.pressure import Pressure
from actinia_futures_plugin.api.run import Run
# endpoints loaded if run as actinia-core plugin as well as standalone app


def create_endpoints(flask_api):

    apidoc = flask_api

    apidoc.add_resource(HelloWorld, "/helloworld")
    apidoc.add_resource(Ingest, "/futures")
    apidoc.add_resource(Info, "/futures/")
    apidoc.add_resource(Predictors, "/futures/<string:model_id>/predictors")
    apidoc.add_resource(Pressure, "/futures/<string:model_id>/pressure")
    apidoc.add_resource(Potential, "/futures/<string:model_id>/potential")
    apidoc.add_resource(Demand, "/futures/<string:model_id>/demand")
    apidoc.add_resource(Calibration, "/futures/<string:model_id>/calibration")
    apidoc.add_resource(Run, "/futures/<string:model_id>/run")
    # apidoc.add_resource(Render, "/futures/<string:model_id>/render")
