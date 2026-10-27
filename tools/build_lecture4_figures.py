"""Reproduce six Lecture 4 vector diagrams in the established textbook palette."""
from pathlib import Path
import build_lecture1_figures as f
f.OUT=Path(__file__).resolve().parents[1]/'book/figures/lecture4'

def begin(w,h,title,desc):
    p=f.start(w,h,title,desc)
    for name,color in [('pink',f.DEEP_PINK),('green',f.DEEP_GREEN)]:
        p.append(f'<defs><marker id="{name}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="{color}"/></marker></defs>')
    f.text(p,25,40,title,'title');return p

def arrow(p,start,end,color='green'):
    f.path(p,f'M{start[0]} {start[1]} L{end[0]} {end[1]}',f.DEEP_GREEN if color=='green' else f.DEEP_PINK,3,extra=f'marker-end="url(#{color})"')

def line():
    p=begin(1000,450,'Projection: keep the line component',
            'On equally scaled x,y axes, b=(3,1) is split into p=(1,2) on the line spanned by (1,2), and e=(2,-1), perpendicular to the line.')
    ox,oy,s=85,340,80
    f.axes(p,ox,oy,s,s,4,3,'x','y')
    def xy(x,y):return ox+s*x,oy-s*y
    f.path(p,f'M{ox} {oy} L{xy(1.45,2.9)[0]} {xy(1.45,2.9)[1]}',f.BLUE,2,extra='stroke-dasharray="6 4"')
    arrow(p,xy(0,0),xy(3,1),'pink');arrow(p,xy(0,0),xy(1,2));arrow(p,xy(1,2),xy(3,1))
    # Equal coordinate scales: dot((1,2),(2,-1)) = 0.
    a=(.12,.24);e=(.24,-.12)
    pts=[xy(1+a[0],2+a[1]),xy(1+a[0]+e[0],2+a[1]+e[1]),xy(1+e[0],2+e[1])]
    f.path(p,'M'+' L'.join(f'{x} {y}' for x,y in pts),f.INK,1.5)
    f.text(p,130,145,'p = (1, 2)','small');f.text(p,335,252,'b = (3, 1)','small');f.text(p,252,174,'e = (2, −1)','small')
    f.text(p,555,125,'b = p + e')
    f.text(p,555,183,'p is on the allowed line.')
    f.text(p,555,233,'e is perpendicular to that line.')
    f.text(p,555,303,'Squared lengths: 10 = 5 + 5','small')
    f.text(p,25,419,'Fixed x,y axes; both axes use the same scale. The residual arrow runs from p to b.','small')
    f.write('line-projection.svg',p)

def measurement():
    p=begin(1000,420,'Two Y readings, one shared fitted value',
            'Two equally weighted observations of Y are 2 and 4. Both fit to 3. Observed minus fitted errors are minus one and plus one.')
    f.text(p,35,99,'Same labeled point · calibrated front and side views','small')
    for y,label,value in [(180,'Front Y reading',2),(275,'Side Y reading',4)]:
        f.text(p,35,y+5,label,'small');f.path(p,f'M300 {y} H880', '#E3D8D0',2)
        for v in (2,3,4):
            x=350+(v-2)*220;f.path(p,f'M{x} {y-7} V{y+7}',f.BLUE,1);f.text(p,x,y+34,str(v),'small','text-anchor="middle"')
        fit=570;obs=350+(value-2)*220
        arrow(p,(fit,y),(obs,y),'pink');f.point(p,obs,y);f.point(p,fit,y,True)
    f.text(p,370,140,'e₂ = 2 − 3 = −1','small');f.text(p,600,245,'e₃ = 4 − 3 = +1','small')
    f.text(p,35,352,'Fitted record: p = (2, 3, 3, 4)');f.text(p,35,390,'Residual: e = (0, −1, +1, 0), with Hᵀe = 0','small')
    f.write('measurement-fit.svg',p)

def least_squares():
    p=begin(1000,460,'Fit vertical errors; check orthogonality in response space',
            'Data points (1,1),(2,2),(3,2), fitted line y=2/3+t/2, and vertical residuals observed minus fitted: minus one sixth, plus one third, minus one sixth.')
    ox,oy,sx,sy=80,350,100,90
    f.axes(p,ox,oy,sx,sy,4,3,'t','y')
    def xy(t,y):return ox+sx*t,oy-sy*y
    x1,y1=xy(0,2/3);x2,y2=xy(4,2/3+2)
    f.path(p,f'M{x1} {y1} L{x2} {y2}',f.BLUE,3)
    for t,y in [(1,1),(2,2),(3,2)]:
        fit=2/3+t/2;xp,yp=xy(t,y);xf,yf=xy(t,fit)
        f.path(p,f'M{xf} {yf} L{xp} {yp}',f.DEEP_PINK,4)
        p.append(f'<circle cx="{xf}" cy="{yf}" r="4" fill="white" stroke="{f.BLUE}" stroke-width="2"/>')
        f.point(p,xp,yp)
    f.text(p,120,290,'−1/6','small');f.text(p,235,150,'+1/3','small');f.text(p,390,213,'−1/6','small')
    f.text(p,555,123,'Best line: y = 2/3 + t/2')
    f.text(p,555,183,'e = (−1/6, 1/3, −1/6)','small')
    f.text(p,555,230,'Squared error: 1/6','small')
    f.text(p,555,291,'Column checks: Σeᵢ = 0, Σtᵢeᵢ = 0','small')
    f.text(p,25,416,'Plot: vertical response gaps. Response space: e is perpendicular to both model columns.','small')
    f.write('least-squares-line.svg',p)

def gram_schmidt():
    p=begin(1000,430,'Subtract the old component before normalizing',
            'In equally scaled x,y axes, a1=(1,0), a2=(1,2). Subtracting projection (1,0) from a2 leaves u2=(0,2). The orthonormal directions are (1,0),(0,1).')
    ox,oy,s=75,320,90;f.axes(p,ox,oy,s,s,3,2,'x','y')
    def xy(x,y):return ox+s*x,oy-s*y
    arrow(p,xy(0,0),xy(1,2),'pink');arrow(p,xy(0,0),xy(1,0))
    arrow(p,xy(1,0),xy(1,2));f.path(p,f'M{ox} {oy} V{oy-2*s}',f.DEEP_GREEN,2,extra='stroke-dasharray="6 4"')
    f.text(p,175,120,'a₂ = (1, 2)','small');f.text(p,177,242,'remainder (0, 2)','small')
    f.text(p,460,120,'1. First direction: a₁ = (1, 0)')
    f.text(p,460,177,'2. Remove projection: (1, 2) − (1, 0)','small')
    f.text(p,460,228,'3. Remainder: u₂ = (0, 2)')
    f.text(p,460,285,'4. Normalize: q₂ = (0, 1)')
    f.text(p,25,389,'The translated vertical arrow and the dashed arrow represent the same remainder vector.','small')
    f.write('gram-schmidt.svg',p)

def four_spaces():
    p=begin(1080,530,'Four spaces: pair complements within each ambient space',
            'Input Rn splits into row space C(A transpose), dimension r, and null space N(A), dimension n minus r. Output Rm splits into column space C(A), dimension r, and left null space N(A transpose), dimension m minus r. A maps the row space bijectively to the column space and the null space to zero.')
    for x,ambient,top,bottom in [
        (30,'Input space: ℝⁿ',('Row space C(Aᵀ)','Dimension r'),('Null space N(A)','Dimension n − r')),
        (710,'Output space: ℝᵐ',('Column space C(A)','Dimension r'),('Left null space N(Aᵀ)','Dimension m − r'))]:
        f.text(p,x+8,92,ambient)
        for y,labels,fill in [(115,top,'#FFF0F6'),(335,bottom,'#EFF9E7')]:
            p.append(f'<rect x="{x}" y="{y}" width="335" height="125" rx="12" fill="{fill}" stroke="{f.BLUE}"/>')
            f.text(p,x+16,y+42,labels[0]);f.text(p,x+16,y+84,labels[1],'small')
        f.path(p,f'M{x+167} 245 V330',f.BLUE,2)
        f.text(p,x+184,282,'⊥','title');f.text(p,x+184,311,'complements','small')
    f.path(p,'M380 175 H690',f.BLUE,3,extra='marker-end="url(#arrow)"')
    f.text(p,410,140,'A: one-to-one and onto','small')
    f.text(p,435,213,'A x_row = b','small')
    f.path(p,'M380 390 L654 285',f.BLUE,3,extra='marker-end="url(#arrow)"')
    f.text(p,410,305,'A x_null = 0','small');f.text(p,671,291,'0','title')
    f.text(p,385,440,'Zero belongs to both output subspaces.','small')
    f.text(p,30,501,'Schematic for A of size m × n and rank r. Pair perpendicular spaces on the same side.','small')
    f.write('four-space-complements.svg',p)

def subspace():
    p=begin(1000,500,'Subspace projection: the error is normal to every allowed direction',
            'A schematic plane S is the column space of A. The fitted vector p=A x-hat lies in S. The vector b ends above S; residual e=b minus p goes from p to b and is perpendicular to every column of A. Thus A transpose times e is zero.')
    p.append(f'<path d="M60 350 L370 270 L485 360 L165 445 Z" fill="#EFF9E7" stroke="{f.DEEP_GREEN}" stroke-width="2"/>')
    origin=(140,390);fit=(270,355);observed=(270,135)
    arrow(p,origin,observed,'pink');arrow(p,origin,fit)
    f.path(p,'M270 355 V135',f.BLUE,3,extra='stroke-dasharray="6 4" marker-end="url(#arrow)"')
    f.text(p,286,144,'b','label');f.text(p,288,245,'e = b − p','small')
    f.text(p,290,382,'p = A x̂','small');f.text(p,80,321,'S = C(A)','small')
    f.text(p,545,135,'1. Choose p inside the allowed span.')
    f.text(p,545,205,'2. Require e ⟂ every column of A.','small')
    f.text(p,545,275,'3. Solve AᵀA x̂ = Aᵀb.')
    f.text(p,545,345,'4. Check Aᵀe = 0.','label')
    f.text(p,30,477,'Schematic: the closest output lies in the subspace; the leftover error lies in its orthogonal complement.','small')
    f.write('subspace-projection.svg',p)

if __name__=='__main__':
    line();measurement();least_squares();gram_schmidt()
    four_spaces();subspace()
    print('Generated six original Lecture 4 SVGs.')
