from random import randrange , uniform
from fighter_game.weapon import Weapon

class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._agility = randrange(1,9)
        self._healthPoints = 100 # Lors de la création d'une instance, les points de vie valent 100.
        self._equipedWeapon = 'none'
            
    def get_name(self):
        """
        Retourne le nom du combattant.
        """
        return self._name
    
    def get_description(self):
        """
        Retourne la description du combattant.
        """
        return self._description
    
    def set_description(self, description):
        """
        Affecte la description du combattant.
        
        """
        self._description=description
    
    def get_agility(self):
        return self._agility
    
    def get_healthPoints(self):
        return self._healthPoints
    
    def get_strenght(self):
        return(10-self._agility)
    
    def get_equipedWeapon(self):
        return self._equipedWeapon
    
    def set_weapon(self,weapon):
        self._equipedWeapon = weapon
    
    def take_weapon(self,weapon):
        if self.get_equipedWeapon() == 'none' and weapon.get_owner() == 'none':
            self.set_weapon(weapon.get_name())
            weapon.set_owner(self.get_name())
        else:
            if self.get_equipedWeapon() == 'none':
                print("cette arme est deja equiper par quelqu'un d'autre")
            else:   
                print(self.get_name(),'a deja une arme equiper')
        return self.get_equipedWeapon()
            
    
    def punch(self,fighter):
       '''
        permet au fighter a de punch un fighter b
        calcule la vie perdu du fighter b en fonction de la force du fighter a et de l'agilité du fighter b et d'un peu d'aleatoire
        '''
       points=int(uniform(0.7,1.0)*10+self.get_strenght()/fighter.get_agility())
       fighter._healthPoints-=points
       return fighter._healthPoints
    
    def summary(self):
        summary = 'Nom:'+ self.get_name() + '\n' + 'Description:'+ self.get_description() + '\n' + 'Points de vie:' + str(self.get_healthPoints()) + '\n' + 'Agilité:' + str(self.get_agility()) + '\n' + 'Force:' + str(self.get_strenght()) + '\n' + 'Arme:'+ self.get_equipedWeapon()
        return summary

marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
Yves_cadour = Fighter('Yves_cadour', 'NSI chef') # on instancie avec les variables de la méthode __init__