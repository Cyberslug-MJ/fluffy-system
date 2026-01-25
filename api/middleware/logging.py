import logging
import time
from logtail import LogtailHandler

token = 'rKnyVjY8n3kBGYnJ8L84F8wj' # token for BetterStack
betterstack_handler = LogtailHandler(source_token=token)

# we'll define our logger object here 
logger = logging.getLogger(__name__)
handler = logging.StreamHandler() # outputs the logs to the terminal by default
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s; %(message)s") # defines the output format of our logs 
# the output of the formatter would be something like [time WARNING 200OK] or such

handler.formatter = formatter #- makes sense to format our output by the formatter
logger.addHandler(handler) #- we pass our hander to our logger 
logger.addHandler(betterstack_handler)
logger.setLevel(logging.INFO) # this means any log that has a level that is greater than or equal to INFO will be outputted by our logger


class LoggingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    
    def __call__(self,request):
        # logic to be executed before the request hits the view or any other middleware goes here.

        start_time = time.time()
        request_data = {
            "method":request.method,
            "ip_address":request.META.get('REMOTE_ADDR'),
            "path":request.path
        }
        logger.info(request_data,extra=request_data)

        response = self.get_response(request)

        #logic executed after the view is called goes here 
        duration = time.time() - start_time 
        response_dict = {
            "status_code":response.status_code,
            "duration":duration
        }
        logger.info(response_dict,extra=response_dict)

        return response

