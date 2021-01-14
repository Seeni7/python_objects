class Vehicle:
    """
    
    Vehicle is a type that describes a machine that helps us travel.

    """

    def __init__(self, engine, tires):

       self.engine = engine
       self.tires = tires 
       

    def description(self):
        print(f"A vehicle with an {self.engine} engine and {self.tires} tires")
        
        