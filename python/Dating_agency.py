
sailors = ['Adrian', 'Caspian', 'Dune', 'Finn', 'Fisher', 'Heron', 'Kai',
           'Ray', 'Sailor', 'Tao']

ladies = ['Ariel', 'Bertha', 'Blue', 'Cali', 'Catalina', 'Gale', 'Hannah',
           'Isla', 'Marina', 'Shelly']

def isnicegirl(s):
    return ord(s[0]) % 2 == 0

def islovable(slady, ssailor):
    return ord(slady[-1]) % 2 == ord(ssailor[-1]) % 2

for lady in ladies:
    if isnicegirl(lady):
        print("Dating service should offer a date with", lady)
        for sailor in sailors:
            if islovable(lady, sailor):
                print("    Sailor", sailor, "should take an offer to date her.")
    else:
        print("Dating service should NOT offer a date with", lady)
