'''
    Created by: Sergio Can
    Date: 23-07-2018
    You can found BFS and Construct_Path algorithm  on Wikipedia page.
'''

import sys
def bfs(problem):
    open_set=[]
    closed_set=set()
    meta=dict()

    root=problem.root
    meta[str(root)]=(None,None)
    open_set.append(root)

    while len(open_set)!=0:
        subtree_root = open_set.pop(0)
        if problem.goal==subtree_root:
            return construct_path(subtree_root,meta)
        Newtree=problem.tree(subtree_root)
        for child,action in zip(Newtree[0],Newtree[1]):
            if str(child) in closed_set:
                continue
            if child not in open_set:
                meta[str(child)]=(subtree_root,action)
                open_set.append(child)
            closed_set.add(str(subtree_root))      
    return meta

def construct_path(state,meta):
    action_list=list()
    while meta[str(state)][0] is not None:
        state,action = meta[str(state)]
        action_list.append(action)
    action_list.reverse()
    return action_list

class Problem():
    def __init__(self,board,goal):
        self.root=list(board)
        self.goal=list(goal)
    # Return a copy of the new board
    def swap(self,board,i,j):
        Nboard= list(board).copy()
        Nboard[i], Nboard[j] = board[j], board[i]
        return Nboard
    #Find zero position on board
    def findZero(self,board):
        i=0
        found=False
        while i < len(board) and not found:
            if board[i]=='0':
                found=True
            else:
                i+=1
        return i
    #Return possible movements for actual state
    def tree(self,board):
        listTree=[]
        actions=[]
        zero=self.findZero(board)
        if zero==0:
            listTree.append(self.swap(board,zero,1))
            listTree.append(self.swap(board,zero,3))
            actions.append("L")
            actions.append("U")
        elif zero==1:
            listTree.append(self.swap(board,zero,0))
            listTree.append(self.swap(board,zero,2))
            listTree.append(self.swap(board,zero,4))
            actions.append("R")
            actions.append("L")
            actions.append("U")
        elif zero==2:
            listTree.append(self.swap(board,zero,1))
            listTree.append(self.swap(board,zero,5))
            actions.append("R")
            actions.append("U")
        elif zero==3:
            listTree.append(self.swap(board,zero,0))
            listTree.append(self.swap(board,zero,4))
            listTree.append(self.swap(board,zero,6))
            actions.append("D")
            actions.append("L")
            actions.append("U")
        elif zero==4:
            listTree.append(self.swap(board,zero,1))
            listTree.append(self.swap(board,zero,3))
            listTree.append(self.swap(board,zero,5))
            listTree.append(self.swap(board,zero,7))
            actions.append("D")
            actions.append("R")
            actions.append("L")
            actions.append("U")
        elif zero==5:
            listTree.append(self.swap(board,zero,2))
            listTree.append(self.swap(board,zero,4))
            listTree.append(self.swap(board,zero,8))
            actions.append("D")
            actions.append("R")
            actions.append("U")
        elif zero==6:
            listTree.append(self.swap(board,zero,3))
            listTree.append(self.swap(board,zero,7))
            actions.append("D")
            actions.append("L")
        elif zero==7:
            listTree.append(self.swap(board,zero,6))
            listTree.append(self.swap(board,zero,4))
            listTree.append(self.swap(board,zero,8))
            actions.append("R")
            actions.append("D")
            actions.append("L")
        elif zero==8:
            listTree.append(self.swap(board,zero,7))
            listTree.append(self.swap(board,zero,5))
            actions.append("R")
            actions.append("D")
        return listTree, actions

if __name__=='__main__':  
    board=str(sys.argv[1])
    goal ="123456780"
    game=Problem(board,goal)
    meta=bfs(game)
    print(meta)

