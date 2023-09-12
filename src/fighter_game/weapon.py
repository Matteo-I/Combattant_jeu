from random import randrange , uniform

class Weapon:
    """
    la classe d'une arme
    """
    def __init__(self,name,description,damage):
        self._name = name 
        self._description = description    
        self._ammos = randrange(1,5)
        self._damage = damage
        self._owner = 'none'
        
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
    
    def get_ammos(self):
        return self._ammos

    def get_damage(self):
        return self._damage
    
    def get_owner(self):
        return self._owner
    
    def set_owner(self,owner):
        self._owner = owner
        
    def shoot(self,fighter):
        if self._ammos > 0:
            self._ammos -= 1
            degas = int(uniform(0.7,1.0)*10+self.get_damage()/fighter.get_agility())
            fighter._healthPoints-= degas
        else:
            print('aucune munitions restantes')
        return fighter._healthPoints
    
    def summary(self):
        summary = 'Nom:'+ self.get_name() + '\n' + 'Description:'+ self.get_description() + '\n' + 'damage:' + str(self.get_damage()) + '\n' + 'ammos:' + str(self.get_ammos())
        return summary
    
bow_of_light = Weapon('Bow of light','arc de zelda',10)