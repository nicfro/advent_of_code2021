from collections import defaultdict

bingo_plates = []
temp = []
with open('day4/input.txt') as f:
    counter = 0
    for line in f:
        if counter == 0:
            numbers = line.strip().split(",")
            counter += 1
        else:
            plate = line.strip().split()
            if len(plate) > 1:
                temp.append(plate)
            else:
                if len(temp) > 1:
                    bingo_plates.append(temp)
                    temp = []
    bingo_plates.append(temp)

# for storing all rows and columns
bingo_dict_rows = defaultdict(dict)
bingo_dict_columns = defaultdict(dict)

# for storing a mapping between where numbers are stored
bingo_dict_row_map =  defaultdict(list)
bingo_dict_column_map = defaultdict(list)

# creating the dictionaries
for i in range(len(bingo_plates)):
    columns = [*zip(*bingo_plates[i])]
    for j in range(len(bingo_plates[i])):
        bingo_dict_rows[i][j] = bingo_plates[i][j]
        for k in bingo_plates[i][j]:
            bingo_dict_row_map[k].append((i,j))
    for j in range(len(columns)):
        bingo_dict_columns[i][j] = list(columns[j])
        for k in columns[j]:
            bingo_dict_column_map[k].append((i,j))

bingo_row_count = defaultdict(lambda: defaultdict(int))
bingo_column_count = defaultdict(lambda: defaultdict(int))

plate_winners = set(range(len(bingo_plates)))

def find_winner():
    have_won = False
    for number in numbers:
        rows_to_check = bingo_dict_row_map[number]
        for i,j in rows_to_check:
            bingo_row_count[i][j] += 1
            bingo_dict_rows[i][j].remove(number)
            if bingo_row_count[i][j] == 5:
                if not have_won:
                    plate_winners.discard(i)
                    first_winner = 0
                    for k in bingo_dict_rows[i]:
                        first_winner += sum([int(x) for x in bingo_dict_rows[i][k]])
                    first_winner *= int(number)
                    have_won = True
                else:
                    plate_winners.discard(i)
                    if len(plate_winners) == 0:
                        last_winner = 0
                        for k in bingo_dict_rows[i]:
                            last_winner += sum([int(x) for x in bingo_dict_rows[i][k]])
                        last_winner *= int(number)
                        return first_winner, last_winner

        columns_to_check = bingo_dict_column_map[number]
        for i,j in columns_to_check:
            bingo_column_count[i][j] += 1
            bingo_dict_columns[i][j].remove(number)
            if bingo_column_count[i][j] == 5:
                
                if not have_won:
                    plate_winners.discard(i)
                    first_winner = 0
                    for k in bingo_dict_columns[i]:
                        first_winner += sum([int(x) for x in bingo_dict_columns[i][k]])
                    first_winner *= int(number)
                    have_won = True
                else:
                    plate_winners.discard(i)
                    if len(plate_winners) == 0:
                        last_winner = 0
                        for k in bingo_dict_columns[i]:
                            last_winner += sum([int(x) for x in bingo_dict_columns[i][k]])
                        last_winner *= int(number)
                        return first_winner, last_winner

    
print(find_winner())



