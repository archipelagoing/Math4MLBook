"""Recompute Lecture 4 fits, projectors and orthogonalization with exact fractions."""
from fractions import Fraction as F
from pathlib import Path
from math import cos,sin,pi,sqrt,isclose
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
checks=0

def check(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

def dot(a,b):return sum(F(x)*F(y) for x,y in zip(a,b))
def sub(a,b):return [F(x)-F(y) for x,y in zip(a,b)]
def scale(c,a):return [F(c)*F(x) for x in a]
def trans(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(row,col) for col in zip(*b)] for row in a]
def mv(a,x):return [dot(row,x) for row in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse(a):
    n=len(a);b=[[F(x) for x in row]+rowi for row,rowi in zip(a,eye(n))]
    for j in range(n):
        i=next(i for i in range(j,n) if b[i][j]);b[j],b[i]=b[i],b[j]
        b[j]=scale(1/b[j][j],b[j])
        for i in range(n):
            if i!=j:b[i]=sub(b[i],scale(b[i][j],b[j]))
    check([row[:n] for row in b],eye(n));return [row[n:] for row in b]

def projector(a):return mm(mm(a,inverse(mm(trans(a),a))),trans(a))
def projection_checks(p):
    check(trans(p),p);check(mm(p,p),p)
    n=len(p);c=[[F(i==j)-p[i][j] for j in range(n)] for i in range(n)]
    check(trans(c),c);check(mm(c,c),c);check(mm(p,c),[[F(0)]*n for _ in range(n)])

def fit(a,b,x,p,e,sse):
    # Independently solve the full-rank system, then verify the reported quantities.
    gram=mm(trans(a),a);rhs=mv(trans(a),b)
    check(mv(inverse(gram),rhs),list(map(F,x)))
    fitted=mv(a,x);error=sub(b,fitted)
    check(fitted,list(map(F,p)));check(error,list(map(F,e)));check(dot(error,error),F(sse))
    check(mv(trans(a),error),[F(0)]*len(a[0]))
    check(dot(b,b),dot(fitted,fitted)+dot(error,error))
    proj=projector(a);projection_checks(proj);check(mv(proj,b),fitted)
    # Check genuine alternative fits, using each column perturbation and a combined one.
    for delta in eye(len(x))+[[F(2-i) for i in range(len(x))]]:
        alternative=mv(a,[F(v)+d for v,d in zip(x,delta)])
        check(dot(sub(b,alternative),sub(b,alternative))>=dot(error,error),True)
    return proj

def orthogonalize(vectors):
    kept=[]
    for a in vectors:
        u=list(map(F,a))
        for v in kept:u=sub(u,scale(dot(v,a)/dot(v,v),v))
        if dot(u,u):kept.append(u)
    for i,u in enumerate(kept):
        for v in kept[:i]:check(dot(u,v),0)
    return kept

def gs(vectors,expected):
    actual=orthogonalize(vectors);check(actual,[[F(x) for x in v] for v in expected])
    # Verify span preservation by projecting each original input onto the result.
    for a in vectors:
        p=[F(0)]*len(a)
        for u in actual:p=[x+y for x,y in zip(p,scale(dot(u,a)/dot(u,u),u))]
        check(p,list(map(F,a)))
    return actual

# Source vectors, coordinate projections and line example.
check(dot([1,2],[2,-1]),0);check(dot([3,1],[3,1]),10)
Pz=[[0,0,0],[0,0,0],[0,0,1]];Pxy=[[1,0,0],[0,1,0],[0,0,0]]
for p in [Pz,Pxy]:projection_checks(p)
check(mv(Pz,[1,2,3]),[0,0,3]);check(mv(Pxy,[1,2,3]),[1,2,0])
check([[x+y for x,y in zip(r,s)] for r,s in zip(Pz,Pxy)],eye(3))
fit([[1],[2]],[3,1],[1],[1,2],[2,-1],5)
# Canonical H and its noisy records, independent Gram solve and exact projector.
H=[[1,0,0],[0,1,0],[0,1,0],[0,0,1]]
PH=fit(H,[2,2,4,4],[2,3,4],[2,3,3,4],[0,-1,1,0],2)
check(PH,[[1,0,0,0],[0,F(1,2),F(1,2),0],[0,F(1,2),F(1,2),0],[0,0,0,1]])
fit(H,[1,3,7,-2],[1,5,-2],[1,5,5,-2],[0,-2,2,0],8)
check(mm(trans(H),H),[[1,0,0],[0,2,0],[0,0,1]])
check(mv(trans(H),[0,1,-1,0]),[0,0,0])
# Source OLS model, every reported value, and checkpoint's origin-only variant.
fit([[1,1],[1,2],[1,3]],[1,2,2],[F(2,3),F(1,2)],
    [F(7,6),F(5,3),F(13,6)],[F(-1,6),F(1,3),F(-1,6)],F(1,6))
check(mv(inverse([[14]]),[11]),[F(11,14)])
# Original permutation transcribed visually from slide 23 (not text-extraction row order).
Q1=[[0,0,1],[0,1,0],[1,0,0]]
check(mm(trans(Q1),Q1),eye(3));check(mm(Q1,Q1),eye(3));check(mv(Q1,[2,3,4]),[4,3,2])
for theta in (0,pi/6,pi/2,-pi/3):
    q=[[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]
    for i in range(2):
        for j in range(2):check(isclose(sum(q[k][i]*q[k][j] for k in range(2)),float(i==j),abs_tol=1e-12),True)
# Exact Gram–Schmidt stages and normalized inner products of the source basis.
u=gs([[2,-2,0],[4,0,-4],[6,-6,6]],[[2,-2,0],[2,2,-4],[2,2,2]])
check([dot(v,v) for v in u],[8,24,12]);check(dot(u[1],[6,-6,6]),-24)
normalized=[[float(x)/sqrt(float(dot(v,v))) for x in v] for v in u]
for i,a in enumerate(normalized):
    for j,b in enumerate(normalized):check(isclose(sum(x*y for x,y in zip(a,b)),float(i==j),abs_tol=1e-12),True)
# Q coordinate example: q2 has sqrt(2) normalization, coefficient = 3 sqrt(2).
check(6/F(2),3);check(mv(PH,[2,2,4,4]),[2,3,3,4])
# Recitation2 Problem 4, dependent a3 and exact projection from orthogonal directions.
u=gs([[1,1,1,1],[3,1,1,3],[4,2,2,4]],[[1,1,1,1],[1,-1,-1,1]])
fit(trans(u),[1,0,0,0],[F(1,4),F(1,4)],[F(1,2),0,0,F(1,2)],[F(1,2),0,0,F(-1,2)],F(1,2))
# Fresh and supporting practice fits.
check(dot([2,1,-1],[1,0,2]),0);check(dot([3,1,1],[3,1,1]),11)
check(mv([[1,2,0],[0,0,1]],[-2,1,0]),[0,0])
B=[[1,1],[0,0]];check(mm(B,B),B);check(B==trans(B),False)
check(mv(B,[0,1]),[1,0])
fit([[2],[1]],[4,1],[F(9,5)],[F(18,5),F(9,5)],[F(2,5),F(-4,5)],F(4,5))
fit([[1,0],[0,1],[1,0]],[1,2,5],[3,2],[3,2,3],[-2,0,2],8)
fit([[1,1],[1,1],[0,1]],[2,4,6],[-3,6],[3,3,6],[-1,1,0],2)
fit([[1,0],[1,1],[1,2]],[1,2,2],[F(7,6),F(1,2)],
    [F(7,6),F(5,3),F(13,6)],[F(-1,6),F(1,3),F(-1,6)],F(1,6))
fit([[1],[1],[1],[1]],[1,4,7,8],[5],[5,5,5,5],[-4,-1,2,3],30)
fit([[1,0],[1,1],[1,2],[1,3]],[1,8,8,20],[F(7,10),F(57,10)],
    [F(7,10),F(32,5),F(121,10),F(89,5)],[F(3,10),F(8,5),F(-41,10),F(11,5)],F(243,10))
fit([[1,0],[0,1],[1,0]],[4,-1,0],[2,-1],[2,-1,2],[2,0,-2],8)
check(mv([[2,0],[0,3]],[2,2]),[4,6]);check(dot([2,0],[4,6]),8)
gs([[1,0,1],[1,1,1]],[[1,0,1],[0,1,0]])
gs([[1,1,0],[1,0,0],[2,1,0]],[[1,1,0],[F(1,2),F(-1,2),0]])
gs([[1,2,0,1],[1,0,0,1],[0,1,0,1]],[[1,2,0,1],[F(2,3),F(-2,3),0,F(2,3)],[F(-1,2),0,0,F(1,2)]])
# Worksheet 12 coefficients reconstructed in rational scaled directions (radicals cancel).
check([F(-1,2)+F(1,6)+F(4,3),F(1,2)+F(1,6)+F(4,3),F(-1,3)+F(4,3)],[1,2,1])
fit([[1],[-1],[1]],[2,1,0],[F(1,3)],[F(1,3),F(-1,3),F(1,3)],
    [F(5,3),F(4,3),F(-1,3)],F(14,3))
fit([[1,-1],[1,0],[1,1]],[2,0,1],[1,F(-1,2)],[F(3,2),1,F(1,2)],
    [F(1,2),-1,F(1,2)],F(3,2))
gs([[0,1,1],[1,1,1]],[[0,1,1],[1,0,0]])
fit([[0,1],[1,0],[1,0]],[2,3,1],[2,2],[2,2,2],[0,1,-1],2)
fit([[1],[1],[0]],[2,0,1],[1],[1,1,0],[1,-1,1],3)
# Every rank-deficient family and its actual output/residual, at multiple parameters.
for a,b,base,direction,p,e in [
    ([[1,2],[0,0]],[3,4],[3,0],[-2,1],[3,0],[0,4]),
    ([[1,3],[0,0],[1,3]],[2,4,0],[1,0],[-3,1],[1,0,1],[1,4,-1]),
    ([[1,2],[2,4]],[3,1],[1,0],[-2,1],[1,2],[2,-1])]:
    check(mv(a,direction),[0]*len(a));check(mv(trans(a),e),[0]*len(a[0]))
    for t in (F(-7,3),F(0),F(2,5)):
        x=[F(v)+t*d for v,d in zip(base,direction)]
        check(mv(a,x),p);check(sub(b,mv(a,x)),list(map(F,e)))
# Analogy direction after GS: independent at positive angle, zero at repeated view.
for theta in (0,pi/6,pi/2):
    v=[cos(theta),0,sin(theta)];u=[v[0]-cos(theta),0,v[2]]
    check(isclose(u[0],0,abs_tol=1e-12),True)
    check(isclose(sqrt(sum(x*x for x in u)),sin(theta),abs_tol=1e-12),True)
# Fragments and assets: source coverage must resolve to exactly four reader pages.
chapter=ROOT/'book/lecture4'
readers=[chapter/f for f in ['index.md','least-squares.md','orthonormal.md','cheatsheet.md']]
practice=(chapter/'practice.md').read_text();solutions=(chapter/'solutions.md').read_text()
check(re.findall(r'\(w4-p(\d+)\)=',practice),[f'{n:02}' for n in range(1,29)])
check(re.findall(r'\(w4-s(\d+)\)=',solutions),[f'{n:02}' for n in range(1,29)])
check(sum(p.read_text().count('class: checkpoint') for p in readers),11)
check(sum(len(re.findall(r'^:::::\{admonition\} Worked example 4\.', p.read_text(), re.M)) for p in readers),14)
check(re.findall(r'^## ([A-K]) ·','\n'.join(p.read_text() for p in readers),re.M),list('ABCDEFGHIJK'))
for f in (ROOT/'book/figures/lecture4').glob('*.svg'):
    tree=ET.parse(f);check(tree.getroot().tag,'{http://www.w3.org/2000/svg}svg')
    check(tree.find('{http://www.w3.org/2000/svg}desc') is not None,True)
print(f'Lecture 4: {checks} exact arithmetic, geometry, family and source-structure checks passed.')
