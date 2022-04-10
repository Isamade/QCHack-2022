import random
from string_comparison import StringComparator

main_database = [
    [['b', 'a', 'r', 'b'], ['b', 'a', 'l', 'd'], ['b', 'o', 'l', 'd'], ['t', 'o', 'l', 'd'], ['t', 'o', 'a', 'd'],
     ['r', 'o', 'a', 'd'], ['c', 'o', 'l', 'd'], ['l', 'o', 'a', 'd']],
    [['c', 'a', 'r', 'd'], ['c', 'o', 'r', 'd'], ['b', 'i', 'r', 'd'], ['b', 'a', 'c', 'k'],
     ['b', 'a', 'r', 'k'], ['d', 'a', 'r', 'k'], ['c', 'o', 'r', 'k'], ['d', 'o', 'r', 'c']],
    [['s', 'o', 'l', 'd'], ['s', 'o', 'd', 'a'], ['b', 'o', 'd', 'e'], ['s', 'o', 'a', 'k'], ['l', 'a', 'i', 'd'],
     ['s', 'a', 'i', 'd'], ['d', 'o', 's', 'e'], ['c', 'o', 'o', 'k']],
    [['c', 'o', 'k', 'e'], ['b', 'o', 'o', 'k'], ['c', 'o', 'o', 'l'], ['c', 'o', 'a', 'l'], ['r', 'a', 'i', 'd'],
     ['d', 'o', 'l', 'l'], ['r', 'a', 'k', 'e'], ['c', 'a', 'k', 'e']],
    [['s', 'a', 'k', 'e'], ['r', 'e', 'a', 'l'], ['r', 'o', 'l', 'e'], ['a', 'i', 'd', 'e'], ['l', 'e', 'a', 'd'],
     ['l', 'a', 't', 'e'], ['b', 'a', 't', 'e'], ['s', 'a', 't', 'e']],
    [['s', 'e', 'a', 'l'], ['b', 'a', 'l', 'l'], ['c', 'a', 'l', 'l'], ['t', 'a', 'l', 'l'], ['s', 'e', 'l', 'l'],
     ['b', 'o', 'a', 't'], ['l', 'a', 'i', 'r'], ['c', 'a', 'r', 'e']],
    [['c', 'o', 'r', 'e'], ['b', 'o', 'r', 'e'], ['b', 'e', 'a', 'r'], ['b', 'o', 'l', 't'], ['c', 'o', 'l', 't'],
     ['r', 'a', 't', 'e'], ['s', 'o', 'l', 'e'], ['c', 'o', 'a', 't']],
    [['d', 'e', 'a', 'l'], ['b', 'a', 't', 's'], ['c', 'a', 't', 's'], ['r', 'a', 't', 's'], ['l', 'a', 's', 't'],
     ['s', 'a', 'l', 't'], ['t', 'o', 'l', 'l'], ['t', 'e', 's', 't']],
    [['r', 'e', 's', 't'], ['b', 'e', 's', 't'], ['t', 'e', 'l', 'l'], ['b', 'i', 'l', 'l'], ['t', 'i', 'l', 'l'],
     ['t', 'i', 'l', 'e'], ['t', 'a', 'l', 'e'], ['t', 'a', 'k', 'e']],
    [['s', 'o', 'i', 'l'], ['l', 'o', 's', 'e'], ['o', 'i', 'l', 's'], ['t', 'a', 's', 'k'], ['b', 'a', 's', 'k'],
     ['r', 'a', 'i', 'l'], ['b', 'a', 'i', 'l'], ['d', 'i', 'a', 'l']],
    [['s', 'a', 'i', 'l'], ['c', 'o', 'd', 'e'], ['c', 'o', 's', 't'], ['s', 'o', 'c', 'k'], ['t', 'a', 'c', 'k'],
     ['t', 'e', 'a', 'l'], ['l', 'o', 's', 't'], ['t', 'o', 's', 's']],
    [['l', 'o', 's', 's'], ['b', 'a', 's', 's'], ['o', 'r', 'e', 's'], ['r', 'i', 'b', 's'], ['c', 'a', 's', 'e'],
     ['r', 'i', 's', 'e'], ['c', 'a', 'r', 's'], ['l', 'i', 's', 't']]]

if __name__ == '__main__':
    database = main_database[random.randrange(0, len(main_database), 1)]
    selected_from_database = database[random.randrange(0, len(database), 1)]
    target = []
    for value in selected_from_database:
        target.append([value])

    input_word = []
    show_database = []
    for value in database:
        show_database.append(''.join(value))
    print(show_database)
    print('A word was randomly selected from the database above; enter four letters that match the selected word')
    print('The more letters you guess right, the higher your score!')
    print('Enter your four letters')
    first_letter = input('First Letter: ')
    input_word.append(first_letter)
    second_letter = input('Second Letter: ')
    input_word.append(second_letter)
    third_letter = input('Third Letter: ')
    input_word.append(third_letter)
    fourth_letter = input('Fourth Letter: ')
    input_word.append(fourth_letter)
    print('Please wait for score')

    # Player One
    player_one_score = 0
    for i, value in enumerate(input_word):
        x = StringComparator([value], target, is_binary=False, shots=10000)
        output_hd = x.run()['hamming_distances']
        if output_hd[i] == 0:
            player_one_score = player_one_score + 1

    # Closest Word
    distances = []
    for value in database:
        x = StringComparator(value, database, is_binary=False, shots=10000)
        output_hd = x.run()['hamming_distances']
        distances.append(sum(output_hd))

    min_val = distances.index(min(distances))
    closest_word = database[min_val]

    # Player Two
    player_two_score = 0
    for i, value in enumerate(closest_word):
        x = StringComparator([value], target, is_binary=False, shots=10000)
        output_hd = x.run()['hamming_distances']
        if output_hd[i] == 0:
            player_two_score = player_two_score + 1

    print('The selected word is ' + ''.join(selected_from_database))
    print('Your score: ', player_one_score)
    print("Opponent's score:", player_two_score)
    if player_one_score > player_two_score:
        print('You Win :)')
    elif player_one_score < player_two_score:
        print('You Lose :(')
    elif player_one_score == player_two_score:
        print('There was a tie')
