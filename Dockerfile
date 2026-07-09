FROM odoo:19.0

USER root
RUN pip install pandas requests

USER odoo