"""Reproduce three original Lecture 2 diagrams using the shared SVG palette."""
from pathlib import Path
import build_lecture1_figures as f
f.OUT = Path(__file__).resolve().parents[1] / 'book/figures/lecture2'

def views():
    p=f.start(1000,340,'Two views constrain one matched point',
        'Front readings (2,3) and side readings (3,4) stack into (2,3,3,4). The repeated Y is an agreement check. Front alone leaves Z free.')
    f.text(p,25,42,'Two views constrain one matched point','title')
    cards=[(25,'World point',['X = 2','Y = 3','Z = 4']),(350,'Matched views',['Front: (X, Y) = (2, 3)','Side: (Y, Z) = (3, 4)']),(735,'Stacked record',['(2, 3, 3, 4)','Y appears twice'])]
    for x,title,lines in cards:
        width=300 if x==350 else 240
        p.append(f'<rect x="{x}" y="76" width="{width}" height="165" rx="12" fill="#FFF0F6" stroke="{f.DEEP_PINK}" stroke-width="2"/>')
        f.text(p,x+16,109,title)
        for j,line in enumerate(lines):f.text(p,x+16,146+34*j,line,'small')
    for a,b in [(275,335),(665,720)]:f.path(p,f'M{a} 158 H{b}',extra='marker-end="url(#arrow)"')
    f.text(p,25,284,'Front only: (2, 3, t), any real t. Both views: (2, 3, 4).')
    f.text(p,25,319,'Calibrated parallel-ray views, fixed origin, and matched labeled points.','small')
    f.write('matched-views.svg',p)

def pictures():
    p=f.start(1000,455,'One system: intersection and column weights',
        'Lines y=(x-1)/2 and y=(11-3x)/2 intersect at (3,1). The same numbers weight columns (1,3) and (-2,2) to produce (1,11).')
    f.text(p,25,39,'One system: intersection and column weights','title')
    # Plot visible segments in x=0..4, y=-1..6; 44 pixels per unit.
    ox,oy,s=80,354,44
    for x in range(5):
        f.path(p,f'M{ox+x*s} 90 V398','#E3D8D0',1)
        f.text(p,ox+x*s,oy+25,str(x),'small','text-anchor="middle"')
    for y in range(-1,7):
        f.path(p,f'M{ox} {oy-y*s} H{ox+4*s}','#E3D8D0',1)
        if y!=0:f.text(p,ox-15,oy-y*s+6,str(y),'small','text-anchor="end"')
    f.path(p,f'M{ox} {oy} H285',extra='marker-end="url(#arrow)"')
    f.path(p,f'M{ox} 398 V75',extra='marker-end="url(#arrow)"')
    f.text(p,293,oy+6,'x');f.text(p,ox-6,66,'y')
    f.path(p,f'M{ox} {oy+.5*s} L{ox+4*s} {oy-1.5*s}',f.DEEP_PINK,3)
    f.path(p,f'M{ox} {oy-5.5*s} L{ox+4*s} {oy+.5*s}',f.DEEP_GREEN,3,extra='stroke-dasharray="8 5"')
    f.point(p,ox+3*s,oy-s);f.text(p,ox+3*s+14,oy-s-12,'(3, 1)')
    f.text(p,360,111,'Rows: both equations must hold')
    f.text(p,360,157,'x − 2y = 1',extra=f'style="fill:{f.DEEP_PINK}"')
    f.text(p,360,198,'3x + 2y = 11',extra=f'style="fill:{f.DEEP_GREEN}"')
    f.text(p,360,270,'Columns: the same x, y are weights')
    f.text(p,360,314,'3(1, 3) + 1(−2, 2) = (1, 11)')
    f.text(p,360,366,'Unknown point: (3, 1). Target: (1, 11).','small')
    f.text(p,25,430,'Solid pink: first line. Dashed green: second line. Their common point satisfies both.','small')
    f.write('three-pictures.svg',p)

def echelon():
    p=f.start(1000,365,'REF → RREF: preserve the solution, clarify the rows',
        'Highlighted pivots form a staircase in REF. RREF makes pivots one and clears entries above. Both augmented matrices represent solution (5,4,2).')
    f.text(p,25,40,'REF → RREF: preserve the solution, clarify the rows','title')
    for x,title,rows in [(50,'REF: zeros below',[[1,1,3,15],[0,1,1,6],[0,0,-1,-2]]),(580,'RREF: lone unit pivots',[[1,0,0,5],[0,1,0,4],[0,0,1,2]])]:
        f.text(p,x,87,title)
        for col,label in enumerate(['x','y','z','rhs']):f.text(p,x+col*80+12,125,label,'small')
        for i,row in enumerate(rows):
            for j,val in enumerate(row):
                xx,yy=x+j*80+17,165+i*49
                if j==i:p.append(f'<rect x="{xx-23}" y="{yy-27}" width="46" height="39" rx="8" fill="{f.GREEN}" stroke="{f.DEEP_GREEN}" stroke-width="2"/>')
                f.text(p,xx,yy,str(val),extra='text-anchor="middle"')
        f.path(p,f'M{x+215} 135 V278',f.INK,2)
    f.path(p,'M410 212 H535',extra='marker-end="url(#arrow)"')
    f.text(p,423,181,'reduce','small')
    f.text(p,25,325,'Green boxes mark pivots. RHS stays attached; it is not a variable column.','small')
    f.write('echelon.svg',p)

if __name__=='__main__':
    views(); pictures(); echelon()
    print('Generated three Lecture 2 SVG diagrams.')
