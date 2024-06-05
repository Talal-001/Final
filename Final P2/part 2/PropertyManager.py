#2
class PropertyManagement:
    def __init__(self,Name,Id,
                 location,description,price_per_night,availability_status):
        self.Id=Id
        self.Name=Name
        self.location=location
        self.description=description
        self.pricepernight=price_per_night
        self.availability_status=availability_status
    def get(self):
        print(self.Id,self.Name,self.location,self.description,self.pricepernight,self.availability_status)
