"""Independent exact arithmetic and completeness checks for Lecture 3."""
from fractions import Fraction as F
from pathlib import Path
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
checks=0

def check(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

def matrix(a):return [[F(x) for x in row] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def mv(a,x):return [sum(F(v)*F(w) for v,w in zip(row,x)) for row in a]
def mm(a,b):return [[sum(F(v)*F(w) for v,w in zip(row,col)) for col in zip(*b)] for row in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,i,j,c):
    b=matrix(a);b[i]=[v+c*w for v,w in zip(b[i],b[j])];return b

def rref(a):
    a=matrix(a);row=0;pivots=[]
    for col in range(len(a[0])):
        pivot=next((i for i in range(row,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        scale=a[row][col];a[row]=[x/scale for x in a[row]]
        for i in range(len(a)):
            if i!=row:a=add(a,i,row,-a[i][col])
        pivots.append(col);row+=1
        if row==len(a):break
    return a,pivots

def rank(a):return len(rref(a)[1])
def augmented(a,b):return [row+[v] for row,v in zip(a,b)]
def solves(a,x,b):check(mv(a,x),list(map(F,b)))
def family(a,b,base,directions):
    solves(a,base,b)
    for v in directions:solves(a,v,[0]*len(a))
    check(rank(directions) if directions else 0,len(directions))
    check(len(directions),len(a[0])-rank(a))
    check(rank(augmented(a,b)),rank(a))

def four_bases(a,col,rows,null,left):
    m,n=len(a),len(a[0]);r=rank(a)
    check(rank(transpose(col)) if col else 0,r)
    for v in col:check(rank(augmented(a,v)),r)
    check(rank(rows),r);check(rank(a+rows),r)
    family(a,[0]*m,[0]*n,null)
    family(transpose(a),[0]*n,[0]*m,left)

# Original source matrices and all displayed reduction stages.
P=[[1,0],[4,3],[2,3]]
solves(P,[F(2,5),F(3,10)],[F(2,5),F(5,2),F(17,10)])
check(rank(P),2)
A=[[1,1,2],[2,1,3],[3,1,4]]
a=add(add(A,1,0,-2),2,0,-3)
check(a,matrix([[1,1,2],[0,-1,-1],[0,-2,-2]]))
a[1]=[-x for x in a[1]];a=add(add(a,2,1,2),0,1,-1)
check(a,matrix([[1,0,1],[0,1,1],[0,0,0]]))
check(rref(A)[0],a)
four_bases(A,[[1,2,3],[1,1,1]],[[1,0,1],[0,1,1]],[[-1,-1,1]],[[1,-2,1]])
for b1,b2 in [(F(1,3),F(5,7)),(2,4),(-3,1)]:
    solves(A,[b2-b1,2*b1-b2,0],[b1,b2,2*b2-b1])
Q1=[[1,1,3],[1,2,4],[2,2,6]];b1=[15,21,30]
check(rref(augmented(Q1,b1))[0],matrix([[1,0,2,9],[0,1,1,6],[0,0,0,0]]))
family(Q1,b1,[9,6,0],[[-2,-1,1]])
Q2=[[1,2,3,5],[2,4,8,12],[3,6,7,13]];b2=[0,6,-6]
a=add(add(augmented(Q2,b2),1,0,-2),2,0,-3)
check(a,matrix([[1,2,3,5,0],[0,0,2,2,6],[0,0,-2,-2,-6]]))
a=add(a,2,1,1);a[1]=[x/2 for x in a[1]];a=add(a,0,1,-3)
check(a,matrix([[1,2,0,2,-9],[0,0,1,1,3],[0,0,0,0,0]]))
family(Q2,b2,[-9,0,3,0],[[-2,1,0,0],[-2,0,-1,1]])
check(mv(Q2,[-3,0,3,0])==b2,False) # Detect the handwritten source error.
Q3=[[1,1,2],[3,-1,14],[1,2,0]];b3=[-2,6,0]
a=add(add(augmented(Q3,b3),1,0,-3),2,0,-1)
check(a,matrix([[1,1,2,-2],[0,-4,8,12],[0,1,-2,2]]))
a[1]=[-x/4 for x in a[1]];a=add(a,2,1,-1)
check(a[2],list(map(F,[0,0,0,5])))
check((rank(Q3),rank(augmented(Q3,b3))),(2,3))
M=[[1,1,0,1],[2,1,0,5]]
check(rref(M)[0],matrix([[1,0,0,4],[0,1,0,-3]]))
check(rank(M),2)
check([4*x-3*y for x,y in zip([1,2],[1,1])],[1,5])
T=[[1,2,1],[-2,-3,1],[3,5,0]]
a=add(add(T,1,0,2),2,0,-3)
check(a,matrix([[1,2,1],[0,1,3],[0,-1,-3]]))
check(rref(T)[0],matrix([[1,0,-5],[0,1,3],[0,0,0]]))
family(T,[0,0,0],[0,0,0],[[5,-3,1]])
solves([[1,1],[1,7],[0,0]],[F(5,6),F(1,6)],[1,2,0])
B=[[3,1],[1,1]];Bi=[[F(1,2),F(-1,2)],[F(-1,2),F(3,2)]]
check(mm(B,Bi),eye(2));check(mm(Bi,B),eye(2))
solves(B,[F(3,2),F(1,2)],[5,2]);solves(Bi,[5,2],[F(3,2),F(1,2)])
# Four canonical shadow spaces, including ambient-dimensional left null vectors.
H=[[1,0,0],[0,1,0],[0,1,0],[0,0,1]];O=[[1,0,0],[0,1,0]]
family(H,[0]*4,[0]*3,[])
family(O,[0,0],[0,0,0],[[0,0,1]])
family(transpose(H),[0]*3,[0]*4,[[0,1,-1,0]])
family(transpose(O),[0]*3,[0]*2,[])
# Fresh practice and supplied supporting problems.
solves([[1,-2,1]],[2,1,0],[0]);solves([[1,-2,1]],[-1,0,1],[0])
P4=[[1,2],[0,1],[1,3]]
solves(P4,[2,1],[4,1,5]);check(rank(augmented(P4,[4,1,6])),3)
family([[1,2,-1],[0,1,3]],[0,0],[0,0,0],[[7,-3,1]])
check(rank([[1,1,1],[2,2,2]]),1);check(rank([[1,1,1],[0,1,-1]]),2)
Rec=[[1,3,1,2],[2,6,4,8],[0,0,2,4]]
check(rref(Rec)[0],matrix([[1,3,0,0],[0,0,1,2],[0,0,0,0]]))
four_bases(Rec,[[1,2,0],[1,4,2]],[[1,3,0,0],[0,0,1,2]],[[-3,1,0,0],[0,0,-2,1]],[[-2,1,-1]])
A9=[[1,1,2],[2,2,4],[0,1,-1]]
family(A9,[4,8,1],[3,1,0],[[-3,1,1]])
family([[1,2,0,1],[0,1,1,-1]],[3,2],[-1,2,0,0],[[2,-1,1,0],[-3,1,0,1]])
check(rank(augmented(A9,[4,9,1])),3)
A13=[[1,2,0],[0,1,1],[1,3,1]]
family(A13,[0]*3,[0]*3,[[2,-1,1]])
for t in [-3,-1,0,F(1,2),1,2,3]:
    check(rank([[1,2,3],[0,t,2*t],[0,0,t-1]]),2 if t in (0,1) else 3)
Recovered=[[1,-1,0],[2,-2,0],[2,-2,0]]
family(Recovered,[2,4,4],[2,0,0],[[1,1,0],[0,0,1]])
check(rank(Recovered),1)
for beta in [-3,-2,-1,0,2]:
    ap=[[1,beta,0],[1,-2,-1],[0,1,1]]
    check(rank(ap),2 if beta==-1 else 3)
    for g in [-1,0,3]:check(rank(augmented(ap,[1,2,g])),2 if beta==-1 and g==-1 else 3)
solves([[1,-1,0],[1,-2,-1],[0,1,1]],[-2,-3,2],[1,2,-1])
family([[1,-1,0],[1,-2,-1],[0,1,1]],[1,2,-1],[0,-1,0],[[-1,-1,1]])
check(rank([[1,3],[2,6]]),1);check(rank([[1,2],[2,1]]),2)
solves([[1,3],[2,6]],[-3,1],[0,0])
solves([[1,0,2],[0,1,-1]],[-2,1,1],[0,0])
P19=[[1,0],[0,2],[1,1]]
solves(P19,[3,2],[3,4,5]);check(rank(augmented(P19,[3,4,6])),3)
V20=[[1,0,1],[1,1,2],[0,1,1]]
solves(V20,[1,1,-1],[0,0,0]);check(rank(V20),2)
B22=[[2,1],[1,-1]];I22=[[F(1,3),F(1,3)],[F(1,3),F(-2,3)]]
check(mm(B22,I22),eye(2));solves(B22,[2,-1],[3,3]);solves(I22,[4,-1],[1,2])
B23=[[1,1],[0,1]];C23=[[1,0],[1,1]];Ci23=[[1,0],[-1,1]]
check(mm(Ci23,B23),matrix([[1,1],[-1,0]]))
solves(B23,[2,-1],[1,-1]);solves(C23,[1,-2],[1,-1])
P24=[[1,0],[0,1],[1,1]]
solves(P24,[2,-1],[2,-1,1]);check(rank(augmented(P24,[2,-1,0])),3)
# Unseen mixed readiness tasks and the compact cheat-sheet example.
solves([[1,-1,0]],[1,1,0],[0]);solves([[1,-1,0]],[0,0,1],[0])
A26=[[1,2,1],[0,1,1],[1,3,2]]
check((rank(A26),rank(augmented(A26,[5,3,9]))),(2,3))
check(add(add(augmented(A26,[5,3,9]),2,0,-1),2,1,-1)[2],[0,0,0,1])
V27=[[1,0,1],[1,1,2],[0,2,2]]
solves(V27,[1,1,-1],[0,0,0]);solves([row[:2] for row in V27],[2,-1],[2,1,-2]);check(rank(V27),2)
B28=[[2,-1],[1,1]];I28=[[F(1,3),F(1,3)],[F(-1,3),F(2,3)]]
check(mm(B28,I28),eye(2));solves(B28,[-1,3],[-5,2]);solves(I28,[-5,2],[-1,3])
Cheat=[[1,2,0],[0,1,1]]
family(Cheat,[4,3],[-2,3,0],[[2,-1,1]])
check(rref(augmented(Cheat,[4,3]))[0],matrix([[1,0,-2,-2],[0,1,1,3]]))
four_bases(Cheat,[[1,0],[2,1]],[[1,0,-2],[0,1,1]],[[2,-1,1]],[])
# Source pairing and assets supplement the mathematical checks.
q=(ROOT/'book/lecture3/practice.md').read_text();s=(ROOT/'book/lecture3/solutions.md').read_text()
check(re.findall(r'\(w3-p(\d+)\)=',q),[f'{n:02}' for n in range(1,29)])
check(re.findall(r'\(w3-s(\d+)\)=',s),[f'{n:02}' for n in range(1,29)])
for name,expected in [('index',5),('solutions-rank',2),('basis',4),('cheatsheet',0)]:
    t=(ROOT/f'book/lecture3/{name}.md').read_text()
    check(t.count('<a href='),4);check(t.count('aria-current="page"'),1)
    check(t.count(':class: checkpoint'),expected)
for name in ['subspace-test','four-spaces','independence','basis-coordinates']:
    check(ET.parse(ROOT/f'book/figures/lecture3/{name}.svg').getroot().tag,'{http://www.w3.org/2000/svg}svg')
print(f'{checks} Lecture 3 exact arithmetic, completeness, source/practice, and asset checks passed.')
