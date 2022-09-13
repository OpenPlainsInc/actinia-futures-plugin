FROM mundialis/actinia-core:latest

# pwgen is needed for the tests
RUN pip3 install pwgen

COPY docker/actinia.cfg /etc/default/actinia
COPY src /src/actinia-futures-plugin/src/
COPY setup.cfg /src/actinia-futures-plugin/
COPY setup.py /src/actinia-futures-plugin/
COPY requirements.txt /src/actinia-futures-plugin/

RUN pip3 install -r /src/actinia-futures-plugin/requirements.txt
RUN pip3 uninstall actinia-futures-plugin.wsgi -y
# SETUPTOOLS_SCM_PRETEND_VERSION is only needed if in the plugin folder is no
# .git folder
ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.0
RUN (cd /src/actinia-futures-plugin && python3 setup.py install)
