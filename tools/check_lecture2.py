"""Exact, independent arithmetic and reader-structure checks for Lecture 2."""
from fractions import Fraction as F
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
checks=0

def check(actual,expected):
    global checks
    assert actual==expected,(actual,expected)
    checks+=1

def mat(rows):return [[F(x) for x in row] for row in rows]
def add(m,i,j,c):
    n=[r[:] for r in m];n[i]=[a+c*b for a,b in zip(m[i],m[j])];return n

def rref(rows):
    a=mat(rows);i=0;pivots=[]
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        divisor=a[i][j];a[i]=[v/divisor for v in a[i]]
        for k in range(len(a)):
            if k!=i:a=add(a,k,i,-a[k][j])
        pivots.append(j);i+=1
        if i==len(a):break
    return a,pivots

def product(a,x):return [sum(F(v)*F(w) for v,w in zip(row,x)) for row in a]
def solvecheck(a,x,b):check(product(a,x),list(map(F,b)))

def classify(rows):
    r,p=rref(rows);n=len(r[0])-1
    return 'none' if n in p else 'unique' if len(p)==n else 'infinite'

main=mat([[1,1,3,15],[1,2,4,21],[1,1,2,13]])
m1=add(add(main,1,0,-1),2,0,-1)
check(m1,mat([[1,1,3,15],[0,1,1,6],[0,0,-1,-2]]))
m2=[r[:] for r in m1];m2[2]=[-v for v in m2[2]]
check(m2,mat([[1,1,3,15],[0,1,1,6],[0,0,1,2]]))
m3=add(add(m2,0,2,-3),1,2,-1)
check(m3,mat([[1,1,0,9],[0,1,0,4],[0,0,1,2]]))
m4=add(m3,0,1,-1)
check(m4,mat([[1,0,0,5],[0,1,0,4],[0,0,1,2]]))
check(rref(main)[0],m4)
solvecheck([r[:3] for r in main],[5,4,2],[15,21,13])
L=[[1,0,0],[-1,1,0],[0,-1,1]]
solvecheck(L,[2,5,9],[2,3,4]);solvecheck(L,[3,7,8],[3,4,1])
A=[[1,2,3],[2,5,2],[6,-3,1]]
a=mat([r+[b] for r,b in zip(A,[6,4,2])])
a=add(add(a,1,0,-2),2,0,-6)
check(a,mat([[1,2,3,6],[0,1,-4,-8],[0,-15,-17,-34]]))
a=add(a,2,1,15)
check(a[2],list(map(F,[0,0,-77,-154])))
check(rref(a)[0],mat([[1,0,0,0],[0,1,0,0],[0,0,1,2]]))
solvecheck(A,[0,0,2],[6,4,2])
solvecheck([[1,-2],[3,2]],[3,1],[1,11])
solvecheck([[2,-1],[1,3]],[3,1],[5,6])
solvecheck([[-1,0,2],[3,1,0],[0,0,1]],[-2,8,1],[4,2,1])
solvecheck([[0,2],[1,1]],[1,2],[4,3])
solvecheck([[2,1],[6,4]],[2,1],[5,16])
check(rref([[2,1,5],[6,4,16]])[0],mat([[1,0,2],[0,1,1]]))
check(rref([[0,2,4],[1,1,3]])[0],mat([[1,0,1],[0,1,2]]))
B=[[1,3,0,0,3],[0,0,1,0,9],[0,0,0,1,4],[0,0,0,0,0]]
check(rref(B),(mat(B),[0,2,3]))
H=[[1,0,0],[0,1,0],[0,1,0],[0,0,1]]
for z in [4,9]:solvecheck(H,[2,3,z],[2,3,3,z])
for b,expected in [([2,3,3,4],'unique'),([2,2,4,4],'none')]:
    check(classify([row+[v] for row,v in zip(H,b)]),expected)
check(classify([[1,0,0,2],[0,1,0,3]]),'infinite')
check(classify([[1,1,2],[2,2,4]]),'infinite')
check(classify([[1,1,2],[2,2,5]]),'none')
# Prove the displayed families symbolically by checking affine base and directions.
# A(base + s*u + t*v)=b for every real parameter follows from A base=b and A directions=0.
for a,base,dirs,b in [
    ([[1,2,0],[0,0,1]],[3,0,4],[[-2,1,0]],[3,4]),
    ([[1,2,0,-1],[0,0,1,4]],[3,0,5,0],[[-2,1,0,0],[1,0,-4,1]],[3,5]),
    ([r[:-1] for r in B],[3,0,9,4],[[-3,1,0,0]],[3,9,4,0]),
    ([[1,1],[2,2]],[2,0],[[-1,1]],[2,4]),
    ([[1,0,0],[0,1,0]],[2,3,0],[[0,0,1]],[2,3]),
]:
    solvecheck(a,base,b)
    for direction in dirs:solvecheck(a,direction,[0]*len(a))
# Symbolic stacked-view consistency: the row difference always gives c-b.
for b,c in [(F(3),F(3)),(F(-2),F(7)),(F(1,3),F(2,3))]:
    aug=mat([r+[v] for r,v in zip(H,[2,b,c,4])])
    check(add(aug,2,1,-1)[2],[0,0,0,c-b])
    check(classify(aug),'unique' if b==c else 'none')
for file in ['index','elimination','practice','solutions']:
    s=(ROOT/f'book/lecture2/{file}.md').read_text()
    check(s.count('<a href='),4);check(s.count('aria-current="page"'),1)
    check(bool(re.search(r'\b(knitting|crochet|yarn|stitch)\b',s,re.I)),False)
    if file in ['index','elimination']:
        check(s.count('{div} section-intro'),4)
        check(s.count('{div} section-recap'),4)
        check(s.count(':class: checkpoint'),4)
p=(ROOT/'book/lecture2/practice.md').read_text();s=(ROOT/'book/lecture2/solutions.md').read_text()
check(re.findall(r'\(w2-p(\d+)\)=',p),[f'{n:02}' for n in range(1,19)])
check(re.findall(r'\(w2-s(\d+)\)=',s),[f'{n:02}' for n in range(1,19)])
print(f'{checks} Lecture 2 arithmetic, family, classification, and structure checks passed.')
