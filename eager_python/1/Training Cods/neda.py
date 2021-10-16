class neda:
    def __init__(self,kind ="girl" ):
        self.kind = kind
    def whatkind(self):
        return self.kind
#------------------------------------
def main():
        girl= neda()
        nicegirl = neda("boos")

        print(girl.whatkind())
        print(nicegirl.whatkind())
if __name__ == '__main__': main()

print(type(neda))
print(vars(neda))
print(dir(neda))
print((neda))

