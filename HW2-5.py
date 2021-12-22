my_list=[7, 5, 3, 3, 2]
world = int(input('ВВедите число'))

while world !=100:
    for el in range(len(my_list)):
        if my_list[el] == world:
            my_list.insert(el+1, world)
        elif my_list[0] < world:
            my_list.insert(0, world)
        elif my_list[-1] > world:
            my_list.append(world)
        elif my_list[el] > world and my_list[el+1] < world:
            my_list.insert(el+1,world)

    print(f"Рейтинг - {my_list}")


