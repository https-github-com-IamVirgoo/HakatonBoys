from .app import *
from .router import *


# Endpoints
api.add_resource(FilePoint, '/api/v1/<string:file>')