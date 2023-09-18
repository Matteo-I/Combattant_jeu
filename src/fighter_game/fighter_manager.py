from fighter_game.fighter import Fighter
from fighter_game.weapon import Weapon

class FighterManager :
    
    def __init__(self):
        self._fighters = []
        self._weapons = []
        
    def create_fighter(self,name,description=''):
        f = Fighter(name,description)
        self._fighters.append(f)
        return f
    
    def create_weapon(self,name,description='',damage=8,weight=2):
        w = Weapon(name,description,damage,weight)
        self._weapons.append(w)
        return w
    
    def create_fight(self,fighter1,weapon1,fighter2,weapon2):
        fighter1.take_weapon(weapon1)
        fighter2.take_weapon(weapon2)
        combattant,combattu=fighter1,fighter2
        while combattant.get_healthPoints() >0:
            combattant.attack(combattu,combattant.get_equipedWeapon())
            combattant,combattu=combattu,combattant
        return combattu
        
        
    
        
            
        
        

        
        
    
