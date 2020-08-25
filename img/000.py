import os

def main():
    print()
    f = os.listdir()
    print(__file__)
    for i in range(len(f)):
        if f[i] == __file__.split("\\")[-1]:continue
        #if n in f:
        a = os.path.splitext(f[i])[0]
        if a.isnumeric():
            print(a)
            continue
        else:
            j = 0
            while 1:
                j+=1
                n = str(j)+'.jpg'
                if os.path.isfile(n):
                    print(n)
                    continue
                else:
                    os.rename(f[i],n)
                    break
            
            
if __name__ == '__main__':
    main()
