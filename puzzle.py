#Imports
import numpy as np
import queue
import argparse


# Class and Function Definitions
# Node
class Node:
    """Class definition of a Node in graph"""
    
    def __init__(self,state,index,parent_index):
        """Initialization with state,parent index and index of node"""
        self.state=state
        self.parent_index=parent_index
        self.index=index
        
    def __equal__(self,other):
        """Equating the state of two different node objaects"""
        return np.array_equal(self.state, other.state)
    
    def __str__(self):
        """Converting the state to a string"""
        string = ' '.join(map(str, self.state.T.flatten()))+'\n'
        return string
    
def swap(matrix, i1, j1, i2, j2):
    """Move the blank tile"""
    temp = matrix[i1, j1]
    matrix[i1, j1] = matrix[i2, j2]
    matrix[i2, j2] = temp
    return matrix

def generate_path(explored,current):
    """Generate path using backtracking"""
    ex=np.array(explored)
    track=[]
    path_str=[]
    node_info=[]
    node=current
    track.append(node)
    path_str.append(node.__str__())
    p_index=node.parent_index
    indices = np.where([node.index == p_index for node in ex])[0]

    while not node.index==0:
        indices = np.where([node.index == p_index for node in ex])[0]
        node=ex[indices[0]]
        p_index=node.parent_index
        track.append(node)
        path_str.append(node.__str__())
        node_info_str = "{:5d} | {:12d} | {:5s}".format(node.index, node.parent_index,node.__str__())
#         node_info_str=str(node.index)+" "+str(node.parent_index)+" "+node.__str__()
        node_info.append(node_info_str)
#     Write to nodePath genreated from backtracking
    with open("nodePath.txt", "w") as f:
        path_str.reverse()
        f.writelines(path_str)
        print("Created file nodePath.txt")
    #     Write nodes info to NodesInfo.txt
    node_info_str = "{:5s} | {:5s} | {:5s}\n".format("Index", "Parent Index","State")
    node_info.append(node_info_str)
    with open("NodesInfo.txt", "w") as f:
        node_info.reverse()
        f.writelines(node_info)
        print("Created file NodesInfo.txt")
    return track
def ActionMoveLeft(current,idx):
    i,j=np.where(current.state==0)
    i=i[0]
    j=j[0]
    node=Node(swap(current.state.copy(),i,j,i,j-1),idx,current.index)
    status=False
    if tuple(map(tuple, node.state)) not in visited:
        status=True
    return status,node

def ActionMoveRight(current,idx):
    i,j=np.where(current.state==0)
    i=i[0]
    j=j[0]
    node=Node(swap(current.state.copy(),i,j,i,j+1),idx,current.index)
    status=False
    if tuple(map(tuple, node.state)) not in visited:
        status=True
    return status,node

def ActionMoveUp(current,idx):
    i,j=np.where(current.state==0)
    i=i[0]
    j=j[0]
    node=Node(swap(current.state.copy(),i,j,i-1,j),idx,current.index)
    status=False
    if tuple(map(tuple, node.state)) not in visited:
        status=True
    return status,node

def ActionMoveDown(current,idx):
    i,j=np.where(current.state==0)
    i=i[0]
    j=j[0]
    node=Node(swap(current.state.copy(),i,j,i+1,j),idx,current.index)
    status=False
    if tuple(map(tuple, node.state)) not in visited:
        status=True
    return status,node
    
def Puzzle(start,goal,grid):
    """Solve the puzzle given a start and goal state"""
    import queue
    queue=queue.Queue()
    global visited
    visited=set()
    current=Node(start,0,0)
    goal=Node(goal,None,None)
    n=grid
    idx=0
    explored=[]
    explored_str=[]
    if  current.__equal__(goal):
        pass
    else:
        queue.put(current)
        while not current.__equal__(goal):
            if not queue.empty():
                current=queue.get()
                explored.append(current)
                explored_str.append(current.__str__())
                
                i,j=np.where(current.state==0)
                i=i[0]
                j=j[0]
            if i+1<n:
                idx+=1
#                 Move Down
                status,node=ActionMoveDown(current,idx)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
            if j+1<n:
                idx+=1
#                 Move Right
                status,node=ActionMoveRight(current,idx)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
            if i-1>=0:
                idx+=1
#                 Move Up
                status,node=ActionMoveUp(current,idx)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
            if j-1>=0:
                idx+=1
#                 Move Left
                status,node=ActionMoveLeft(current,idx)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
#     Write explored nodes to nodes.txt
    with open("Nodes.txt", "w") as f:
        f.writelines(explored_str)
        print("Created file Nodes.txt")

    return generate_path(explored,current)

    

    


#Implementation

def main():
    parser = argparse.ArgumentParser(description='This program  is used to solve a 8 puzzle game using BFS')
    parser.add_argument('-ss', '--start_state', type=str, help='Start State column wise', required=False)
    args = parser.parse_args()
    if not args.start_state:
        # Define a random start state
        values = np.arange(9)
        np.random.shuffle(values)
        start = np.reshape(values, (3, 3))
        start=start
        print("We have generated start state\n",start)


    else:
        state_list = args.start_state.split()
        state_list = [int(i) for i in state_list]
        start = np.array(state_list).reshape((3, 3)).T
        print("You have selected the following start state\n",start)


    # Define a goal state
    goal= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    print("Goal:\n",goal)
    print("Puzzle is being solved")
    Puzzle(start,goal,3)

if __name__ == '__main__':
    main()




