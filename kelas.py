class characters:
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp
    
    def attack(self):
        print(f'{self.name} attacks with {self.atk}')
    def hit(self, dmg):
        print(f"{self.name} got hit with {dmg}")
        self.hp -= dmg
        if self.hp <= 0:
            print(f'{self.name} is dead')

# characters
player1=characters('player1',2,3)
player2=characters('player2',3,2)

player1.hit(3)