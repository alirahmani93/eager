"""
Riley is a very bad boy, but at the same time, he is a yo-yo master. So, he decided to use his yo-yo skills to annoy his friend Anton.

Anton's room can be represented as a grid with n
rows and m columns. Let (i,j) denote the cell in row i and column j. Anton is currently standing at position (i,j)

in his room. To annoy Anton, Riley decided to throw exactly two yo-yos in cells of the room (they can be in the same cell).

Because Anton doesn't like yo-yos thrown on the floor, he has to pick up both of them and return back to the initial position. The distance travelled by Anton is the shortest path that goes through the positions of both yo-yos and returns back to (i,j)
by travelling only to adjacent by side cells. That is, if he is in cell (x,y) then he can travel to the cells (x+1,y), (x−1,y), (x,y+1) and (x,y−1)

in one step (if a cell with those coordinates exists).

Riley is wondering where he should throw these two yo-yos so that the distance travelled by Anton is maximized. But because he is very busy, he asked you to tell him.

[               
0,0     0,1     0,2

1,0     1,1     1,2

2,0     2,1     2,2
]



"""
import math


class Room:
    def __init__(self,n,m,i,j) -> None:
        self.n=n
        self.m=m
        self.i=i
        self.j=j
    def board(m,n):
        Board = list()   
        

        for col in range (0,m+1):
            Board.append(col)

            for row in range (1,n+1):
                Board.append(row*col)

        return Board

 
class Anton(Room):
    
    def shortest_path(n,m,i,j):
        pass


class Riley(Room):

    pass



if __name__ == "__main__" :
    r=Room(3,2,1,1)
    print(r.board)