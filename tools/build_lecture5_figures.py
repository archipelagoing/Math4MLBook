"""Reproduce six source-grounded Lecture 5 SVG diagrams."""
from pathlib import Path
from math import cos,sin,pi
import build_lecture1_figures as f
f.OUT=Path(__file__).resolve().parents[1]/'book/figures/lecture5'

def begin(w,h,title,desc):
 p=f.start(w,h,title,desc);f.text(p,25,40,title,'title')
 for name,color in [('pink',f.DEEP_PINK),('green',f.DEEP_GREEN)]:
  p.append(f'<defs><marker id="{name}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="{color}"/></marker></defs>')
 return p

def arrow(p,a,b,color='pink',dashed=False):
 f.path(p,f'M{a[0]} {a[1]} L{b[0]} {b[1]}',f.DEEP_PINK if color=='pink' else f.DEEP_GREEN,3,extra=f'marker-end="url(#{color})"'+(' stroke-dasharray="6 4"' if dashed else ''))

def polygon(p,points,fill='#FFF0F6',stroke=f.DEEP_PINK,dash=False):
 p.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="{fill}" stroke="{stroke}" stroke-width="2"'+(' stroke-dasharray="5 5"' if dash else '')+'/>')

def transforms():
 p=begin(1080,505,'Changing a direction versus preserving its line',
         'Left: matrix [2,-1;1,2] maps (2,3) to (1,8). Right: [2,1;2,3] maps (1,2) to (4,8), on the same line. Both panels use equal coordinate scales.')
 for ox,title,v,w in [(95,'A = [2, −1; 1, 2]',(2,3),(1,8)),(635,'B = [2, 1; 2, 3]',(1,2),(4,8))]:
  oy,s=390,32;f.text(p,ox-35,91,title)
  f.axes(p,ox,oy,s,s,5,8,'x','y')
  xy=lambda a:(ox+s*a[0],oy-s*a[1])
  arrow(p,(ox,oy),xy(w),'green');arrow(p,(ox,oy),xy(v),'pink')
  f.text(p,*[xy(v)[0]+12,xy(v)[1]+8],f'v = {v}','small')
  f.text(p,xy(w)[0]+16,xy(w)[1]-8,f'output = {w}','small')
 f.text(p,45,452,'Different coordinate ratios: no common λ.','small')
 f.text(p,585,452,'Output = 4v: one preserved line.','small')
 f.text(p,25,489,'Source vectors and products from PDF pages 3–8. Green: output. Pink: input.','small')
 f.write('transformed-vectors.svg',p)

def stretch():
 p=begin(1080,470,'A stretch keeps two eigenlines; a 45° turn keeps none',
         'Two equally scaled coordinate panels show the original square with dashed outline. Under diag(1,2) it becomes a vertical rectangle; under a 45 degree rotation it becomes a diamond. Axis unit vectors stay on their lines only for the stretch.')
 square=[(-1,-1),(1,-1),(1,1),(-1,1)]
 for ox,title,transform in [(260,'D = diag(1, 2)',lambda x,y:(x,2*y)),(800,'R: 45° counterclockwise',lambda x,y:((x-y)/2**.5,(x+y)/2**.5))]:
  oy,s=270,67;xy=lambda a:(ox+s*a[0],oy-s*a[1])
  f.text(p,ox-170,95,title)
  polygon(p,[xy(a) for a in square],fill='none',stroke=f.BLUE,dash=True)
  polygon(p,[xy(transform(*a)) for a in square],fill='#EFF9E7',stroke=f.DEEP_GREEN)
  f.path(p,f'M{ox-160} {oy} H{ox+170}',f.BLUE,1,extra='marker-end="url(#arrow)"')
  f.path(p,f'M{ox} {oy+150} V{oy-160}',f.BLUE,1,extra='marker-end="url(#arrow)"')
  for a in [(1,0),(0,1)]:arrow(p,(ox,oy),xy(transform(*a)),'pink')
  f.text(p,ox+173,oy+5,'x','small');f.text(p,ox+10,oy-130,'y','small')
 f.text(p,70,437,'Eigenvalues 1 and 2; axes stay on their lines.','small')
 f.text(p,605,437,'No nonzero real vector stays on its line.','small')
 f.write('stretch-and-rotation.svg',p)

def svd_geometry():
 p=begin(1080,490,'SVD pairs input directions with output stretch directions',
         'A unit circle with right unit axes v1 at 45 degrees and v2 at 135 degrees maps to an ellipse with semiaxes 3u1 and u2, with u1 at 30 degrees and u2 at 120 degrees. Right and left axes are each orthonormal.')
 for ox,title,t,scales in [(250,'Input: unit circle',pi/4,(1,1)),(800,'Output: ellipse',pi/6,(3,1))]:
  oy,s=280,58;f.text(p,ox-160,92,title)
  def xy(x,y):return ox+s*x,oy-s*y
  points=[]
  for j in range(121):
   a=2*pi*j/120;x=scales[0]*cos(a);y=scales[1]*sin(a)
   points.append(xy(cos(t)*x-sin(t)*y,sin(t)*x+cos(t)*y))
  polygon(p,points,'#EFF9E7',f.DEEP_GREEN)
  for j,ang in enumerate([t,t+pi/2]):
   end=xy(scales[j]*cos(ang),scales[j]*sin(ang));arrow(p,(ox,oy),end,'pink' if j==0 else 'green')
   f.text(p,end[0]+10,end[1]-12,('v₁' if j==0 else 'v₂') if ox==250 else ('3u₁' if j==0 else 'u₂'),'small')
 f.path(p,'M390 270 H555',f.BLUE,3,extra='marker-end="url(#arrow)"');f.text(p,455,240,'A')
 f.text(p,40,424,'A v₁ = 3u₁; A v₂ = u₂. Each pair of axes is perpendicular in its own space.','small')
 f.text(p,40,465,'A concrete illustration of the source’s circle-to-ellipse geometry; σ₁ = 3, σ₂ = 1.','small')
 f.write('svd-geometry.svg',p)

def factors():
 p=begin(1080,520,'Factor dimensions: full and compact are both exact',
         'Full A m by n equals U m by m, Sigma m by n and V transpose n by n. Compact rank-r factors have dimensions m by r, r by r and r by n. Full U and V are orthogonal; compact columns are orthonormal.')
 for y,title,shapes in [(125,'Full SVD',['A: m × n','U: m × m','Σ: m × n','Vᵀ: n × n']),(325,'Compact SVD',['A: m × n','Uᵣ: m × r','Σᵣ: r × r','Vᵣᵀ: r × n'])]:
  f.text(p,25,y-33,title)
  for i,label in enumerate(shapes):
   x=25+i*265;p.append(f'<rect x="{x}" y="{y}" width="225" height="90" rx="12" fill="'+('#FFF0F6' if i%2==0 else '#EFF9E7')+f'" stroke="{f.BLUE}"/>')
   f.text(p,x+17,y+52,label)
   if i<3:f.text(p,x+237,y+52,'=' if i==0 else '×')
 f.text(p,25,476,'r = rank(A). Compact Σ contains only positive strengths. Do not invert rectangular compact factors.','small')
 f.write('factor-shapes.svg',p)

def truncation():
 p=begin(1080,480,'Keep k directions; reconstruct the original outer shape',
         'A compact exact matrix factorization has inner size r. Truncation keeps k columns of U and V and k diagonal strengths. The row-coordinate table Z has m by k entries, while its reconstruction remains m by n.')
 for i,(x,w,title,shape) in enumerate([(25,210,'Uₖ','m × k'),(295,180,'Σₖ','k × k'),(540,210,'Vₖᵀ','k × n'),(825,225,'Rₖ','m × n')]):
  p.append(f'<rect x="{x}" y="150" width="{w}" height="150" rx="10" fill="'+('#EFF9E7' if i%2 else '#FFF0F6')+f'" stroke="{f.BLUE}" stroke-width="2"/>')
  f.text(p,x+w/2,204,title,'title','text-anchor="middle"');f.text(p,x+w/2,264,shape,'label','text-anchor="middle"')
  if i<3:f.text(p,x+w+24,230,'=' if i==2 else '×','title')
 f.text(p,25,100,'A = Uᵣ Σᵣ Vᵣᵀ  →  keep the first k terms, with k ≤ r','small')
 f.text(p,30,365,'Smaller coordinates: Z = R Vₖ = Uₖ Σₖ, size m × k.')
 f.text(p,30,417,'Squared Frobenius error = sum of squared discarded singular values.','small')
 f.write('truncation.svg',p)

def recommendations():
 p=begin(1080,440,'A feature score needs one user row and one movie row',
         'A user feature row passes through diagonal weights and pairs with a movie feature row, yielding a scalar score. The row lengths are both k. Missing ratings are not zero targets; fitting and calibration are separate steps.')
 labels=[('User row Lᵢ','1 × k'),('Weights W','k × k diagonal'),('Movie row Mⱼᵀ','k × 1'),('One score','scalar')]
 for i,(title,shape) in enumerate(labels):
  x=25+265*i;p.append(f'<rect x="{x}" y="145" width="225" height="115" rx="12" fill="'+('#FFF0F6' if i%2==0 else '#EFF9E7')+f'" stroke="{f.BLUE}"/>')
  f.text(p,x+14,185,title);f.text(p,x+14,228,shape,'small')
  if i<3:f.text(p,x+235,209,'=' if i==2 else '×')
 f.text(p,25,102,'Feature order must match in all three factors.','small')
 f.text(p,25,324,'Source example: User 1 × weights × Captain America → 0.0249','small')
 f.text(p,25,381,'That is a raw feature score. The source supplies no fitted conversion to a 1–5 rating.','small')
 f.write('recommendation-flow.svg',p)

if __name__=='__main__':
 transforms();stretch();svd_geometry();factors();truncation();recommendations()
 print('Generated six original Lecture 5 SVGs.')
