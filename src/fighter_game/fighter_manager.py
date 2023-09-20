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
    
    def create_fight(self,combattant,combattu):
        if combattant.get_healthPoints() > 0:
            combattant.attack(combattu)
            print('pv de',combattu,combattu.get_healthPoints())
            return self.create_fight(combattu,combattant)
        else:
#             self._fighters.remove(combattant)
            return combattu

#         combattant.attack(combattu)
#         print('pv de',combattu,combattu.get_healthPoints())
#         if combattu.get_healthPoints() > 0:
#             self.create_fight(combattu,combattant)
#         else:
#             return combattant
            


#         if combattant.get_healthPoints() > 0:
#             combattant.attack(combattu)
#             print('pv de',combattu,combattu.get_healthPoints())
#             self.create_fight(combattu,combattant)
#         else:
#             return combattu
             
             
#         while combattant.get_healthPoints() >0:
#             combattant.attack(combattu)
#             combattant,combattu=combattu,combattant
#         return combattu
        
        
    
        
            
        
        

        
        
    
marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
Yves_cadour = Fighter('Yves', 'NSI chef') # on instancie avec les variables de la méthode __init__ 