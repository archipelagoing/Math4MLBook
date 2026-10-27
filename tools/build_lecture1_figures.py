"""Regenerate the shadow chapter's four original SVGs and its book mark."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'book/figures/lecture1'
INK, BLUE = '#543124', '#3975DB'
PAPER, PINK, GREEN = '#FFF9F5', '#FF4FA3', '#8DEB42'
DEEP_PINK, DEEP_GREEN = '#C91E70', '#357D22'


def start(width, height, title, desc):
    return [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<rect width="{width}" height="{height}" rx="16" fill="{PAPER}"/>
<style>text{{font-family:Georgia,serif;fill:{INK}}}.title{{font-size:27px;font-weight:bold}}.label{{font-size:21px}}.small{{font-size:18px}}</style>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="{BLUE}"/></marker></defs>''']


def text(parts, x, y, value, cls='label', extra=''):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" {extra}>{escape(value)}</text>')


def path(parts, d, color=BLUE, width=2, extra=''):
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>')


def point(parts,x,y,second=False):
    if second:
        parts.append(f'<path d="M{x} {y-8} L{x+8} {y} L{x} {y+8} L{x-8} {y} Z" fill="{GREEN}" stroke="{DEEP_GREEN}" stroke-width="2"/>')
    else:
        parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{PINK}" stroke="{DEEP_PINK}" stroke-width="2"/>')


def write(name,parts):
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/name).write_text('\n'.join(parts+['</svg>'])+'\n')


def axes(parts,ox,oy,sx,sy,xmax,ymax,xlabel,ylabel):
    for x in range(xmax+1):
        xx=ox+x*sx
        path(parts,f'M{xx} {oy-ymax*sy} V{oy}', '#E3D8D0',1)
        text(parts,xx,oy+23,str(x),'small','text-anchor="middle"')
    for y in range(1,ymax+1):
        yy=oy-y*sy
        path(parts,f'M{ox} {yy} H{ox+xmax*sx}', '#E3D8D0',1)
        if ymax<=5 or y in (4,9):text(parts,ox-12,yy+5,str(y),'small','text-anchor="end"')
    path(parts,f'M{ox} {oy} H{ox+xmax*sx+15}',extra='marker-end="url(#arrow)"')
    path(parts,f'M{ox} {oy} V{oy-ymax*sy-14}',extra='marker-end="url(#arrow)"')
    text(parts,ox+xmax*sx+22,oy+5,xlabel,'small')
    text(parts,ox-5,oy-ymax*sy-23,ylabel,'small')


def views():
    p=start(1120,440,'One front mark can hide two different depths',
            'Two candidate point positions p=(2,3,4) and p-prime=(2,3,9) have the same front mark (2,3). A side view records (3,4) and (3,9). Axes are calibrated X,Y and Y,Z; positions are alternatives, not simultaneous unidentified points.')
    text(p,25,38,'One front mark can hide two different depths','title')
    text(p,30,88,'World: X = 2, Y = 3')
    path(p,'M45 283 H305',extra='marker-end="url(#arrow)"')
    for z in [0,4,9]:
        xx=55+z*24;path(p,f'M{xx} 277 V289',INK,1)
        text(p,xx,310,str(z),'small','text-anchor="middle"')
    point(p,151,283);point(p,271,283,True)
    text(p,100,238,'p: Z = 4','small');text(p,216,211,"p′: Z = 9",'small')
    text(p,300,315,'Z','small')
    text(p,30,350,'Move only in depth.', 'small')
    text(p,390,88,'Front screen: keep X,Y')
    axes(p,435,327,38,38,4,5,'X','Y')
    # A ring around one dot denotes coincident alternative front marks.
    p.append(f'<circle cx="511" cy="213" r="12" fill="none" stroke="{DEEP_GREEN}" stroke-width="3"/>')
    point(p,511,213);text(p,532,207,'(2, 3)','small')
    text(p,400,374,'Both positions share this mark.','small')
    text(p,768,88,'Side screen: keep Y,Z')
    axes(p,813,327,19,19,5,10,'Y','Z')
    point(p,870,251);point(p,870,156,True)
    text(p,888,256,'(3, 4)','small');text(p,888,161,'(3, 9)','small')
    text(p,773,374,'The depth change becomes visible.','small')
    text(p,26,416,'Ideal parallel-ray views of matched points. A view records selected coordinates, not a whole solid object.','small')
    write('shadow-views.svg',p)


def profiles():
    p=start(1120,490,'Four labeled marks → one ordered profile',
            'Left: front-screen marks of four beads A,B,C,D at fixed Y=1,2,3,4. Pink circles are profile r=(3,1,3,1), green diamonds are s=(1,3,1,3). Right: coefficient coordinates r=2e+a, s=2e-a, and the uniform profile 2e. These are distinct physical and record coordinate plots.')
    text(p,25,38,'Four labeled marks → one ordered profile','title')
    text(p,65,82,'Front marks: X varies, Y labels the bead','small')
    axes(p,100,362,65,55,4,4,'X','Y')
    for i,(r,s,label) in enumerate(zip([3,1,3,1],[1,3,1,3],'ABCD'),1):
        y=362-i*55
        point(p,100+r*65,y);point(p,100+s*65,y,True)
        text(p,43,y+5,label,'small')
    point(p,95,411);text(p,112,417,'r = (3, 1, 3, 1)','small')
    point(p,330,411,True);text(p,347,417,'s = (1, 3, 1, 3)','small')
    text(p,640,82,'Coefficients of the profile family','small')
    ox,oy,scale=675,257,65
    for i in range(5):
        path(p,f'M{ox+i*scale} 128 V387','#E3D8D0',1)
        text(p,ox+i*scale,oy+24,str(i),'small','text-anchor="middle"')
    for j in [-2,-1,1,2]:
        yy=oy-j*scale;path(p,f'M630 {yy} H970','#E3D8D0',1)
    path(p,f'M630 {oy} H990',extra='marker-end="url(#arrow)"')
    path(p,f'M{ox} 390 V110',extra='marker-end="url(#arrow)"')
    text(p,1003,263,'α');text(p,683,109,'β')
    for x,y,color,label in [(805,192,DEEP_PINK,'r = 2e + a'),(805,322,DEEP_GREEN,'s = 2e − a')]:
        path(p,f'M{ox} {oy} L{x} {y}',color,3)
        p.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{color}"/>')
        text(p,x+15,y-8,label,'small')
    p.append(f'<circle cx="805" cy="257" r="6" fill="{BLUE}"/>')
    text(p,823,250,'2e: all X = 2','small')
    text(p,638,417,'e = (1,1,1,1);  a = (1,−1,1,−1)','small')
    text(p,25,465,'Left: positions on a screen. Right: coefficients that select a four-entry measurement record.','small')
    write('shadow-profiles.svg',p)


def geometry():
    p=start(860,530,'Geometry of four-point measurement records',
            'In equal-scale orthonormal profile coordinates q0=e/2 and q1=a/2, r=(4,2) and s=(4,-2). The drawn coordinates preserve record-space angles and lengths. This angle is not a physical orientation of the point frame.')
    text(p,25,38,'Geometry of four-point measurement records','title')
    ox,oy,scale=98,284,65
    for i in range(7):
        x=ox+i*scale;path(p,f'M{x} 90 V440','#E3D8D0',1)
        text(p,x,oy+28,str(i),'small','text-anchor="middle"')
    for j in [-2,-1,1,2]:
        y=oy-j*scale;path(p,f'M60 {y} H650','#E3D8D0',1)
    path(p,f'M60 {oy} H690',width=2.5,extra='marker-end="url(#arrow)"')
    path(p,f'M{ox} 450 V76',width=2.5,extra='marker-end="url(#arrow)"')
    for y,col,label in [(154,DEEP_PINK,'r'),(414,DEEP_GREEN,'s')]:
        path(p,f'M{ox} {oy} L358 {y}',col,3.5)
        p.append(f'<circle cx="358" cy="{y}" r="6" fill="{col}"/>');text(p,376,y+5,label)
    path(p,'M358 154 V414',width=1.5,extra='stroke-dasharray="5 4"')
    text(p,710,oy+6,'q₀');text(p,ox+12,81,'q₁')
    text(p,440,114,'r = (4, 2) in q-coordinates');text(p,440,147,'s = (4, −2) in q-coordinates')
    text(p,440,185,'q₀ = e/2, q₁ = a/2','small')
    text(p,25,490,'Squared record length: 4² + 2² = 20. This is not a physical frame rotation.','small')
    write('shadow-geometry.svg',p)


def view_map():
    p=start(1060,365,'A view matrix tells you what each coordinate changes',
            'The point p=(2,3,4) has three input coordinates. O keeps X and Y; its column effects are (1,0),(0,1),(0,0). The output is the front mark (2,3). A Z change is invisible to this view.')
    text(p,25,38,'A view matrix tells you what each coordinate changes','title')
    for x,w,title,rows in [(25,235,'World point p',['X = 2','Y = 3','Z = 4']),
                           (335,360,'Front view O: keep X,Y',['X column: (1, 0)','Y column: (0, 1)','Z column: (0, 0)']),
                           (770,260,'Screen mark Op',['horizontal X = 2','vertical Y = 3'])]:
        fill='#FFF0F6' if x==25 else '#EFF9E7'
        p.append(f'<rect x="{x}" y="84" width="{w}" height="170" rx="12" fill="{fill}" stroke="{BLUE}" stroke-width="1.4"/>')
        text(p,x+14,114,title,'small')
        for i,value in enumerate(rows):text(p,x+16,153+i*35,value)
    for a,b in [(270,321),(705,756)]:path(p,f'M{a} 169 H{b}',width=2.5,extra='marker-end="url(#arrow)"')
    text(p,27,300,'Op = 2(1, 0) + 3(0, 1) + 4(0, 0) = (2, 3)')
    text(p,27,338,'Three input coordinates → two readings. The zero third column makes depth invisible.','small')
    write('shadow-map.svg',p)


def mark():
    (ROOT/'book/figures/shadow-mark.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="A point and its two calibrated views"><rect width="100" height="100" rx="22" fill="{PAPER}"/><path d="M12 75 V20 M12 75 H65 M43 87 V35 M43 87 H90" fill="none" stroke="{BLUE}" stroke-width="4" stroke-linecap="round"/><path d="M35 45 L68 61" fill="none" stroke="{INK}" stroke-dasharray="4 3" stroke-width="2"/><circle cx="35" cy="45" r="10" fill="{PINK}" stroke="{DEEP_PINK}" stroke-width="2"/><circle cx="68" cy="61" r="10" fill="{GREEN}" stroke="{DEEP_GREEN}" stroke-width="2"/></svg>\n''')


if __name__=='__main__':
    views(); profiles(); geometry(); view_map(); mark()
    print('Generated four shadow/point SVGs and the book mark.')
