#################################################################################################################
#COMP 593    Lab 7
#
#Description:
#   Practiced creating and accessing values within a complex data structure.
#
#Usage:
#   Lab7.py
#
#History
#   Date        Author     Description    
#   2022-04-07  S.Hunter   Initial creation
###################################################################################################################

from Library import Comma_Sep_List

def main():

    Personal_Info = {
        'Name': 'Serena Hunter',
        'Student_ID': 10265447,
        'Pizza_Toppings': [
            'pineapple',
            'bacon',
            'cheese'
        ],
        'Movies': [
            {'Title': 'Mission_Impossible',
             'Genre': 'Mystery'
            },
            {'Title': 'Mara',
             'Genre': 'Horror'
            }
        ]
    }

    New_Movie = {'Title': 'Fast_and_Furious', 'Genre': 'Action'}
    Personal_Info['Movies'].append(New_Movie)

    New_Toppings = ('peppers', 'ground_beef', 'onions')
    Add_New_Toppings(Personal_Info, New_Toppings)

    Print_Sentences(Personal_Info)

    pass

def Add_New_Toppings(info_dict, Toppings):
    for T in Toppings:
        info_dict['Pizza_Toppings'].append(T)

    info_dict['Pizza_Toppings'].sort()

def Print_Sentences(info_dict):

    Sentence = 'Hi Joe, my name is ' + info_dict['Name'] + ', and my student ID is ' + str(info_dict['Student_ID']) + '.'
    print(Sentence)

    Sentence = 'My ideal pizza has '
    Sentence += Comma_Sep_List(info_dict['Pizza_Toppings'])
    Sentence += '.'
    print(Sentence)

    Genres_List = [M['Genre'] for M in info_dict['Movies']]
    Sentence = 'I like to watch '
    Sentence += Comma_Sep_List(Genres_List)
    Sentence += ' movies.'
    print(Sentence)

    Titles_List = [M['Title'].title() for M in info_dict['Movies']]
    Sentence = 'Some of my favorites are '
    Sentence += Comma_Sep_List(Titles_List)
    Sentence += '!'
    print(Sentence)

main()