class Vehicle:
    """
    
    Vehicle is a type that describes a machine that helps us travel.

    """
  #  default_tire = 'tire'

    def __init__(self, distance_traveled=0, unit='miles'):

       self.distance_traveled = distance_traveled
       self.unit = unit 

    # @classmethod
    # def bycycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)
       

    def description(self):
       # print(f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}")
       return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"
        
        