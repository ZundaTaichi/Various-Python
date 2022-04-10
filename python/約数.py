a = 1
while a == 1 :
    print()
    num = input('数値を入力してください:')

    if num != 'end' :
      num = int (num)
      for i in range(1, num+1):
           if num % i == 0:
                print(i, end=" ")

    else :
      a = 0