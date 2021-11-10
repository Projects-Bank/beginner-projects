# Function to build stuff
def build_spear():
    what_i_have['wood'] = what_i_have['wood'] - 2
    what_i_have['stone'] = what_i_have['stone'] - 1
    print("Hooray! You built a spear!")
    print(f'Now you have: {what_i_have}')

def build_chest():
    print("Hooray! You can build a chest!")

def check_materials(what_i_have):
    print(f'You have: {what_i_have}')
    if (what_i_have['wood'] > 2) and (what_i_have['stone'] > 1) and (what_i_have['knife'] == True):
        build_spear()
    elif (what_i_have['wood'] > 3) and (what_i_have['hammer'] == True):
        build_chest()
    else:
        print("Sorry, you can't build anything now.")

#Dictionary
what_i_have = {'wood': 35, 'stone': 2, 'knife': True, 'hammer': False}

check_materials(what_i_have)
