def get_bongji_num(num):
    count = num // 5
    num = num % 5
    count += num // 3
    
    if num % 3 != 0: 
        return -1
    
    return count

if __name__ == '__main__':
    input = input()
    output = get_bongji_num(int(input))
    print(output)
