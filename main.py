from random import randint

# List to store all created NPCs
npc_list = []

# Player information (dictionary)
player = {
    "name": "Warrior",   #player name here.  
    "level": 1,         
    "xp": 0,              
    "max_xp": 30,         
    "hp": 100,            
    "max_hp": 100,        
    "damage": 25,         
}


#-----------------------------------------------------------------------------

# Function to create a new NPC with given level
def create_npc(level):
    new_npc = {
        "name": f"Monster #{level}",   
        "level": level,                
        "damage": 5 * level,           # NPC's attack damage(scales with level)
        "hp": 100 * level,             
        "max_hp": 100 * level,         
        "xp": 7 * level,               
    }
    return new_npc


# Function to generate multiple NPCs
def generate_npc(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npc(x + 1)    # Create NPC with level (starting from 1)
        npc_list.append(new_npc)       # Add the new NPC to the npc_list



# Function to display all NPCs in the list
def show_npc():
    for npc in npc_list:
        show_npc(npc)

def show_npc(npc):
    print(f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']}  // Hp: {npc['hp']} // Xp:{npc['xp']}")

#display player
def show_player():
    print(f"Name: {player['name']} // Level: {player['level']} // Damage: {player['damage']}  // Hp: {player['hp']}/{player['max_hp']} // Xp:{player['xp']}/{player['max_xp']}")



def reset_player():
    player['hp'] = player['max_hp']

def reset_npc(npc):
    npc['hp'] = npc['max_hp']


def level_up():
    if player['xp'] >= player['max_xp']:
        player['level'] +=1
        player['xp'] = 0 
        player['max_xp'] = player['max_xp'] *2
        player['max_hp'] += 20

# Function to start the battle
def start_battle(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        attack_npc(npc)         # Player attacks the NPC
        attack_player(npc)      # NPC attacks the player
        show_battle_info(npc)   # Display information
    if player["hp"] > 0: #player won
        print(f"the {player['name']} won and got {npc['xp']} experience points!")
        player["xp"] += npc['xp']
        show_player()
    else:
        print(f"the {npc['name']} won the battle!")
        show_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)



# Function for the player to attack the NPC
def attack_npc(npc):
    npc["hp"] = npc["hp"] - player["damage"]  #Subtract player's damage from NPC's HP



# Function for the NPC to attack the player
def attack_player(npc):
    player["hp"] -= npc["damage"]     # Subtract NPC's damage from player's HP



# Function to display current HP of both player and NPC
def show_battle_info(npc):
    print(f"Player: {player['hp']}/{player['max_hp']}")       
    print(f"NPC: {npc['name']} {npc['hp']}/{npc['max_hp']}")      
    print("--------------------------------\n")




# Generate 5 NPCs and store them in the list
generate_npc(5)

# Select the first NPC to start the battle
selected_npc = npc_list[0]

# Start the battle with the selected NPC
start_battle(selected_npc)
start_battle(selected_npc)
start_battle(selected_npc)
start_battle(selected_npc)
start_battle(selected_npc)


show_player()
