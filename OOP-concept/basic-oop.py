class car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.doors=4
    def drive(self,driverName,doors):
        myBrand=self.brand
        self.doors=doors
        return f"\n{driverName} start the car {doors}"
car1=car("Suzuki",230)
DriveManual=car1.drive("Waqar",3)
print(car1.brand,car1.price,car1.doors,DriveManual)

car2=car("GS 150","450k")
car2.drive("ali",6)
print(car2.doors)