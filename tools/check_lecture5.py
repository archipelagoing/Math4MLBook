"""Independent exact eigenpair/rank checks and numerical full-SVD reconstruction."""
from fractions import Fraction as F
from math import sqrt,isclose,cos,sin,pi
from pathlib import Path
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];checks=0

def check(a,b):
 global checks
 assert a==b,(a,b)
 checks+=1

def close(a,b):check(isclose(float(a),float(b),rel_tol=1e-11,abs_tol=1e-11),True)
def dot(a,b):return sum(F(x)*F(y) for x,y in zip(a,b))
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(row,col) for col in zip(*b)] for row in a]
def mv(a,x):return [dot(row,x) for row in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def rank(a):
 a=[[F(v) for v in row] for row in a];row=0
 for col in range(len(a[0])):
  p=next((i for i in range(row,len(a)) if a[i][col]),None)
  if p is None:continue
  a[p],a[row]=a[row],a[p];scale=a[row][col];a[row]=[v/scale for v in a[row]]
  for i in range(len(a)):
   if i!=row:
    c=a[i][col];a[i]=[x-c*y for x,y in zip(a[i],a[row])]
  row+=1
  if row==len(a):break
 return row

def eigenspaces(a,pairs):
 # Exact vector equations, nullity and independence establish full eigenspaces,
 # rather than checking only a convenient representative.
 n=len(a);rootlist=[]
 for lam,vecs,multiplicity in pairs:
  shifted=[[F(x)-(F(lam) if i==j else 0) for j,x in enumerate(row)] for i,row in enumerate(a)]
  for v in vecs:check(mv(a,v),[F(lam)*x for x in v]);check(dot(v,v)>0,True)
  check(rank(tr(vecs)),len(vecs));check(n-rank(shifted),len(vecs));rootlist += [F(lam)]*multiplicity
 if n==2:
  check(sum(rootlist),a[0][0]+a[1][1]);check(rootlist[0]*rootlist[1],F(a[0][0])*a[1][1]-F(a[0][1])*a[1][0])

def normalized(v):
 norm=sqrt(float(dot(v,v)));return [float(x)/norm for x in v]

def svd(a,vdirs,evals,udirs):
 m,n=len(a),len(a[0]);g=mm(tr(a),a);r=rank(a)
 check(len(vdirs),n);check(len(udirs),m)
 check(sum(mu>0 for mu in evals),r);check(evals,sorted(evals,reverse=True))
 for i,v in enumerate(vdirs):
  check(mv(g,v),[F(evals[i])*x for x in v])
  for w in vdirs[:i]:check(dot(v,w),0)
  check(dot(v,v)>0,True)
 Vcols=[normalized(v) for v in vdirs];Ucols=[normalized(u) for u in udirs]
 for i in range(m):
  for j in range(m):close(sum(x*y for x,y in zip(Ucols[i],Ucols[j])),int(i==j))
 for i,mu in enumerate(evals):
  if not mu:continue
  actual=[sum(float(x)*y for x,y in zip(row,Vcols[i]))/sqrt(mu) for row in a]
  for x,y in zip(actual,Ucols[i]):close(x,y)
 for u in udirs[r:]:check(mv(tr(a),u),[0]*n)
 for i in range(m):
  for j in range(n):
   value=sum(sqrt(evals[k])*Ucols[k][i]*Vcols[k][j] for k in range(r))
   close(value,a[i][j])
 # Full and compact shapes: singular triples reconstruct every displayed entry.
 check((m,m,n,n),(len(Ucols),len(Ucols[0]),len(Vcols),len(Vcols[0])))
 return Ucols,Vcols

# Source transformation products and rotation/stretch interpretation.
check(mv([[2,-1],[1,2]],[2,3]),[1,8]);check(mv([[2,1],[2,3]],[1,2]),[4,8])
check(dot([1,8],[1,8]),5*dot([2,3],[2,3]))
eigenspaces([[2,1],[2,3]],[(4,[[1,2]],1),(1,[[1,-1]],1)])
eigenspaces([[1,0],[0,2]],[(1,[[1,0]],1),(2,[[0,1]],1)])
check(mm(mm([[1,1],[2,-1]],[[4,0],[0,1]]),[[F(1,3),F(1,3)],[F(2,3),F(-1,3)]]),[[2,1],[2,3]])
eigenspaces([[2,1],[0,2]],[(2,[[1,0]],2)])
eigenspaces([[2,0],[0,2]],[(2,[[1,0],[0,1]],2)])
# Handwritten positive-definite example and exact spectral reconstruction.
S=[[3,1],[1,3]];Qint=[[1,-1],[1,1]]
eigenspaces(S,[(4,[[1,1]],1),(2,[[-1,1]],1)])
check([[v/F(2) for v in row] for row in mm(mm(Qint,[[4,0],[0,2]]),tr(Qint))],S)
check(dot([1,0],[1,1]),1) # I's eigenvectors need not be perpendicular.
for theta in (pi/4,pi/2):check(-4*sin(theta)**2<0,True)
# Canonical 4x3 H, both null spaces and ordered repeated strengths.
H=[[1,0,0],[0,1,0],[0,1,0],[0,0,1]]
svd(H,[[0,1,0],[1,0,0],[0,0,1]],[2,1,1],[[0,1,1,0],[1,0,0,0],[0,0,0,1],[0,1,-1,0]])
# Worksheet14, and every source final exercise.
A=[[3,0],[4,5]]
check(mm(tr(A),A),[[25,20],[20,25]])
svd(A,[[1,1],[1,-1]],[45,5],[[1,3],[3,-1]])
svd([[1,1],[0,0],[0,0]],[[1,1],[1,-1]],[2,0],[[1,0,0],[0,1,0],[0,0,1]])
eigenspaces([[3,1],[4,6]],[(7,[[1,4]],1),(2,[[1,-1]],1)])
svd([[4,0],[3,-5]],[[1,-1],[1,1]],[40,10],[[1,2],[2,-1]])
check(mm(tr([[4,0],[3,-5]]),[[4,0],[3,-5]]),[[25,-15],[-15,25]])
# Exact low-rank reconstructions, discarded energy and all feature-table cases.
R1=[[F(3,2),F(3,2)],[F(9,2),F(9,2)]];check(rank(R1),1)
error=[[F(x)-y for x,y in zip(row,r)] for row,r in zip(A,R1)]
check(sum(dot(row,row) for row in error),5);check(F(45,50),F(9,10))
H1=[[0,0,0],[0,1,0],[0,1,0],[0,0,0]];check(rank(H1),1)
check(sum((F(x)-F(y))**2 for row,r in zip(H,H1) for x,y in zip(row,r)),2)
users=[list(map(F,row)) for row in [('0.7','0.2','0.1','0'),('0','0.05','0.75','0.2'),('0.4','0.3','0.2','0.1')]]
weights=list(map(F,['0.4','0.3','0.27','0.05']))
movies=[list(map(F,row)) for row in [('1','0','0','0'),('0','0.1','0.7','0.2'),('0.5','0.5','0.1','0'),('0.98','0','0','0.03')]]
def score(u,v):return sum(x*w*y for x,w,y in zip(u,weights,v))
check(score(users[0],movies[1]),F('0.0249'));check(score(users[0],[F(0),F('.1'),F('.7'),F('.9')]),F('.0249'))
check(score(users[0],movies[0]),F('.28'));check(score(users[0],movies[0])==5,False)
check(mm(tr(users),users)==eye(4),False)
# Both source genre tables and earliest rating picture: check literal retained numbers.
text=(ROOT/'book/lecture5/applications.md').read_text()
for literal in ['| John | 5 | 1 | 3 | 5 |','| Tom | ? | ? | ? | 2 |','| Alice | 4 | ? | 3 | ? |',
 '| User 1 | 0.7 | 0.2 | 0.1 | 0 |','| User 2 | 0 | 0.05 | 0.75 | 0.2 |',
 '| User m | 0.4 | 0.3 | 0.2 | 0.1 |','| The Notebook | 1.0 | 0 | 0 | 0 |',
 '| Captain America | 0 | 0.1 | 0.7 | 0.2 |','| Seven | 0.5 | 0.5 | 0.1 | 0 |',
 '| Forrest Gump | 0.98 | 0 | 0 | 0.03 |']:
 check(literal in text,True)
# Practice eigenpairs, full eigenspaces, roots and defective/repeated cases.
for a,pairs in [
 ([[2,1],[0,3]],[(3,[[1,1]],1),(2,[[1,0]],1)]),
 ([[1,2],[0,1]],[(1,[[1,0]],2)]),
 ([[-2,0],[0,0]],[(-2,[[1,0]],1),(0,[[0,1]],1)]),
 ([[1,4],[2,3]],[(5,[[1,1]],1),(-1,[[-2,1]],1)]),
 ([[2,4],[2,4]],[(6,[[1,1]],1),(0,[[-2,1]],1)]),
 ([[4,2],[0,1]],[(4,[[1,0]],1),(1,[[-2,3]],1)]),
 ([[5,2],[0,1]],[(5,[[1,0]],1),(1,[[-1,2]],1)]),
 ([[3,1],[0,3]],[(3,[[1,0]],2)]),
 ([[3,0],[0,3]],[(3,[[1,0],[0,1]],2)]),
 ([[2,-1],[-1,2]],[(3,[[1,-1]],1),(1,[[1,1]],1)]),
 ([[4,2],[1,3]],[(5,[[2,1]],1),(2,[[1,-1]],1)])]:eigenspaces(a,pairs)
check(mm(mm([[1,-1],[0,2]],[[5,0],[0,1]]),[[1,F(1,2)],[0,F(1,2)]]),[[5,2],[0,1]])
# Fresh SVD variants, including rectangular/zero/negative/tied cases.
svd([[0,2],[0,0]],[[0,1],[1,0]],[4,0],[[1,0],[0,1]])
svd([[-3,0],[0,1]],[[1,0],[0,1]],[9,1],[[-1,0],[0,1]])
svd([[2,2],[1,-1]],[[1,1],[1,-1]],[8,2],[[1,0],[0,1]])
svd([[0,0],[0,2],[0,0]],[[0,1],[1,0]],[4,0],[[0,1,0],[1,0,0],[0,0,1]])
svd([[3,0,0],[0,3,0]],[[1,0,0],[0,1,0],[0,0,1]],[9,9,0],[[1,0],[0,1]])
svd([[-3,0,0],[0,3,0]],[[1,0,0],[0,1,0],[0,0,1]],[9,9,0],[[-1,0],[0,1]])
svd([[2,0],[0,1]],[[-1,0],[0,1]],[4,1],[[-1,0],[0,1]])
svd([[0,0,0],[0,0,0]],[[1,0,0],[0,1,0],[0,0,1]],[0,0,0],[[1,0],[0,1]])
svd([[1,1],[1,-1],[0,0]],[[1,0],[0,1]],[2,2],[[1,1,0],[1,-1,0],[0,0,1]])
svd([[3,0],[0,-1]],[[1,0],[0,1]],[9,1],[[1,0],[0,-1]])
svd([[4,0],[0,-2]],[[1,0],[0,1]],[16,4],[[1,0],[0,-1]])
check(F(36+9,36+9+4),F(45,49));check(4*(80+40+1),484)
check(F('.2')*3*F('.5')+F('.8')*F('.25'),F('.5'))
for b in [[[5,1],[5,1]],[[5,5],[1,1]]]:
 check(rank(b),1);check(b[0][0],5);check(b[1][1],1)
# Validate diagram's chosen circle map preserves the declared singular strengths.
for t in [j*pi/8 for j in range(16)]:
 x,y=cos(t),sin(t);a,b=3*x,y;rotated=(cos(pi/6)*a-sin(pi/6)*b,sin(pi/6)*a+cos(pi/6)*b)
 close(sum(v*v for v in rotated),9*x*x+y*y)
# Bank pairing, ordered source parts and reproducible SVG structure.
chapter=ROOT/'book/lecture5';pages=[chapter/f for f in ['index.md','svd.md','applications.md','cheatsheet.md']]
check(re.findall(r'\(w5-p(\d+)\)=',(chapter/'practice.md').read_text()),[f'{n:02}' for n in range(1,29)])
check(re.findall(r'\(w5-s(\d+)\)=',(chapter/'solutions.md').read_text()),[f'{n:02}' for n in range(1,29)])
check(re.findall(r'^## ([A-J]) ·','\n'.join(p.read_text() for p in pages),re.M),list('ABCDEFGHIJ'))
check(sum(p.read_text().count('class: checkpoint') for p in pages),10)
check(sum(len(re.findall(r'^:::::\{admonition\} Worked example 5\.',p.read_text(),re.M)) for p in pages),15)
assets=list((ROOT/'book/figures/lecture5').glob('*.svg'));check(len(assets),6)
for p in assets:
 tree=ET.parse(p);check(tree.getroot().tag,'{http://www.w3.org/2000/svg}svg');check(tree.find('{http://www.w3.org/2000/svg}desc') is not None,True)
print(f'Lecture 5: {checks} eigenpair, eigenspace, SVD, reconstruction, source-data and structure checks passed.')
