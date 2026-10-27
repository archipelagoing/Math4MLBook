"""Regenerate original Lecture 1 SVG schematics using only the standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'book/figures/lecture1'
INK, BLUE, PINK, GREEN = '#543124', '#3975DB', '#FF4FA3', '#8DEB42'
PAPER, DEEP_PINK, DEEP_GREEN = '#FFF9F5', '#C91E70', '#357D22'


def start(width, height, title, desc):
    return [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<rect width="{width}" height="{height}" rx="16" fill="{PAPER}"/>
<style>text{{font-family:Georgia,serif;fill:{INK}}}.title{{font-size:27px;font-weight:bold}}.label{{font-size:21px}}.small{{font-size:18px}}.number{{font-size:25px;text-anchor:middle}}</style>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="{BLUE}"/></marker></defs>''']


def text(parts, x, y, value, cls='label', extra=''):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" {extra}>{escape(value)}</text>')


def write(name, parts):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text('\n'.join(parts + ['</svg>']) + '\n')


def sampler():
    W = [[3, 1, 3, 1], [1, 3, 1, 3], [3, 1, 3, 1], [1, 3, 1, 3]]
    p = start(1140, 350, 'One row of stitches, one ordered record', 'Four rows of 24 schematic stitch cells, grouped into four sections of six. Pink counts alternate 3,1,3,1 and 1,3,1,3. Every row totals eight pink and sixteen green. Matrix entries summarize sections, not individual stitches. Rows are shown in record order.')
    text(p, 28, 38, 'A 24-stitch sampler → four section counts per row', 'title')
    for j, label in enumerate('ABCD'):
        text(p, 49+j*132, 80, f'{label}: 6 stitches', 'small')
    for i, row in enumerate(W):
        y = 100+i*36
        text(p, 12, y+23, str(i+1), 'small')
        for j, count in enumerate(row):
            for k in range(6):
                x = 42+j*132+k*20
                color = PINK if k<count else GREEN
                p.append(f'<rect x="{x}" y="{y}" width="18" height="29" rx="4" fill="{color}" stroke="{INK}" stroke-width="0.7" data-stitch="true" data-pink="{str(k<count).lower()}"/>')
                p.append(f'<path d="M{x+4} {y+6} L{x+9} {y+22} L{x+14} {y+6}" fill="none" stroke="{INK}" stroke-width="1"/>')
        text(p, 585, y+22, '8 pink', 'small')
    text(p, 738, 78, 'Section-count matrix W')
    for i, row in enumerate(W):
        for j, value in enumerate(row):
            x, y = 740+j*65, 98+i*36
            p.append(f'<rect x="{x}" y="{y}" width="54" height="30" rx="5" fill="#FFF0F6" stroke="{BLUE}" stroke-width="0.8"/>')
            text(p, x+27, y+23, str(value), 'number')
    text(p, 30, 284, 'A matrix entry counts pink stitches in a six-stitch section; the rest are green.')
    text(p, 30, 320, 'Schematic symbols, not loop-accurate technique instructions. Row numbers define the record order.', 'small')
    write('sampler.svg', p)


def plane(name, normalized=False):
    title = 'Uniform and alternating record directions' if normalized else 'Coefficients of a repeat family'
    p = start(860, 530, title, 'A two-axis plot of repeat coordinates. The same row r is alpha=2 beta=1 in the unnormalized e,a basis, or 4,2 in the normalized q0,q1 basis. The axes are mathematical record directions, not fabric dimensions.')
    text(p, 25, 38, title, 'title')
    ox, oy = 98, 284
    scale = 115 if not normalized else 65
    maximum = 3 if not normalized else 6
    for i in range(maximum+1):
        x=ox+i*scale
        p.append(f'<path d="M{x} 90 V440" stroke="#E3D8D0" stroke-width="1"/>')
        text(p,x,oy+28,str(i),'small','text-anchor="middle"')
    for j in [-2,-1,1,2]:
        y=oy-j*(75 if not normalized else 65)
        p.append(f'<path d="M60 {y} H650" stroke="#E3D8D0" stroke-width="1"/>')
    p.append(f'<path d="M60 {oy} H690" stroke="{BLUE}" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
    p.append(f'<path d="M{ox} 450 V76" stroke="{BLUE}" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
    xx = ox+(2 if not normalized else 4)*scale
    yy = oy-(75 if not normalized else 130)
    down = oy+(75 if not normalized else 130)
    for y,col,label in [(yy,DEEP_PINK,'r'),(down,DEEP_GREEN,'s')]:
        p.append(f'<path d="M{ox} {oy} L{xx} {y}" stroke="{col}" stroke-width="3.5"/>')
        p.append(f'<circle cx="{xx}" cy="{y}" r="6" fill="{col}"/>')
        text(p,xx+18,y+5,label)
    p.append(f'<path d="M{xx} {yy} V{down}" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    text(p,710,oy+6,'q₀' if normalized else 'α')
    text(p,ox+12,81,'q₁' if normalized else 'β')
    if normalized:
        text(p,440,114,'r = (4, 2) in q-coordinates')
        text(p,440,147,'s = (4, −2) in q-coordinates')
        text(p,440,185,'q₀ = e/2,  q₁ = a/2', 'small')
        text(p,25,490,'Squared length of r: 4² + 2² = 20. This is record-space geometry.', 'small')
    else:
        p.append(f'<circle cx="{xx}" cy="{oy}" r="6" fill="{BLUE}"/>')
        text(p,xx+18,oy-10,'2e')
        text(p,440,113,'r = 2e + a')
        text(p,440,140,'(3, 1, 3, 1)', 'small')
        text(p,440,178,'s = 2e − a')
        text(p,440,205,'(1, 3, 1, 3)', 'small')
        text(p,440,243,'Uniform: 2e', 'small')
        text(p,440,270,'(2, 2, 2, 2)', 'small')
        text(p,25,490,'Each point selects a four-entry record; the plot does not measure the fabric.', 'small')
    write(name,p)


def operation_map():
    p=start(1030,350,'A product with named input and output spaces','Eighteen plain operations and six increases combine column effects. Plain consumes one and produces one; increase consumes one and produces two. The output is twenty-four consumed and thirty produced.')
    text(p,26,38,'Columns are effects; the input supplies their coefficients.','title')
    boxes=[(28,88,235,'Operation counts',['18 plain','6 increases']), (338,88,300,'B = consumed / produced',['plain column: (1, 1)','increase column: (1, 2)']), (725,88,275,'Combined record',['24 consumed','30 produced'])]
    for x,y,w,label,items in boxes:
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="150" rx="13" fill="{ "#FFF0F6" if x<300 else "#EFF9E7"}" stroke="{BLUE}" stroke-width="1.3"/>')
        text(p,x+14,y+30,label,'small')
        for i,item in enumerate(items): text(p,x+15,y+75+i*37,item)
    for a,b in [(270,327),(646,714)]:
        p.append(f'<path d="M{a} 166 H{b}" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#arrow)"/>')
    text(p,27,286,'18(1, 1) + 6(1, 2) = (24, 30)')
    text(p,27,322,'The result counts stitches; it does not specify operation placement or the full fabric.','small')
    write('operation-map.svg',p)


def mark():
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Two colored yarn loops and blue needles"><rect width="100" height="100" rx="22" fill="{PAPER}"/><path d="M22 78 L76 20 M24 21 L78 77" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/><ellipse cx="37" cy="48" rx="15" ry="21" fill="none" stroke="{PINK}" stroke-width="8" transform="rotate(-20 37 48)"/><ellipse cx="63" cy="48" rx="15" ry="21" fill="none" stroke="{GREEN}" stroke-width="8" transform="rotate(20 63 48)"/></svg>'''
    (ROOT/'book/figures/yarn-mark.svg').write_text(svg+'\n')


if __name__=='__main__':
    sampler(); plane('repeat-family.svg'); plane('repeat-geometry.svg',True); operation_map(); mark()
    print('Generated four original Lecture 1 SVGs and the book mark.')
