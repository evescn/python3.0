lucky_num = 19
input_num = input("Input the guese num:")
while int(input_num) != lucky_num:
    # print(lucky_num)
    if int(input_num) > lucky_num:
        print("Input number is bigger.")
    else:
        print("Input number is smaller.")
    input_num = input("Input the guese num:")

print("Bingo!")