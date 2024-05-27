import random
from typing import List, Union, Tuple


Num = Union[int, float]
Point = Tuple[Num, Num]

def rect_into_tri(
        top_right: Tuple[Num, Num] = (2, 1), 
        triangles: int             = 5,      
        _rand_tol: Num             = 1e6,    
        ) -> List[Tuple[Point, Point, Point]]:


    width, height = top_right
    assert triangles > 2 and triangles % 2 == 1, "Needs Odd number greater than 2"
    

    _rand_tol = int(_rand_tol)

    
    insert_top = triangles // 2
    p = q = None
    while not p or not different_distances(p, q, height):
        p = [0] + rand_points(insert_top,     width, int(_rand_tol)) + [width]  
        q = [0] + rand_points(insert_top - 1, width, int(_rand_tol)) + [width]  
    
    top_tri = [((t0, height), (t1, height), (b0, 0))


               for t0, t1, b0 in zip(p, p[1:], q)]
    bottom_tri = [((b0, 0), (b1, 0), (t1, height))
                  for b0, b1, t1 in zip(q, q[1:], p[1:])]

    return top_tri + bottom_tri

def rect_into_top_tri(
        top_right: Tuple[Num, Num] = (2, 1),
        triangles: int             = 4,
        _rand_tol: Num             = 1e6,
        ) -> List[Tuple[Point, Point, Point]]:
    

    width, height = top_right
    assert int(triangles)==triangles and triangles > 2, "Needs int > 2"
    

    _rand_tol = int(_rand_tol)

    
    insert_top = triangles - 2
    top = [0] + rand_points(insert_top, width, int(_rand_tol)) + [width]  


    top_tri = [((0, 0), (t0, height), (t1, height))
               for t0, t1 in zip(top, top[1:])]
    bottom_tri = [((0, 0), (width, height), (width, 0))]

    return top_tri + bottom_tri


def rand_points(n: int, width: Num=1, _rand_tol: int=1_000_000) -> List[float]:
    "return n sorted, random points where 0 < point < width"
    return sorted(p * width / _rand_tol
                  for p in random.sample(range(1, _rand_tol), n))

def different_distances(p: List[Num], q: List[Num], height: Num) -> bool:
    "Are all point-to-next-point distances in p and q; and height all different?"
    diffs =  [p1 - p0 for p0, p1 in zip(p, p[1:])]
    diffs += [q1 - q0 for q0, q1 in zip(q, q[1:])]
    diffs += [height]
    return len(diffs) == len(set(diffs))


if __name__ == "__main__":
    from pprint import pprint as pp

    print("\nrect_into_tri #1")
    pp(rect_into_tri((2, 1), 5, 10))
    print("\nrect_into_tri #2")
    pp(rect_into_tri((2, 1), 5, 10))
    print("\nrect_into_top_tri #1")
    pp(rect_into_top_tri((2, 1), 4, 10))
    print("\nrect_into_top_tri #2")
    pp(rect_into_top_tri((2, 1), 4, 10))
