import time
import random


actions_words=['say','walk','info','fight','start']
fightings_words=['hit','item','run']
locations_words=['forest','village']
items=['health_potion','mana_potion']
info_actions=['say', 'walk','sleep','items','equip']
players_weapons=["arm","sword_iron","axe_iron","spear_iron"]
players_magics=["fire","lighting"]

forest=["Wolf","Big_wolf"]

damage={"arm":1,"sword_iron":8, "axe_iron":6, "spear_iron":10,"Wolf":3, "Big_wolf":6}
stamina={"arm":0,"sword_iron":2, "axe_iron":1, "spear_iron":3,"Wolf":2,"Big_wolf":4}
enemy_stamina={"Wolf":6,"Big_wolf":16}
armor={"leather":1,"iron":2,"dragon":4,"Wolf":0,"Big_wolf":1}
health={"Wolf":20,"Big_wolf":50,"health_potion":15}
magic={"Wolf":0,"Big_wolf":0,"fire":6,"lighting":10}
mana={"Wolf":0,"Big_wolf":0,"fire":1,"lighting":3,"mana_potion":12}
XP={"Wolf":5,"Big_wolf":10}




player_location='village'
equiped_weapon='sword_iron'
equiped_magic='fire'
equiped_armor='leather'


Health_heal=40
Mana_heal=30
Stamina_heal=30



def Get_input():
    if len(inp) <=0:
        print('Try to say ":info info".')
    elif len(inp) > 2:
        print('So many words. Try command "info {}".'.format(inp[0]))
    elif len(inp)==1:
        print('Need second word.Try command "info {}".'.format(inp[0]))

class Game:
    def __init__(self,all_words,main_word):
        self.all_words=all_words
        self.main_word=main_word
    def Say(self):
        print('You said:{}'.format(sub_word))
    def Walk(self):
        print('Now going to {}'.format(sub_word))
        print('You are in the {}.'.format(sub_word))
        if sub_word=='forest':
            print('Enter ":start fighting" for battle')
    def Info(self):
        if sub_word == 'walk':
            print('village, forest - available words for "walk".')
        elif sub_word == 'info':
            print('walk, fighting - available words for "info".')
        elif sub_word == 'fighting':
            print('Useable command: change (arm, sword_iron, axe_iron or srear_iron), attack, magic, item (health_potion or mana_potion), run away. ')
        else:
            print('Unknown action word')

#Player stats
class Player:
    def __init__(self,player_health,player_weapon,player_mana,player_stamina,player_armor,player_magic,player_magic_equiped,player_xp):
        self.player_health=player_health
        self.player_weapon=equiped_weapon
        self.player_mana=player_mana
        self.player_stamina=player_stamina
        self.player_armor=player_armor
        self.player_magic=player_magic
        self.player_magic_equiped=equiped_magic
        self.player_xp=player_xp
        
    
#Enemy stats and actions
class Creatures(Player):
    def __init__(self,mob_health,mob_mana,mob_stamina,mob_attack,mob_magic,mob_armor):
        self.mob_health=mob_health
        self.mob_mana=mob_mana
        self.mob_stamina=mob_stamina
        self.mob_attack=mob_attack
        self.mob_magic=mob_magic
        self.mob_armor=mob_armor

    def Fighting(self):
        print('The battle begin.')
        random_numb=random.randint(1,10)
        if not random_numb ==1 or not random_numb ==2:
            print(comm_enemy,'appear!')
            enemy_name=comm_enemy
            enemy=Creatures(health[comm_enemy],mana[comm_enemy],enemy_stamina[comm_enemy],damage[comm_enemy],magic[comm_enemy],armor[comm_enemy])
        else:
            print(big_enemy,'appear!')
            enemy_name=big_enemy
            enemy=Creatures(health[big_enemy],mana[big_enemy],enemy_stamina[big_enemy],damage[big_enemy],magic[big_enemy],armor[big_enemy])
        def mob_crithit():
            player.player_health-=int(round(enemy.mob_attack*2))
            enemy.mob_stamina-=stamina[enemy_name]
        def mob_magic():
            player.player_health-=int(round(enemy.mob_magic))
            enemy.mob_mana-=mana[enemy_name]
        def player_hit():
            enemy.mob_health-=int(round(damage[player.player_weapon]*(1 - enemy.mob_armor/10)))
            player.player_stamina-=stamina[player.player_weapon]
        def player_criticalhit():
            enemy.mob_health-=int(round(damage[player.player_weapon]*2))
            player.player_stamina-=stamina[player.player_weapon]
            enemy.mob_stamina=stamina[enemy_name]
        def player_magic_hit():
            enemy.mob_health-=int(round(magic[player.player_magic_equiped]))
            player.player_mana-=mana[player.player_magic_equiped]
        def mob_hit():
            player.player_health-=int(round(enemy.mob_attack*(1 - player.player_armor/10)))
            enemy.mob_stamina-=stamina[enemy_name]
        while True:
            if enemy.mob_health > 0 and player.player_health > 0:
                random_numb=random.randint(1,10)
                print('HP-',player.player_health,'; Stamina-',player.player_stamina,'; Mana-',player.player_mana,'; Damage-',damage[player.player_weapon])
                print('Equiped weapon -',player.player_weapon)
                print('Enemy stats: HP-',enemy.mob_health,'; Stamina-',enemy.mob_stamina,'; Armor-',enemy.mob_armor,'; Mana-',enemy.mob_mana)
                inp=input(': ').split()   
                if len(inp)==2:
                    act_word=inp[0]
                    sub_word=inp[1]
                    #command for leave
                    if act_word== 'run' and sub_word=='away':
                        print('Leaving battle.')
                        break
                    #command for items
                    elif act_word == 'item':
                        if sub_word == 'health_potion':
                            if player.player_health < 36:
                                player.player_health+=health[sub_word]
                            else:
                                player.player_health=50
                        elif sub_word == 'mana_potion':
                            if player.player_mana < 29:
                                player.player_mana+=mana[sub_word]
                            else:
                                player.player_mana=30
                        else:
                            print('Unknown item')
                    #command for change weapon
                    elif act_word=='change':
                        if sub_word in players_weapons and not sub_word == player.player_weapon:
                            player.player_weapon=sub_word
                            print('Done.')
                        elif sub_word in players_weapons and sub_word == player.player_weapon:
                            print('You are already equip',sub_word)
                        elif sub_word not in players_weapons:
                            if sub_word in players_magics and sub_word == player.player_magic_equiped:
                                print('You are already with magic',sub_word)
                            elif sub_word in players_magics and not sub_word == player.player_magic_equiped:
                                equiped_magic=sub_word
                                player.player_magic_equiped=sub_word
                                print('Done.')
                            else:
                                print('You have no',sub_word)
                    else:
                        print('Unknown command')
                elif len(inp)==1:
                    act_word=inp[0]

                    #command for attack
                    if act_word=='attack':
                        if player.player_stamina > stamina[player.player_weapon]:
                            if random_numb == 10:
                                player_criticalhit()
                            else:
                                if enemy.mob_stamina==0:
                                    player_criticalhit()
                                else:
                                    player_hit()
                            random_numb=random.randint(1,10)
                            if random_numb == 10:
                                mob_crithit()
                            else:
                                mob_hit()
                        else:
                            print("You can't fight with this weapon. Leave this battle and restore some stramina or change weapon.")
                    #command for magic
                    if act_word=='magic':
                        if player.player_mana > mana[player.player_magic_equiped]:
                            player_magic_hit()
                        else:
                            print("You can't use this magic. Leave this battle and restore some mana or change magic.")
                else:
                    print('Unknown command.')
            elif enemy.mob_health <= 0:
                print(enemy_name,'is dead.')
                print(XP[enemy_name],'XP earned')
                player.player_xp+=XP[enemy_name]
                break
            elif player.player_health <=0:
                print("Oops, you died.")
                break

              #1-hp,  2-weapon, 3-mana,4-stamina,5-armor,   6-magic damage  7-equiped magic 78XP
player = Player(50,equiped_weapon,6,24,armor[equiped_armor],magic[equiped_magic],equiped_magic,0)

print('Try to write "info info".')

while True:
    if player.player_health > 0:
        inp = input(': ').split()
        if not len(inp)==2:
            Get_input()
        else:
            act_word = inp[0]
            sub_word = inp[1]
            if act_word in actions_words:
                talk = Game(inp,act_word)
                if act_word == 'say':
                    talk.Say()
                elif act_word=='walk':
                    if sub_word in locations_words:
                        if not player_location==sub_word:
                            player_location=sub_word
                            talk.Walk()
                        else:
                            print('You are already in {}'.format(sub_word))
                    else:
                        print('Unknown location. Try command "info location".')
                elif act_word=='info':
                    talk.Info()
                elif act_word=='start' and sub_word=='fighting':
                    if player_location=='forest':
                        comm_enemy="Wolf"
                        big_enemy="Big_wolf"
                        Creatures.Fighting(0)
                    
            else:
                print('Unknown action. Try command "info actions".')
    else:
        break
    
    
