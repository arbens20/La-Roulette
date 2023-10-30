import random
import pickle
import keyboard



# Fonction pum k kreye nbre cache an
def nbr_cache(val):
    
    return random.randint(val[0], val[1])

# Fonction pum recuperer vale ki nan fichier pkl ln
def charg_joueur():
    try:
        with open('fichier_joueur.pkl', 'rb') as f:
            données = pickle.load(f)
    except (FileNotFoundError, EOFError):
        données = {}
    return données

# Fonction poum k save infos yo
def save_infos_joueur(données):
    with open('fichier_joueur.pkl', 'wb') as f:
        pickle.dump(données, f)

# Fonction poum kmnc jwe
def start_game(val, pseudo):
    nbr_machine = nbr_cache(val)
    # print(nbr_machine)
    essais_restants = 4

    print(f"Hello!!, {pseudo}! Byenvini nan LA ROULETTE HT, ou gen 4 chans pouw eseye.")

    while essais_restants > 0:
        try:
            nbr_devine = int(input(f"Mete yn nomb ki an {val[0]} ak {val[1]} : "))
        except ValueError:
            print("SVP METE YON NOMB KI VALID.")
            continue

        if nbr_devine < nbr_machine:
            print("NOMB OU METE AN TWO BA.")
        elif nbr_devine > nbr_machine:
            print("NOMB OU METE AN TWO WO.")
        else:
            score = essais_restants * 30
            print(f"Bravo, ou genyen! Le nomb kache an sete  {nbr_machine}. ou fe {score} pwen.")
            return score

        essais_restants -= 1
        print(f"CHANS OU RETE SE : {essais_restants}")

    print(f"Désolé, OU PEDI. Nomb kache an sete  {nbr_machine}.")
    return 0



def stop_game():
    global run  
    run = False
    
    
# Fonction main jwet lan
def la_roulette_ht():
    global run
    run = True 
    infos_joueurs = charg_joueur()

    while run:
        pseudo = input("METE  pseudo w : ")
        if pseudo not in infos_joueurs:
            infos_joueurs[pseudo] = 0

        score_partie = start_game((0, 100), pseudo)
        infos_joueurs[pseudo] += score_partie

        print(f" {pseudo} gen : {infos_joueurs[pseudo]} pwen")

        save_infos_joueur(infos_joueurs)

        continuer = input("OU VLE KONTINYE ? (W/N) : ")
        if continuer.lower() != "w":
            print(f"BYE BYE, {pseudo}! total pwen w se {infos_joueurs[pseudo]} .")
            break


keyboard.add_hotkey('k', stop_game)

# start
if __name__ == "__main__":
    la_roulette_ht()