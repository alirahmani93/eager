# class a:

#     ab = []
#     def rec(self , x :int):
        
#         y = x // 2
#         # self.ab.append(y)

#         if y == 0 :
#             pass
#             # print("if")
#             # return print("ab:",self.ab)
#         else:
#             self.ab.append(y)
#             # print("else")
#             return self.rec(y)
#         return self.ab



# l = a()
# print(l.rec(100))

def find_path(self, node_a, node_b, path=list()):
    path = path + [node_a]
    if node_a == node_b:
        return path
    if node_a not in self.adj_matrix[node_a]:
        return print("There is no cycle")
    for node in self.adj_matrix[node_a]:
        if node not in path:
            new_path = find_path(self, node, node_b, path)
            if new_path: return new_path
    return f"path {path}"

print(find_path())