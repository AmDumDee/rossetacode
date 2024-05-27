
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import sys

def center_point(p1, p2):
    
    cp = []
    for i in range(3):
        cp.append((p1[i]+p2[i])/2)
        
    return cp
    
def sum_point(p1, p2):
    
    sp = []
    for i in range(3):
        sp.append(p1[i]+p2[i])
        
    return sp

def div_point(p, d):
    
    sp = []
    for i in range(3):
        sp.append(p[i]/d)
        
    return sp
    
def mul_point(p, m):
    
    sp = []
    for i in range(3):
        sp.append(p[i]*m)
        
    return sp

def get_face_points(input_points, input_faces):
    
    
    NUM_DIMENSIONS = 3
    
    
    
    face_points = []
    
    for curr_face in input_faces:
        face_point = [0.0, 0.0, 0.0]
        for curr_point_index in curr_face:
            curr_point = input_points[curr_point_index]
            
            for i in range(NUM_DIMENSIONS):
                face_point[i] += curr_point[i]
        
        num_points = len(curr_face)
        for i in range(NUM_DIMENSIONS):
            face_point[i] /= num_points
        face_points.append(face_point)
        
    return face_points
    
def get_edges_faces(input_points, input_faces):
    
    
    edges = []
    
    
    for facenum in range(len(input_faces)):
        face = input_faces[facenum]
        num_points = len(face)
        
        for pointindex in range(num_points):
            
            if pointindex < num_points - 1:
                pointnum_1 = face[pointindex]
                pointnum_2 = face[pointindex+1]
            else:
                
                pointnum_1 = face[pointindex]
                pointnum_2 = face[0]
            
            if pointnum_1 > pointnum_2:
                temp = pointnum_1
                pointnum_1 = pointnum_2
                pointnum_2 = temp
            edges.append([pointnum_1, pointnum_2, facenum])
            
    
    
    edges = sorted(edges)
    
    
    
    num_edges = len(edges)
    eindex = 0
    merged_edges = []
    
    while eindex < num_edges:
        e1 = edges[eindex]
        
        if eindex < num_edges - 1:
            e2 = edges[eindex+1]
            if e1[0] == e2[0] and e1[1] == e2[1]:
                merged_edges.append([e1[0],e1[1],e1[2],e2[2]])
                eindex += 2
            else:
                merged_edges.append([e1[0],e1[1],e1[2],None])
                eindex += 1
        else:
            merged_edges.append([e1[0],e1[1],e1[2],None])
            eindex += 1
            
    
    
    edges_centers = []
    
    for me in merged_edges:
        p1 = input_points[me[0]]
        p2 = input_points[me[1]]
        cp = center_point(p1, p2)
        edges_centers.append(me+[cp])
            
    return edges_centers
       
def get_edge_points(input_points, edges_faces, face_points):
    
    edge_points = []
    
    for edge in edges_faces:
        
        cp = edge[4]
        
        fp1 = face_points[edge[2]]
        
        if edge[3] == None:
            fp2 = fp1
        else:
            fp2 = face_points[edge[3]]
        cfp = center_point(fp1, fp2)
        
        edge_point = center_point(cp, cfp)
        edge_points.append(edge_point)      
        
    return edge_points
    
def get_avg_face_points(input_points, input_faces, face_points):
    
    
    num_points = len(input_points)
    
    temp_points = []
    
    for pointnum in range(num_points):
        temp_points.append([[0.0, 0.0, 0.0], 0])
        
    
    
    for facenum in range(len(input_faces)):
        fp = face_points[facenum]
        for pointnum in input_faces[facenum]:
            tp = temp_points[pointnum][0]
            temp_points[pointnum][0] = sum_point(tp,fp)
            temp_points[pointnum][1] += 1
            
    
    
    avg_face_points = []
    
    for tp in temp_points:
       afp = div_point(tp[0], tp[1])
       avg_face_points.append(afp)
       
    return avg_face_points
    
def get_avg_mid_edges(input_points, edges_faces):
    
    
    num_points = len(input_points)
    
    temp_points = []
    
    for pointnum in range(num_points):
        temp_points.append([[0.0, 0.0, 0.0], 0])
        
    
    
    for edge in edges_faces:
        cp = edge[4]
        for pointnum in [edge[0], edge[1]]:
            tp = temp_points[pointnum][0]
            temp_points[pointnum][0] = sum_point(tp,cp)
            temp_points[pointnum][1] += 1
    
    
    
    avg_mid_edges = []
        
    for tp in temp_points:
       ame = div_point(tp[0], tp[1])
       avg_mid_edges.append(ame)
       
    return avg_mid_edges

def get_points_faces(input_points, input_faces):
    
    
    num_points = len(input_points)
    
    points_faces = []
    
    for pointnum in range(num_points):
        points_faces.append(0)
        
    
    
    for facenum in range(len(input_faces)):
        for pointnum in input_faces[facenum]:
            points_faces[pointnum] += 1
            
    return points_faces

def get_new_points(input_points, points_faces, avg_face_points, avg_mid_edges):
    """
    
    m1 = (n - 3.0) / n
    m2 = 1.0 / n
    m3 = 2.0 / n
    new_coords = (m1 * old_coords)
               + (m2 * avg_face_points)
               + (m3 * avg_mid_edges)
                        
    """
    
    new_points =[]
    
    for pointnum in range(len(input_points)):
        n = points_faces[pointnum]
        m1 = (n - 3.0) / n
        m2 = 1.0 / n
        m3 = 2.0 / n
        old_coords = input_points[pointnum]
        p1 = mul_point(old_coords, m1)
        afp = avg_face_points[pointnum]
        p2 = mul_point(afp, m2)
        ame = avg_mid_edges[pointnum]
        p3 = mul_point(ame, m3)
        p4 = sum_point(p1, p2)
        new_coords = sum_point(p4, p3)
        
        new_points.append(new_coords)
        
    return new_points
    
def switch_nums(point_nums):
    if point_nums[0] < point_nums[1]:
        return point_nums
    else:
        return (point_nums[1], point_nums[0])    

def cmc_subdiv(input_points, input_faces):
    
    
    face_points = get_face_points(input_points, input_faces)
    
    
    edges_faces = get_edges_faces(input_points, input_faces)
    
    
    
    edge_points = get_edge_points(input_points, edges_faces, face_points)
                    
    
                    
    avg_face_points = get_avg_face_points(input_points, input_faces, face_points)
       
    
       
    avg_mid_edges = get_avg_mid_edges(input_points, edges_faces) 
       
    
    
    points_faces = get_points_faces(input_points, input_faces)
    
        
    new_points = get_new_points(input_points, points_faces, avg_face_points, avg_mid_edges)
        
    
    
    
    
    face_point_nums = []
    
    
    next_pointnum = len(new_points)
    
    for face_point in face_points:
        new_points.append(face_point)
        face_point_nums.append(next_pointnum)
        next_pointnum += 1
        
    
    
    edge_point_nums = dict()
    
    for edgenum in range(len(edges_faces)):
        pointnum_1 = edges_faces[edgenum][0]
        pointnum_2 = edges_faces[edgenum][1]
        edge_point = edge_points[edgenum]
        new_points.append(edge_point)
        edge_point_nums[(pointnum_1, pointnum_2)] = next_pointnum
        next_pointnum += 1
    

    
    new_faces =[]
    
    for oldfacenum in range(len(input_faces)):
        oldface = input_faces[oldfacenum]

        if len(oldface) == 4:
            a = oldface[0]
            b = oldface[1]
            c = oldface[2]
            d = oldface[3]
            face_point_abcd = face_point_nums[oldfacenum]
            edge_point_ab = edge_point_nums[switch_nums((a, b))]
            edge_point_da = edge_point_nums[switch_nums((d, a))]
            edge_point_bc = edge_point_nums[switch_nums((b, c))]
            edge_point_cd = edge_point_nums[switch_nums((c, d))]
            new_faces.append((a, edge_point_ab, face_point_abcd, edge_point_da))
            new_faces.append((b, edge_point_bc, face_point_abcd, edge_point_ab))
            new_faces.append((c, edge_point_cd, face_point_abcd, edge_point_bc))
            new_faces.append((d, edge_point_da, face_point_abcd, edge_point_cd))    
    
    return new_points, new_faces
    

def graph_output(output_points, output_faces):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    """
    
    Plot each face
    
    """
    
    for facenum in range(len(output_faces)):
        curr_face = output_faces[facenum]
        xcurr = []
        ycurr = []
        zcurr = []
        for pointnum in range(len(curr_face)):
            xcurr.append(output_points[curr_face[pointnum]][0])
            ycurr.append(output_points[curr_face[pointnum]][1])
            zcurr.append(output_points[curr_face[pointnum]][2])
        xcurr.append(output_points[curr_face[0]][0])
        ycurr.append(output_points[curr_face[0]][1])
        zcurr.append(output_points[curr_face[0]][2])
        
        ax.plot(xcurr,ycurr,zcurr,color='b')
    
    plt.show()


# cube

input_points = [
  [-1.0,  1.0,  1.0],
  [-1.0, -1.0,  1.0],
  [ 1.0, -1.0,  1.0],
  [ 1.0,  1.0,  1.0],
  [ 1.0, -1.0, -1.0],
  [ 1.0,  1.0, -1.0],
  [-1.0, -1.0, -1.0],
  [-1.0,  1.0, -1.0]
]

input_faces = [
  [0, 1, 2, 3],
  [3, 2, 4, 5],
  [5, 4, 6, 7],
  [7, 0, 3, 5],
  [7, 6, 1, 0],
  [6, 1, 2, 4],
]

if len(sys.argv) != 2:
    print("Should have one argument integer number of iterations")
    sys.exit()
else:
    iterations = int(sys.argv[1])
    
    output_points, output_faces = input_points, input_faces
    
    for i in range(iterations):
        output_points, output_faces = cmc_subdiv(output_points, output_faces)
        
graph_output(output_points, output_faces)
