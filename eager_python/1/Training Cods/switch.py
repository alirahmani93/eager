def main():
    choices = dict(one ="first", two='secend', three = 'third', four='fourth',five='fifth')

    v=input("your code: ")
    print(choices.get(v,'others'))

if __name__ == '__main__':main()
