"""Independent exact sample-statistics, covariance PCA and reconstruction checks."""
from fractions import Fraction as F
from pathlib import Path
from math import sqrt,isclose
import hashlib,re,struct,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];checks=0

def check(a,b):
 global checks
 assert a==b,(a,b)
 checks+=1

def close(a,b):check(isclose(float(a),float(b),abs_tol=1e-11,rel_tol=1e-11),True)
def mat(a):return [[F(x) for x in row] for row in a]
def dot(a,b):return sum(F(x)*F(y) for x,y in zip(a,b))
def tr(a):return list(map(list,zip(*a)))
def mv(a,v):return [dot(row,v) for row in a]
def mm(a,b):return [[dot(row,col) for col in zip(*b)] for row in a]
def stats(a):
 a=mat(a);m,n=len(a),len(a[0]);mu=[sum(col)/m for col in zip(*a)]
 x=[[v-u for v,u in zip(row,mu)] for row in a]
 for col in zip(*x):check(sum(col),0)
 gram=mm(tr(x),x);cov=[[v/(m-1) for v in row] for row in gram]
 check(cov,tr(cov));return mu,x,cov

def pca(a,mu,c,lams,dirs,k=1):
 m,n=len(a),len(a[0]);mean,x,cov=stats(a)
 check(mean,list(map(F,mu)));check(cov,mat(c));check(list(lams),sorted(lams,reverse=True))
 check(len(dirs),n)
 for i,(lam,q) in enumerate(zip(lams,dirs)):
  check(lam>=0,True);check(dot(q,q)>0,True)
  check(mv(cov,q),[F(lam)*v for v in q])
  for r in dirs[:i]:check(dot(q,r),0)
 # Exact outer products divided by squared norms avoid normalizing radicals.
 projs=[[[F(a)*b/dot(q,q) for b in q] for a in q] for q in dirs]
 identity=[[sum(p[i][j] for p in projs) for j in range(n)] for i in range(n)]
 check(identity,[[F(i==j) for j in range(n)] for i in range(n)])
 reconstructed_cov=[[sum(F(lam)*p[i][j] for lam,p in zip(lams,projs)) for j in range(n)] for i in range(n)]
 check(reconstructed_cov,cov)
 P=[[sum(p[i][j] for p in projs[:k]) for j in range(n)] for i in range(n)]
 check(P,tr(P));check(mm(P,P),P)
 fitted=[mv(P,row) for row in x];errors=[[u-v for u,v in zip(row,fit)] for row,fit in zip(x,fitted)]
 for error in errors:
  for q in dirs[:k]:check(dot(error,q),0)
 sse=sum(dot(row,row) for row in errors);check(sse,(m-1)*sum(map(F,lams[k:])))
 for row,fit,error in zip(x,fitted,errors):check(dot(row,row),dot(fit,fit)+dot(error,error))
 # Sample score variances equal covariance eigenvalues; all cross terms vanish.
 ts=[[dot(row,q) for row in x] for q in dirs]
 for j,(q,lam) in enumerate(zip(dirs,lams)):
  check(sum(ts[j]),0);check(dot(ts[j],ts[j])/((m-1)*dot(q,q)),F(lam))
  for t in ts[:j]:check(dot(ts[j],t),0)
 dhat=[[v+u for v,u in zip(row,mean)] for row in fitted]
 # Independent closed-form 2x2 eigenvalues cross-check the supplied spectrum.
 if n==2:
  a,b,d=map(float,[cov[0][0],cov[0][1],cov[1][1]])
  disc=sqrt((a-d)**2+4*b*b)
  close(lams[0],(a+d+disc)/2);close(lams[1],(a+d-disc)/2)
 return {'mean':mean,'x':x,'cov':cov,'projector':P,'reconstructed':dhat,'errors':errors,'sse':sse,'score_numerators':ts,
         'evr':sum(map(F,lams[:k]))/sum(map(F,lams)) if sum(lams) else None}

# Source arithmetic and declared sample-versus-population convention.
check(300*300*3,270000)
mu,x,c=stats([[3],[7],[5]]);check(mu,[5]);check(x,[[-2],[2],[0]]);check(c,[[4]]);close(sqrt(float(c[0][0])),2)
check(sum(v[0]**2 for v in x)/3,F(8,3))
pca([[3,2],[7,6],[5,4]],[5,4],[[4,4],[4,4]],[8,0],[[1,1],[1,-1]])
pizza=pca([[1,5],[2,4],[3,3],[4,2],[5,1]],[3,3],[[F(5,2),F(-5,2)],[F(-5,2),F(5,2)]],[5,0],[[1,-1],[1,1]])
check(pizza['sse'],0);check(pizza['score_numerators'][0],[-4,-2,0,2,4])
# Triangle, fixed-total objective and canonical four-record cloud.
check(dot([2,1],[2,1]),dot([2,0],[2,0])+dot([0,1],[0,1]))
cloud=pca([[3,2],[2,3],[1,0],[0,1]],[F(3,2),F(3,2)],[[F(5,3),1],[1,F(5,3)]],[F(8,3),F(2,3)],[[1,1],[1,-1]])
check(cloud['score_numerators'][0],[2,2,-2,-2]);check(cloud['evr'],F(4,5));check(cloud['sse'],2)
# Every stage of the source's student calculation, including exact reconstruction.
students=pca([[10,90],[6,80],[20,100]],[12,90],[[52,70],[70,100]],[150,2],[[5,7],[-7,5]])
check(students['x'],[[-2,0],[-6,-10],[8,10]])
check(mm(tr(students['x']),students['x']),[[104,140],[140,200]])
check(students['score_numerators'][0],[-10,-100,110]);check(students['score_numerators'][1],[14,-8,-6])
for t,expected in zip(students['score_numerators'][0],[-1.1624763874381928,-11.624763874381928,12.78724026182012]):close(float(t)/sqrt(74),expected)
check(students['reconstructed'],[[F(419,37),F(3295,37)],[F(194,37),F(2980,37)],[F(719,37),F(3715,37)]])
check(students['errors'],[[F(-49,37),F(35,37)],[F(28,37),F(-20,37)],[F(21,37),F(-15,37)]])
check(students['sse'],4);check(students['sse']/3,F(4,3));check(students['evr'],F(75,76))
# Preprocessing and exact inverse in raw and standardized feature metrics.
raw=pca([[1,10],[2,20],[3,30]],[2,20],[[1,10],[10,100]],[101,0],[[1,10],[-10,1]])
standard=pca([[-1,-1],[0,0],[1,1]],[0,0],[[1,1],[1,1]],[2,0],[[1,1],[1,-1]])
check([[2+r[0],20+10*r[1]] for r in standard['reconstructed']],mat([[1,10],[2,20],[3,30]]))
check(raw['sse'],0)
# Four-pixel decoder's unit direction and exact coefficient/reconstruction.
q=[F(1,2),F(-1,2),F(-1,2),F(1,2)];check(dot(q,q),1);check(dot(q,[1,-1,-1,1]),2)
check([2+2*v for v in q],[3,1,1,3])
# All three source failure mechanisms, using the declared numerical illustrations.
pca([[-2,0],[0,0],[2,0]],[0,0],[[4,0],[0,0]],[4,0],[[1,0],[0,1]])
after=pca([[-2,0],[0,0],[2,0],[0,10]],[0,F(5,2)],[[F(8,3),0],[0,25]],[25,F(8,3)],[[0,1],[1,0]])
classes=pca([[x,y] for y in [F(-1,10),F(1,10)] for x in [-3,-1,1,3]],[0,0],[[F(40,7),0],[0,F(2,175)]],[F(40,7),F(2,175)],[[1,0],[0,1]])
check(classes['evr'],F(500,501))
check(classes['reconstructed'][:4],classes['reconstructed'][4:])
curve=pca([[-2,0],[-1,F(3,2)],[0,2],[1,F(3,2)],[2,0]],[0,1],[[F(5,2),0],[0,F(7,8)]],[F(5,2),F(7,8)],[[1,0],[0,1]])
check(curve['sse']>0,True)
# Fresh cheat sheet example.
cheat=pca([[0,0],[4,0],[0,2],[4,2]],[2,1],[[F(16,3),0],[0,F(4,3)]],[F(16,3),F(4,3)],[[1,0],[0,1]])
check(cheat['evr'],F(4,5));check(cheat['sse'],4);check(cheat['reconstructed'],[[0,1],[4,1],[0,1],[4,1]])
# Practice arithmetic: numerical means/covariances, unit projections, fitted models.
check(20*30*3,1800);check(min(50-1,1800),49)
mu,x,c=stats([[2],[4],[9]]);check(mu,[5]);check(x,[[-3],[-1],[4]])
check(stats([[12],[14],[19]])[1],x)
check(stats([[1,10],[3,14],[5,12]])[:2],([3,12],[[-2,-2],[0,2],[2,0]]))
check(stats([[1],[2],[6]])[2],[[7]]);check(4*9,36)
check(stats([[1,6],[3,2],[5,4]])[2],[[4,-2],[-2,4]])
mu,x,c=stats([[-1,1],[0,0],[1,1]]);check(c,[[1,0],[0,F(1,3)]])
check(dot([3,-3],[1,-1]),6);check(dot([3,-3],[1,1]),0)
check(dot([1,3],[1,1]),4);check(dot([-1,1],[1,1]),0);check(dot([-1,1],[-1,1]),2)
for v1 in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:check(1+8*v1*v1<=9,True)
check([F(36,4),F(4,4)],[9,1]);check(F(9,10),F(36,40))
pca([[1,0],[3,0],[5,0]],[3,0],[[4,0],[0,0]],[4,0],[[1,0],[0,1]])
score=F(24,5);recon=[10+score*F(3,5),20+score*F(4,5)]
check(recon,[F(322,25),F(596,25)]);res=[14-recon[0],23-recon[1]]
check(dot(res,[3,4]),0);check(dot(res,res),F(49,25))
check(F(7+2,7+2+1),F(9,10));check(5*1,5)
constant=pca([[2,3],[2,3],[2,3]],[2,3],[[0,0],[0,0]],[0,0],[[1,0],[0,1]])
check(constant['evr'],None);check(constant['sse'],0)
tied=pca([[2,0],[0,2],[-2,0],[0,-2]],[0,0],[[F(8,3),0],[0,F(8,3)]],[F(8,3),F(8,3)],[[1,0],[0,1]])
check(tied['evr'],F(1,2))
check(stats([[2,20],[4,40],[6,60]])[2],[[4,40],[40,400]])
check([[F(x)/s for x,s in zip(row,[2,20])] for row in stats([[2,20],[4,40],[6,60]])[1]],[[-1,-1],[0,0],[1,1]])
check(10*10,100);check(100*5+600+600*5,4100);check(F(100,1)/F('100.1'),F(1000,1001))
# Fresh no-hint mixed computations and complete source data.
check(stats([[1,4],[3,0],[8,2]])[0],[4,2]);check(stats([[1,4],[3,0],[8,2]])[2],[[13,-2],[-2,4]])
mixed=pca([[5,5],[4,6],[1,3],[2,2]],[3,4],[[F(10,3),F(8,3)],[F(8,3),F(10,3)]],[6,F(2,3)],[[1,1],[1,-1]])
check(mixed['score_numerators'][0],[3,3,-3,-3]);check(mixed['evr'],F(9,10));check(mixed['sse'],2)
check(mixed['reconstructed'],[[F(9,2),F(11,2)],[F(9,2),F(11,2)],[F(3,2),F(5,2)],[F(3,2),F(5,2)]])
check([F(v*v,5) for v in [10,5,0,0]],[20,5,0,0]);check(F(20,25),F(4,5))
y=[F(2),F(1)];yhat=[F(3,2),F(3,2)];check(dot([u-v for u,v in zip(y,yhat)],[1,1]),0)
dhat=[10+2*yhat[0],100+10*yhat[1]];check(dhat,[13,115]);check(dot([1,-5],[2,10]),-48)
# Same-source duplicates, source statement/data retention and all figure assets.
a=ROOT/'resources/lectures/WK6_PCA.pdf';b=ROOT/'resources/lectures/Week 6 Slides - PCA (1).pdf'
check(hashlib.sha256(a.read_bytes()).digest(),hashlib.sha256(b.read_bytes()).digest())
chapter=ROOT/'book/lecture6';pages=[chapter/f for f in ['index.md','principal-components.md','applications.md','cheatsheet.md']]
for literal in ['| 1 | 10 | 90 |','| 2 | 6 | 80 |','| 3 | 20 | 100 |']:
 check(literal in (chapter/'principal-components.md').read_text(),True)
check(re.findall(r'\(w6-p(\d+)\)=',(chapter/'practice.md').read_text()),[f'{n:02}' for n in range(1,29)])
check(re.findall(r'\(w6-s(\d+)\)=',(chapter/'solutions.md').read_text()),[f'{n:02}' for n in range(1,29)])
check(re.findall(r'^## ([A-L]) ·','\n'.join(p.read_text() for p in pages),re.M),list('ABCDEFGHIJKL'))
check(sum(p.read_text().count('class: checkpoint') for p in pages),12)
check(sum(len(re.findall(r'^:::::\{admonition\} Worked example 6\.',p.read_text(),re.M)) for p in pages),15)
assets=ROOT/'book/figures/lecture6';svgs=list(assets.glob('*.svg'));check(len(svgs),7)
for f in svgs:
 tree=ET.parse(f);check(tree.getroot().tag,'{http://www.w3.org/2000/svg}svg');check(tree.find('{http://www.w3.org/2000/svg}desc') is not None,True)
for file,shape in [('genetics-source.png',(670,554)),('eigenfaces-source.png',(3911,698))]:
 data=(assets/file).read_bytes();check(data[:8],b'\x89PNG\r\n\x1a\n');check(struct.unpack('>II',data[16:24]),shape)
print(f'Lecture 6: {checks} exact statistics, spectral, projection, reconstruction, preprocessing and source/asset checks passed.')
