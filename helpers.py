ALPHAPET_LENGTH = 26
alphapet =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
statistics = [  ['e', 12.02],
                ['t', 9.10],
                ['a', 8.12],
                ['o', 7.68],
                ['i', 7.31],
                ['n', 6.95],
                ['s', 6.28],
                ['r', 6.02],
                ['h', 5.92],
                ['d', 4.32],
                ['l', 3.98],
                ['u', 2.88],
                ['c', 2.71],
                ['m', 2.61],
                ['f', 2.30],
                ['y', 2.11],
                ['w', 2.09],
                ['g', 2.03],
                ['p', 1.82],
                ['b', 1.49],
                ['v', 1.11],
                ['k', 0.69],
                ['x', 0.17],
                ['q', 0.11],
                ['j', 0.10],
                ['z', 0.07]]

def get_lines_from_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    return lines

def write_lines_to_file(filename, lines):
    output_file = open(filename, 'w')
    output_file.writelines(lines)
    output_file.close()

def calculate_similarity(array1, array2):
    if len(array1) != len(array2):
        print("lengths are not matching")
        return
    true = 0
    length = 0
    for i, j in zip(array1, array2):
        chars1 = i.split()
        chars2 = j.split()
        length += len(chars1)
        for l, m in zip(chars1, chars2):
            if l == m:
                true += 1
    return (true/length)*100

def calculate_statistics(lines):
    rank = []
    CHARACHTERS_COUNT = 0
    for i in range(ALPHAPET_LENGTH):
        rank.append([alphapet[i], 0])

    for line in lines:
        line = line.lower()
        for i in range(ALPHAPET_LENGTH):
            charachter = rank[i][0]
            charachter_count = line.count(charachter)
            rank[i][1] += charachter_count
            CHARACHTERS_COUNT += charachter_count
    
    for i in range(ALPHAPET_LENGTH):
        rank[i][1] = (rank[i][1]/CHARACHTERS_COUNT) * 100
    
    #rank the calculated statistics
    statistics = []
    for i in range(ALPHAPET_LENGTH):
        maximum = 0
        maximum_index = 0
        for j in range(ALPHAPET_LENGTH):
            if rank[j][1] >= maximum:
                maximum = rank[j][1]
                maximum_index = j
        statistics.append([rank[maximum_index][0], maximum])
        rank[maximum_index][1] = -1
    return statistics

def calculate_variance(statistics1, statistics2):
    variance = 0
    for i in range(ALPHAPET_LENGTH):
        variance += abs(statistics1[i][1] - statistics2[i][1])
    return variance
