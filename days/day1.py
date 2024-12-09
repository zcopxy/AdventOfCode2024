def read_input(file_path):
    
    list1 = []
    list2 = []
    
    with open(file_path, 'r') as file:
        
        for line in file:
            num1, num2 = map(int, line.strip().split())
            list1.append(num1)
            list2.append(num2)
        
        return list1, list2
    
def day1_1(list1, list2):
    list1, list2 = sorted(list1), sorted(list2)

    return sum(abs(x-y) for x,y in zip(list1, list2))

def main():
    
    file_path = 'inputs/input_day1.txt'
    list1, list2 = read_input(file_path)

    result = day1_1(list1, list2)

    print(f'Total distance: {result}')

if __name__ == '__main__':
    main()

