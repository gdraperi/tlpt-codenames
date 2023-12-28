import random

if __name__ == "__main__":
    print('start')

    with open(r"adjectives.txt", 'r') as fp:
        adj_list = fp.readlines()
        x = len(adj_list)
        adj = adj_list[random.randint(0,x)].strip()
    fp.close()
 
    with open(r"animals.txt", 'r') as fp:
        animals_list = fp.readlines()
        x = len(animals_list)
        animal = animals_list[random.randint(0,x)]
    fp.close()
    print(adj + " " + animal)
    print('end')