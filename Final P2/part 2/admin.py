from PropertyManager import PropertyManagement
class admin:
    def __init__(self,Name,location,description,price_per_night,availability_status):
        self.property=PropertyManagement(Name,location,description,price_per_night,availability_status)
    def list(self):
        prop=input("Enter a number for the property it is:")
        name=input("Enter a name for the property: ") 
        loco=input("Enter the location for the property:")
        descrip=input("Enter the decription for the property:")
        pernight=input("Enter the price per night for the property:")
        availability=input("Enter the availability for the property:")
        propertynumber=prop
        prop=PropertyManagement(name,loco,descrip,pernight,availability)
        print("Property has been listed!")
a=admin.list()
