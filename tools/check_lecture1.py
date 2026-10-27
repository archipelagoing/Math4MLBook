"""Recompute Lecture 1 numerical examples and audit practice/solution pairing.

Run with Python 3.12+: python tools/check_lecture1.py
This checks stated arithmetic, not every prose claim or student learning.
"""
from fractions import Fraction as F
from math import acos, degrees, isclose, sqrt
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
checks = 0

def equal(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1

def dot(u, v):
    assert len(u) == len(v)
    return sum(a*b for a, b in zip(u, v))

def add(u, v):
    return [a+b for a, b in zip(u, v)]

def scale(c, u):
    return [c*a for a in u]

def transpose(a):
    return list(map(list, zip(*a)))

def product(a, b):
    assert len(a[0]) == len(b)
    return [[dot(row, col) for col in transpose(b)] for row in a]

def trace(a):
    assert len(a) == len(a[0])
    return sum(a[i][i] for i in range(len(a)))

e, a = [1]*4, [1,-1,1,-1]
r, s = [3,1,3,1], [1,3,1,3]
equal(add(scale(2,e),a), r)
equal(add(scale(2,e),scale(-1,a)), s)
equal(add(r,s), [4]*4)
equal(add(r,scale(-1,s)), [2,-2,2,-2])
equal(dot(e,a),0)
equal(dot(r,r),20)
equal(dot(s,s),20)
equal(dot(r,s),12)
equal(dot(add(r,scale(-1,s)),add(r,scale(-1,s))),16)
equal(F(dot(r,s),20),F(3,5))
equal(round(degrees(acos(3/5)),2),53.13)
equal(dot([3,4],[4,3]),24)
equal(round(degrees(acos(24/25)),2),16.26)
equal(dot([3,4],[3,4]),25)
equal(add(scale(2,[2,-1,3]),scale(-1,[-1,4,0])),[5,-6,6])
equal(add(scale(3,e),a),[4,2,4,2])
equal(sum(t*t for t in [F(-3,5),0,F(4,5)]),1)
equal(dot([1,-2,3],add([2,0,-1],[0,4,1])),-6)
equal(dot([1,-2,3],[2,0,-1]),-1)
equal(dot([1,-2,3],[0,4,1]),-5)
equal(dot([2,0,2,0],[0,2,0,2]),0)
equal(dot([2,-1,2],[1,0,-1]),0)
for x,y,z,member in [(1,2,3,False),(1,3,2,True),(2,5,3,True),(2,4,3,False)]:
    equal(y == x+z,member)

A,B=[[1,2],[3,4]],[[2,0],[-1,1]]
equal([add(u,v) for u,v in zip(A,B)],[[3,2],[2,5]])
equal([add(scale(2,u),scale(-1,v)) for u,v in zip(A,B)],[[0,4],[7,7]])
equal(transpose([[1,2,3],[4,5,6]]),[[1,4],[2,5],[3,6]])
equal(trace([[3,2,4],[2,5,6],[4,6,8]]),16)
K=[[0,2,-1],[-2,0,3],[1,-3,0]]
equal(transpose(K),[scale(-1,row) for row in K])
equal(product([[1,0,0],[-1,1,0],[0,-1,1]],[[2],[5],[9]]),[[2],[3],[4]])
equal(product([[1,2,3],[3,2,1]],[[0,2],[1,1],[0,1]]),[[2,7],[2,9]])
# The selected shadow canon: one front view and stacked front/side views.
O=[[1,0,0],[0,1,0]]
H=[[1,0,0],[0,1,0],[0,1,0],[0,0,1]]
equal(product(O,[[2],[3],[4]]),[[2],[3]])
equal(product(O,[[2],[3],[9]]),[[2],[3]])
equal(product(H,[[2],[3],[4]]),[[2],[3],[3],[4]])
equal(product(H,[[12],[4],[2]]),[[12],[4],[4],[2]])
equal(product(O,[[0],[0],[5]]),[[0],[0]])
equal(dot([1,0,0],[2,3,4]),2)
equal((len(O),len(O[0])),(2,3))
equal((len(H),len(H[0])),(4,3))
W=[r,s,r,s]
S=[[1,0],[1,0],[0,1],[0,1]]
equal(transpose(W),W)
equal(trace(W),12)
equal(sum(map(sum,W)),32)
equal(product(W,S),[[4,4]]*4)
M,N=[[2,1,-1],[0,3,2]],[[1,2],[0,-1],[2,1]]
equal(product(M,N),[[0,2],[4,-1]])
equal(product(N,M),[[2,7,3],[0,-3,-2],[4,5,0]])
equal(trace(product(M,N)),trace(product(N,M)))
equal(trace(product(M,N)),-1)
R=[[2,1,2,1],[1,2,1,2],[3,0,3,0]]
equal(product(R,S),[[3,3]]*3)
equal(product(R,[[1]]*4),[[6]]*3)
equal(product(transpose(R),[[1]]*3),[[6],[3],[6],[3]])
equal(sum(map(sum,R)),18)
equal(product([[1]*4],[[t] for t in add(s,scale(-1,r))]),[[0]])
U,D=[[1,1],[0,1]],[[2,0],[0,1]]
equal(product(U,D),[[2,1],[0,1]])
equal(product(D,U),[[2,2],[0,1]])
P=[[0,1],[1,0]]
equal(product(D,P),[[0,2],[1,0]])
equal(product(P,D),[[0,1],[2,0]])
M=[[2,5],[-1,4]]
MT=transpose(M)
symmetric=[[F(u+v,2) for u,v in zip(row,col)] for row,col in zip(M,MT)]
skew=[[F(u-v,2) for u,v in zip(row,col)] for row,col in zip(M,MT)]
equal(symmetric,[[2,2],[2,4]])
equal(skew,[[0,3],[-3,0]])
A=[[1,0,1],[0,1,1]]
for x in [[2,-1,3],[1,-2,4]]:
    equal(product(A,[[t] for t in x]),[[5],[2]])
equal(product(A,[[-1],[-1],[1]]),[[0],[0]])
equal(product(transpose(A),A),[[1,0,1],[0,1,1],[1,1,2]])
equal(product(A,transpose(A)),[[2,1],[1,2]])

# Original slide examples restored to the concise reader edition.
equal(add([0,2],[2,2]),[2,4])
equal(add([0,2],scale(-1,[2,2])),[-2,0])
equal(scale(2,[2,2]),[4,4])
equal(scale(F(1,2),[2,2]),[1,1])
equal(scale(-1,[2,2]),[-2,-2])
equal(transpose([[1,2],[3,4]]),[[1,3],[2,4]])
equal(transpose([[3,2,4],[2,5,6],[4,6,8]]),[[3,2,4],[2,5,6],[4,6,8]])
# A normal to the lecture's u,v plane is (4,4,-3); w lies outside it.
equal(dot([4,4,-3],[1,2,4]),0)
equal(dot([4,4,-3],[2,1,4]),0)
equal(dot([4,4,-3],[9,8,7]),47)

# New section checkpoints use fresh numbers while preserving coordinate roles.
equal(dot([3,-1],[2,6]),0)
equal(dot([0,-5],[0,-5]),25)
equal(dot([0,-1],[0,-1]),1)
equal([scale(-2,row) for row in [[1,-2],[0,3]]],[[-2,4],[0,-6]])
equal(product(O,[[5],[-2],[7]]),[[5],[-2]])
equal(product(O,[[5],[-2],[10]]),[[5],[-2]])

practice=(ROOT/'book/lecture1/practice.md').read_text()
solutions=(ROOT/'book/lecture1/solutions.md').read_text()
equal(sorted(re.findall(r'^\(w1-p(\d+)\)=',practice,re.M)),[f'{n:02}' for n in range(1,25)])
equal(re.findall(r'^\(w1-s(\d+)\)=',solutions,re.M),[f'{n:02}' for n in range(1,25)])
equal(sorted(re.findall(r'<w1-s(\d+)>',practice)),[f'{n:02}' for n in range(1,25)])
# Only active assets are part of this chapter's validation; earlier SVGs are retained.
for name in ['shadow-views','shadow-profiles','shadow-geometry','shadow-map']:
    import xml.etree.ElementTree as ET
    path=ROOT/'book/figures/lecture1'/f'{name}.svg'
    equal(ET.parse(path).getroot().tag,'{http://www.w3.org/2000/svg}svg')
for path in [ROOT/'book/intro.md',*[ROOT/'book/lecture1'/f'{name}.md' for name in ['index','geometry','matrix-guide','cheatsheet','practice','solutions']]]:
    equal(bool(re.search(r'\b(knitting|crochet|stitch|stitches|swatch|sampler|fabric|yarn)\b',path.read_text(),re.I)),False)
print(f'{checks} Lecture 1 arithmetic, pairing, active-asset, and narrative checks passed.')
