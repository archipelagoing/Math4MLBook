"""Reproduce four original Lecture 3 SVGs with the established palette."""
from pathlib import Path
import build_lecture1_figures as f
f.OUT=Path(__file__).resolve().parents[1]/'book/figures/lecture3'

def begin(w,h,title,desc):
    p=f.start(w,h,title,desc)
    p.append(f'<defs><marker id="pink-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="{f.DEEP_PINK}"/></marker><marker id="green-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="{f.DEEP_GREEN}"/></marker></defs>')
    f.text(p,25,40,title,'title');return p

def arrow(p,x1,y1,x2,y2,color='pink',dash=False):
    f.path(p,f'M{x1} {y1} L{x2} {y2}',f.DEEP_PINK if color=='pink' else f.DEEP_GREEN,3,
           extra=f'marker-end="url(#{color}-arrow)"'+(' stroke-dasharray="7 5"' if dash else ''))

def axes(p,ox,oy,scale,lo,hi):
    for i in range(lo,hi+1):
        f.path(p,f'M{ox+i*scale} {oy-hi*scale} V{oy-lo*scale}','#E3D8D0',1)
        f.path(p,f'M{ox+lo*scale} {oy-i*scale} H{ox+hi*scale}','#E3D8D0',1)
        f.text(p,ox+i*scale,oy+22,str(i),'small','text-anchor="middle"')
    f.path(p,f'M{ox+lo*scale} {oy} H{ox+hi*scale+13}',extra='marker-end="url(#arrow)"')
    f.path(p,f'M{ox} {oy-lo*scale} V{oy-hi*scale-13}',extra='marker-end="url(#arrow)"')
    f.text(p,ox+hi*scale+22,oy+5,'x','small');f.text(p,ox-5,oy-hi*scale-25,'y','small')

def subspaces():
    p=begin(1050,460,'Closure is a test, not a shape impression',
        'A line y=x through zero contains (1,1) and its negative (-1,-1). A first-quadrant region contains (1,1) but not its negative.')
    f.text(p,65,88,'Line through zero: y = x')
    axes(p,250,245,60,-2,2)
    f.path(p,'M130 365 L370 125',f.BLUE,2,extra='stroke-dasharray="5 5"')
    arrow(p,250,245,310,185);arrow(p,250,245,190,305,'green')
    f.text(p,320,175,'v','small');f.text(p,145,310,'−v','small')
    f.text(p,80,410,'Both remain in the line.','small')
    f.text(p,590,88,'First quadrant: x ≥ 0, y ≥ 0')
    p.append('<rect x="775" y="125" width="120" height="120" fill="#FFF0A6"/>')
    axes(p,775,245,60,-2,2)
    arrow(p,775,245,835,185);arrow(p,775,245,715,305,'green',True)
    f.text(p,845,180,'v: inside','small');f.text(p,622,336,'−v: outside','small')
    f.text(p,590,410,'Negative scaling leaves the set.','small')
    f.text(p,25,446,'The shaded quadrant is only the portion shown. Coordinates extend beyond the drawing.','small')
    f.write('subspace-test.svg',p)

def spaces():
    p=begin(1050,510,'Two views make the four spaces tangible',
        'O maps R3 input points to R2 front readings; H maps R3 to R4 stacked readings. Input cards list row and null spaces, output cards list column and left null spaces.')
    for y,name,input_lines,output_lines in [
        (100,'O: front view',['Input: ℝ³','Row space: XY coordinate plane','Null space: all (0, 0, t)'],['Output: ℝ²','Column space: every screen pair','Left null space: {0}']),
        (300,'H: stacked views',['Input: ℝ³','Row space: all ℝ³','Null space: {0}'],['Output: ℝ⁴','Column space: b2 = b3','Left null: span of (0, 1, −1, 0)'])]:
        for x,w,lines,fill in [(25,355,input_lines,'#FFF0F6'),(565,460,output_lines,'#EFF9E7')]:
            p.append(f'<rect x="{x}" y="{y}" width="{w}" height="153" rx="12" fill="{fill}" stroke="{f.BLUE}" stroke-width="1.5"/>')
            for i,line in enumerate(lines):f.text(p,x+16,y+34+i*43,line,'small')
        f.text(p,398,y+37,name,'small')
        f.path(p,f'M395 {y+74} H547',width=3,extra='marker-end="url(#arrow)"')
    f.text(p,25,487,'Input changes versus output compatibility: different spaces answer different questions.','small')
    f.write('four-spaces.svg',p)

def independence():
    p=begin(1050,400,'Independence checks the whole list',
        'Two collinear arrows are dependent, two nonparallel arrows are independent, three planar arrows can be dependent with the third equal to the sum of the first two.')
    for x,title in [(30,'One line'),(370,'Two directions'),(710,'Three planar arrows')]:f.text(p,x,91,title)
    arrow(p,120,275,245,150);arrow(p,120,275,182.5,212.5,'green')
    f.text(p,242,130,'2v','small');f.text(p,142,200,'v','small')
    arrow(p,505,275,575,165);arrow(p,505,275,420,175,'green')
    f.text(p,566,148,'u','small');f.text(p,403,156,'v','small')
    arrow(p,805,275,920,275);arrow(p,805,275,805,160,'green')
    f.path(p,'M805 275 L920 160',f.BLUE,3,extra='marker-end="url(#arrow)"')
    f.text(p,935,281,'u','small');f.text(p,782,148,'v','small');f.text(p,919,145,'w','small')
    for x,result in [(30,'Dependent: one is a multiple.'),(370,'Independent: not parallel.'),(710,'Dependent: w = u + v.')]:f.text(p,x,337,result,'small')
    f.text(p,25,380,'At most n vectors can be independent in ℝⁿ; pairwise nonparallel is not enough for a longer list.','small')
    f.write('independence.svg',p)

def basis():
    p=begin(1050,480,'Same screen vector, different coefficient labels',
        'Fixed X,Y axes show b1=(3,1), b2=(1,1). The partial 1.5b1=(4.5,1.5), then adding 0.5b2=(0.5,0.5), reaches x=(5,2).')
    ox,oy,scale=80,340,65
    for x in range(7):
        f.path(p,f'M{ox+x*scale} 125 V{oy}','#E3D8D0',1)
        f.text(p,ox+x*scale,oy+23,str(x),'small','text-anchor="middle"')
    for y in range(4):
        f.path(p,f'M{ox} {oy-y*scale} H{ox+6*scale}','#E3D8D0',1)
        f.text(p,ox-15,oy-y*scale+5,str(y),'small','text-anchor="end"')
    f.path(p,f'M{ox} {oy} H490',extra='marker-end="url(#arrow)"')
    f.path(p,f'M{ox} {oy} V110',extra='marker-end="url(#arrow)"')
    f.text(p,495,oy+5,'X','small');f.text(p,ox-8,100,'Y','small')
    arrow(p,ox,oy,ox+3*scale,oy-scale);arrow(p,ox,oy,ox+scale,oy-scale,'green')
    f.text(p,ox+3*scale+7,oy-scale+23,'b1 = (3, 1)','small')
    f.text(p,ox+scale-44,oy-scale-18,'b2 = (1, 1)','small')
    partial=(ox+4.5*scale,oy-1.5*scale);target=(ox+5*scale,oy-2*scale)
    f.path(p,f'M{ox} {oy} L{partial[0]} {partial[1]}',f.DEEP_PINK,2,extra='stroke-dasharray="6 5"')
    arrow(p,*partial,*target,'green');f.point(p,*target)
    f.text(p,target[0]+12,target[1]-9,'(5, 2)','small')
    f.text(p,565,145,'Basis columns: (3, 1), (1, 1)','small')
    f.text(p,565,204,'New coefficients: (3/2, 1/2)')
    f.text(p,565,253,'Natural coordinates: (5, 2)')
    f.text(p,565,306,'3/2 b1 + 1/2 b2 reaches the same point.','small')
    f.text(p,25,415,'Solid arrows: basis directions. Dashed leg: 3/2 b1. Final green leg: 1/2 b2.','small')
    f.text(p,25,451,'Coordinates change; the calibrated origin and the screen mark stay fixed.','small')
    f.write('basis-coordinates.svg',p)

if __name__=='__main__':
    subspaces();spaces();independence();basis()
    print('Generated four original Lecture 3 SVGs.')
