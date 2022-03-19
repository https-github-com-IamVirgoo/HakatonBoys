from flask_restful import Resource


from .tools import *


class FilePoint(Resource):
    """ 
    #Endpoint:
    /api/v1/<string:file>
    #Methods
    - Get
    - Post (?)
    
    Provides endpoint for file transfering, especialy google sheets
    """
    
    
    # TODO: implement inteface which can understand what typeof file is 
    # provided
    def get(self, file: str):
        data = get_data(file)
        
        ctn = []
        for i in data.keys():
            ctn.append(i)
            ctn.append(priceCalc(i))

        
        return {
            'eur':euroActual,
            'usd':dollarActual,
            'ctn':ctn
        }