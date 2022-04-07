


def main():
    
    info_data = {
        'name': "Ben",
        'student_id': 10180039,
        'pizza_toppings': [
            "pepperoni",
            "bacon",
            "chilli flakes",
        ],
        'movies': [
            {'title': "Oldboy",
             'genre': "Mystery",
            },
            {'title': "Godzilla",
             'genre': "Kaiju",
            },
        ],
    }

    new_movie =  {'title': "Robocop", 'genre': "Action"}
    info_data['movies'].append(new_movie)

    more_toppings = ("sausage", "extra cheese")
    add_more_toppings(info_data, more_toppings)

    print_my_info(info_data)

    pass

def add_more_toppings(info_data, more_toppings):

    for t in more_toppings:
        info_data['pizza_toppings'].append(t)
        info_data['pizza_toppings'].sort()

def print_my_info(info_data):

    print("Hi Jeremy, my name is", info_data['name'], "and my student ID is", info_data['student_id'],end=".\n")

    print("My ideal pizza has ", end='')
    for i,g in enumerate(info_data['pizza_toppings']):
        if i < len(info_data['pizza_toppings']) - 1:
            print(g, end=', ')
        else:
            print(g, end='.\n')

    print("I like to watch ", end='')
    for i,g in enumerate(info_data['movies']):
        if i < len(info_data['movies']) - 1:
            print(g['genre'], end=', ')
        else:
            print(g['genre'], end='.\n')

    print("Some of my favourites are ", end='')
    for i,g in enumerate(info_data['movies']):

        if i < len(info_data['movies']) - 1:
            print(g['title'], end=', ')
        else:
            print(g['title'], end='!\n')

main()