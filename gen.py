with open('AVeryLongPieceOfCode.py', 'w', encoding='utf8') as f:
    f.write('x = input("请给出一个不多于5位的正整数:")\n'
            'x = int(x)\n'
            'if x==1:\n'
            '    print("是1位数")\n'
            '    print("个位数是1")\n'
            '    print("倒过来是1")\n'
            )

    for num in range(2, 100000):
        f.write(f'elif x=={num}:\n'
                f'    print("是{len(str(num))}位数")\n'
                f'    print("个位数是{str(num)[-1]}")\n'
                f'    print("倒过来是{str(num)[::-1]}")\n')
