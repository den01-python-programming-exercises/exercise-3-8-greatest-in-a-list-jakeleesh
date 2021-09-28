def main():
    #write your code below this line
    nums = []
    while True:
        num = int(input())
        if (num == -1):
            break
        else:
            nums.append(num)
    greatest = nums[0]
    for number in nums:
        if number > greatest:
            greatest = number
    print("The greatest number: " + str(greatest))

if __name__ == '__main__':
    main()
