import itertools

def get_3333() -> dict:
    """
    x - y = 3333 になる全ての組み合わせを取り出す
    x,yは4桁の数字である
    """

    numbers = [1,2,3,4,5,6,7,8,9]
    left_permutation = list(itertools.permutations(numbers, 5)) #numbersからとれる5桁の数
    right_permutation = list(itertools.permutations(numbers, 4)) #numbersからとれる4桁の数
    correct_combos = {}
    
    for i in left_permutation:
        left_number = int(''.join(map(str, i)))
        for j in right_permutation:
            right_number = int(''.join(map(str, j)))
            if left_number - right_number == 33333: #left_number - right_number == 33333の場合dictionaryに入れる
                correct_combos[left_number] = right_number

    filtered = filter(filter_dupes, correct_combos.items())
    
    return dict(filtered) #left_numberとright_numberのセットをdictionaryに入れる

def filter_dupes(d) -> bool:
    """
    同じ数字があればFalseで返す
    """
    both = str(d[0]) + str(d[1])
    condition = len(set(both)) == len(list(both))
    return condition

def format_output(combos: dict):
    """
    x-y = 33333 となるためのoutput用の関数
    「当てはまる数字の組み合わせ
    　左の数字: ○○○○○
    　右の数字: ○○○○」
    """
    print("当てはまる数字の組み合わせ")
    
    number_of_combos = 0

    for left_number, right_number in combos.items(): 
        number_of_combos +=1
        print('{0:>3}.{1:　>5}: {2:>4}'.format(number_of_combos, '左の数字', left_number))
        print('{0:　>7}: {1:>4}'.format('右の数字', right_number))
    
if __name__ == "__main__":
    combos = get_3333()
    format_output(combos)