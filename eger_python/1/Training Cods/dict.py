def main():
    d = {'one': 1, 'two': 2, 'three': 3}
    print(d)
    for k in sorted(d.keys()):
        print(k,d[k])

    m=dict(one=1 ,two=2, three=3 ,four='string')
    for k in sorted(m.keys()):
        print(k,m[k])

    m['seven']=7
    print(m)
if __name__ == '__main__':main()