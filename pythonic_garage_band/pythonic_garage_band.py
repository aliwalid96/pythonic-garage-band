from abc import abstractmethod




class Band():
    """
        class has some class method and play solo method  
    """    
    instances=[]

    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)


    def play_solos(self):
        solos=[]
        for member in self.members:
           solos.append(member.play_solo()) 
        return solos


    def __str__(self):
      return self.name

    def __repr__(self):
        return self.name
    @classmethod
    def to_list(cls):
        return cls.instances


class Musician :
    """
        class has some method like 
        play solos   
    """
    def __init__ (self,name):
        self.name=name

    @abstractmethod
    def play_solo():
        pass
    @abstractmethod
    def get_instrument ():

        pass

        
class Guitarist(Musician):
    """
    class inherit from Musician class
    """
    def play_solo(self):
        return "face melting guitar solo"

    def get_instrument(self):
        return "guitar"
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'




class Bassist(Musician):
    """
        class inherit from Musician class

    
    """
    def __init__(self ,name):
        self.name = name

    def get_instrument(self):
        return "bass" 

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
   

    def play_solo(self):
        return "bom bom buh bom"

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):
    """
        class inherit from Musician class

    """
    def play_solo(self):
        return "rattle boom crash"

    def get_instrument(self):
        return "drums"
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'