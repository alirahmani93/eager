class point:
    x=0
    y=0
    def distpower2(self , other):
        return (self.x - other.x)**2 + (self.y -other.y)**2

p1 = point()
p1.x=3
p1.y=4
p2 = point()
p2.x=0
p2.y=0

print(p1.distpower2(p2))

# p1.distpower2(5,6)
