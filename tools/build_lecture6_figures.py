"""Reproduce seven Week 6 SVGs and extract two credited empirical source figures."""
from pathlib import Path
from math import sqrt,sin,cos,pi
from tempfile import TemporaryDirectory
import shutil,subprocess
import build_lecture1_figures as f
ROOT=Path(__file__).resolve().parents[1];f.OUT=ROOT/'book/figures/lecture6'

def begin(w,h,title,desc):
 p=f.start(w,h,title,desc);f.text(p,25,40,title,'title')
 for name,c in [('pink',f.DEEP_PINK),('green',f.DEEP_GREEN)]:
  p.append(f'<defs><marker id="{name}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="{c}"/></marker></defs>')
 return p

def arrow(p,a,b,color='pink'):
 f.path(p,f'M{a[0]} {a[1]} L{b[0]} {b[1]}',f.DEEP_PINK if color=='pink' else f.DEEP_GREEN,2.5,extra=f'marker-end="url(#{color})"')

def axis(p,ox,oy,s,xmax,ymax,xlabel='x',ylabel='y',negative=False):
 f.path(p,f'M{ox-s*xmax if negative else ox} {oy} H{ox+s*xmax}',f.BLUE,1.5,extra='marker-end="url(#arrow)"')
 f.path(p,f'M{ox} {oy+s*ymax if negative else oy} V{oy-s*ymax}',f.BLUE,1.5,extra='marker-end="url(#arrow)"')
 f.text(p,ox+s*xmax+8,oy+7,xlabel,'small');f.text(p,ox+5,oy-s*ymax-9,ylabel,'small')

def dimensions():
 p=begin(1080,430,'Many measured entries can vary in only a few directions',
 'A 300 by 300 RGB image becomes 270000 numerical features in one row. A three-feature cloud near a plane has two dominant within-plane directions and smaller perpendicular deviations.')
 f.text(p,30,95,'One image → one observation row')
 for j in range(3):
  for i in range(4):p.append(f'<rect x="{50+i*50}" y="{130+j*50}" width="47" height="47" fill="'+[f.PINK,f.GREEN,'#FFF0A6','#C4D9FA'][(i+j)%4]+'"/>')
 f.text(p,285,157,'300 × 300 × 3','small');f.text(p,285,203,'= 270,000 entries','small')
 f.text(p,30,326,'Fixed order: R, G, B, then the next pixel.','small')
 f.text(p,570,95,'Three features; approximately a plane','small')
 p.append('<polygon points="595,282 875,160 1010,246 735,370" fill="#EFF9E7" stroke="#357D22"/>')
 for i in range(20):
  a=(i%5)/5;b=(i//5)/4;x=620+230*a+90*b;y=280-100*a+65*b+(-1)**i*8
  p.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{f.DEEP_PINK}"/>')
 arrow(p,(760,270),(880,215));arrow(p,(760,270),(810,307),'green')
 f.text(p,25,399,'The pixel array and point cloud are schematics; fewer coordinates trade detail for a measured approximation.','small')
 f.write('dimensions.svg',p)

def pizza():
 p=begin(1080,425,'Center → use long and short axes → retain one coordinate',
 'Toy pizza/gym counts (1,5),(2,4),(3,3),(4,2),(5,1) form a line. Centering at (3,3) gives scores along (1,-1)/sqrt2 with zero perpendicular scores; the retained one-dimensional scores are minus 2sqrt2, minus sqrt2, zero, sqrt2, 2sqrt2.')
 f.text(p,25,93,'1. Raw paired counts','small');f.text(p,395,93,'2. Centered directions','small');f.text(p,770,93,'3. Retained score','small')
 axis(p,55,320,37,6,5,'Pizza','Gym')
 for x,y in [(1,5),(2,4),(3,3),(4,2),(5,1)]:f.point(p,55+37*x,320-37*y)
 axis(p,550,230,30,4,4,'x','y',True)
 for x in [-2,-1,0,1,2]:f.point(p,550+30*x,230+30*x)
 arrow(p,(550,230),(630,310));arrow(p,(550,230),(600,180),'green')
 f.text(p,600,334,'q₁','small');f.text(p,600,163,'q₂','small')
 f.path(p,'M780 240 H1040',f.BLUE,2,extra='marker-end="url(#arrow)"')
 for i,label in enumerate(['−2√2','−√2','0','√2','2√2']):
  x=795+i*52;f.point(p,x,240);f.text(p,x,277,label,'small','text-anchor="middle"')
 f.text(p,770,320,'Short-direction scores are all 0.','small')
 f.text(p,25,399,'Declared toy observations; the source scatter is noisy and has no supplied raw coordinates.','small')
 f.write('pizza-gym.svg',p)

def objective():
 p=begin(1080,450,'Retained squared length plus residual error equals the total',
 'Vector (2,1) projects onto the horizontal unit direction to (2,0); residual (0,1) is perpendicular. A second panel shows an elongated downward cloud, its long/short orthogonal axes and perpendicular projection segments onto the long axis.')
 ox,oy,s=70,320,90;axis(p,ox,oy,s,3,2,'x','y')
 arrow(p,(ox,oy),(ox+2*s,oy-s));arrow(p,(ox,oy),(ox+2*s,oy),'green')
 f.path(p,f'M{ox+2*s} {oy} V{oy-s}',f.BLUE,2,extra='stroke-dasharray="5 4"')
 f.path(p,f'M{ox+2*s-12} {oy} v-12 h12',f.INK,1)
 f.text(p,125,199,'x = (2, 1)','small');f.text(p,168,350,'projection (2, 0)','small');f.text(p,270,261,'error (0, 1)','small')
 f.text(p,52,390,'5 = 4 + 1','label')
 c=(790,240);arrow(p,(660,110),(920,370));arrow(p,c,(865,165),'green')
 f.text(p,932,365,'long','small');f.text(p,868,154,'short','small')
 for t,e in [(-110,8),(-85,-14),(-65,21),(-30,-9),(10,12),(30,-24),(70,13),(98,-8)]:
  foot=(c[0]+t,c[1]+t);point=(foot[0]+e,foot[1]-e)
  f.point(p,*point);f.path(p,f'M{point[0]} {point[1]} L{foot[0]} {foot[1]}',f.DEEP_GREEN,1.5)
 f.text(p,580,416,'Choose the long axis for the cloud, not just for one point.','small')
 f.write('projection-objective.svg',p)

def students():
 p=begin(1080,490,'One component for the three source students',
 'Original student rows (10,90),(6,80),(20,100) center at (12,90). A centered plot shows the points and their perpendicular projections onto direction (5,7)/sqrt74, with equal x and y coordinate scales.')
 f.text(p,30,100,'Mean: (12, 90)');f.text(p,30,155,'Centered rows:','small')
 for i,t in enumerate(['(−2, 0)','(−6, −10)','(8, 10)']):f.text(p,50,202+39*i,t,'small')
 f.text(p,30,365,'Unit loading: (5, 7) / √74','small')
 ox,oy,s=765,255,13;axis(p,ox,oy,s,13,12,'Δstudy','Δexam',True)
 f.path(p,f'M{ox-100} {oy+140} L{ox+100} {oy-140}',f.BLUE,2)
 for i,(x,y) in enumerate([(-2,0),(-6,-10),(8,10)],1):
  a=(5*x+7*y)/74;xp,yp=5*a,7*a
  f.path(p,f'M{ox+x*s} {oy-y*s} L{ox+xp*s} {oy-yp*s}',f.DEEP_GREEN,2)
  f.point(p,ox+x*s,oy-y*s);f.point(p,ox+xp*s,oy-yp*s,True)
  f.text(p,ox+x*s+10,oy-y*s+16,str(i),'small')
 f.text(p,30,451,'Pink circles: centered originals. Green diamonds: nearest points on the PC1 line.','small')
 f.write('student-pca.svg',p)

def budget():
 p=begin(1000,450,'Same total variance, different coordinate directions',
 'Two stacked bars both total 152. Original feature variances are 52 and 100; principal-coordinate variances are 150 and 2. Retaining PC1 keeps 150/152, about 98.7 percent.')
 s=1.65;bottom=350
 for x,values,labels in [(160,[52,100],['Study: 52','Exam: 100']),(610,[150,2],['PC1: 150','PC2: 2'])]:
  y=bottom
  for i,(v,label) in enumerate(zip(values,labels)):
   h=v*s;y-=h;p.append(f'<rect x="{x}" y="{y}" width="200" height="{h}" fill="'+('#8DEB42' if i==0 else '#C4D9FA')+f'" stroke="{f.INK}"/>')
   if h>25:f.text(p,x+100,y+h/2+5,label,'label','text-anchor="middle"')
   else:f.text(p,x+215,y+5,label,'small');f.path(p,f'M{x+200} {y+2} h10',f.BLUE,1)
  f.text(p,x+100,82,'Total: 152','label','text-anchor="middle"')
 f.text(p,160,388,'Original axes');f.text(p,600,388,'Principal axes')
 f.text(p,25,430,'PC1 retains 150 / 152 = 75 / 76 ≈ 98.7%; PC2 contains the remaining variance.','small')
 f.write('variance-budget.svg',p)

def preprocessing():
 p=begin(1080,640,'The complete preprocessing and reconstruction path',
 'Six panels follow the exact toy rows (1,10),(2,20),(3,30): raw values, centering at (2,20), scaling by (1,10), selecting orthogonal standardized axes, projection onto their leading axis, and undoing scaling and centering to recover original rows.')
 panels=[('1. Raw data',[(1,10),(2,20),(3,30)],(0,0),(30,5),False),
 ('2. Center', [(-1,-10),(0,0),(1,10)],(0,0),(40,6),True),
 ('3. Standardize',[(-1,-1),(0,0),(1,1)],(0,0),(45,45),True),
 ('4. Find axes',[(-1,-1),(0,0),(1,1)],(0,0),(45,45),True),
 ('5. Project',[(-1,-1),(0,0),(1,1)],(0,0),(45,45),True),
 ('6. Restore units',[(1,10),(2,20),(3,30)],(0,0),(30,5),False)]
 for j,(title,points,_,scale,centered) in enumerate(panels):
  bx=25+j%3*355;by=85+j//3*265
  p.append(f'<rect x="{bx}" y="{by}" width="330" height="235" rx="10" fill="white" stroke="#E3D4CA"/>')
  f.text(p,bx+12,by+30,title,'label');ox=bx+(160 if centered else 85);oy=by+(135 if centered else 200);sx,sy=scale
  f.path(p,f'M{bx+45} {oy} H{bx+285}',f.BLUE,1);f.path(p,f'M{ox} {by+50} V{by+210}',f.BLUE,1)
  if j in (3,4):
   arrow(p,(ox-60,oy+60),(ox+60,oy-60));arrow(p,(ox,oy),(ox+45,oy+45),'green')
  for x,y in points:f.point(p,ox+x*sx,oy-y*sy,second=(j==4 or j==5))
 f.text(p,25,626,'Toy data have zero discarded variance; scaling makes their raw slope 10 become standardized slope 1.','small')
 f.write('preprocessing.svg',p)

def failures():
 p=begin(1080,445,'Three ways high retained variance can miss the intended goal',
 'Left: a far vertical point changes the leading direction of three horizontal points. Center: a linear projection cannot follow a curved arch. Right: horizontally spread classes separated only vertically merge after keeping the horizontal coordinate.')
 for x,title in [(25,'One outlier changes PC1'),(385,'A line misses a curve'),(745,'Low variance can carry labels')]:f.text(p,x,98,title,'small')
 f.path(p,'M65 330 H270',f.BLUE,1.5,extra='marker-end="url(#arrow)"')
 f.path(p,'M165 355 V125',f.BLUE,1.5,extra='marker-end="url(#arrow)"')
 f.text(p,280,337,'x','small');f.text(p,172,115,'y','small')
 for x,y in [(-2,0),(0,0),(2,0),(0,10)]:f.point(p,165+13*x,330-13*y)
 f.path(p,'M80 330 H250',f.BLUE,2,extra='stroke-dasharray="5 4"');arrow(p,(165,345),(165,180),'green')
 f.path(p,'M410 310 H650',f.BLUE,1.5,extra='marker-end="url(#arrow)"')
 f.path(p,'M530 350 V150',f.BLUE,1.5,extra='marker-end="url(#arrow)"')
 f.text(p,658,317,'x','small');f.text(p,536,140,'y','small')
 for i in range(21):
  x=-2+4*i/20;y=2-x*x/2;f.point(p,530+40*x,310-40*y)
 f.path(p,'M435 270 H630',f.BLUE,2)
 axis(p,875,280,24,5,4,'x','y',True)
 for i,x in enumerate([-3,-1,1,3]):
  f.point(p,875+24*x,255,True);f.point(p,875+24*x,305)
 f.path(p,'M770 280 H985',f.BLUE,2);f.text(p,770,365,'Same x scores, different classes.','small')
 f.text(p,25,417,'These are declared teaching datasets, not the source’s unprovided numerical observations.','small')
 f.write('failure-cases.svg',p)

def empirical():
 # Extract unchanged embedded images. No crop, invented data or AI image editing.
 with TemporaryDirectory() as temp:
  prefix=Path(temp)/'source'
  subprocess.run(['pdfimages','-f','34','-l','35','-png',str(ROOT/'resources/lectures/WK6_PCA.pdf'),str(prefix)],check=True)
  f.OUT.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(Path(temp)/'source-000.png',f.OUT/'genetics-source.png')
  shutil.copyfile(Path(temp)/'source-001.png',f.OUT/'eigenfaces-source.png')

if __name__=='__main__':
 dimensions();pizza();objective();students();budget();preprocessing();failures();empirical()
 print('Built seven original SVGs and extracted two credited source illustrations.')
