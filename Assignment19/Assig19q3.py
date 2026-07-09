#write a program which contains filter(),map(),and reduce() in it .
# python application which contains one list of number.list contains the number which are accepted from user.
# filter should filter out all such numbers which greater than or eual to 70 and less than or eual to 90.map function will increase each number by 10.
# reduce will return product of all that numbers.

from functools import reduce

def FilterData(data):
    return list(filter(lambda x: x >= 70 and x <= 90, data))

def MapData(data):
    return list(map(lambda x: x + 10, data))

def ReduceData(data):
    return reduce(lambda x, y: x * y, data)

def main():
    

    size = int(input("Enter number of elements: "))

    data = []

    print("Enter the elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Input List:", data)

    fdata = FilterData(data)
    print("Filtered List:", fdata)

    mdata = MapData(fdata)
    print("Mapped List:", mdata)

    if len(mdata) > 0:
        ans = ReduceData(mdata)
        print("Product:", ans)
    else:
        print("No elements found.")

if __name__ == "__main__":
    main()
