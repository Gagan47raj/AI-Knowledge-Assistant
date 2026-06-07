from datetime import datetime

class FunctionService:
    
    def get_current_time(self):

        return {"current_time" : datetime.now().strftime("%H:%M:%S")}