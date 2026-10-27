"""Review the actual numbered sidebar, topic pages, and integrated practice."""
import asyncio
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]/'book/_build/html'
ROUTES={
 1:[('index','Vectors & combinations'),('geometry','Dot products & geometry'),('matrix-guide','Matrices & products'),('cheatsheet','TL;DR cheat sheet')],
 2:[('index','Systems & elimination'),('elimination','Determinants & geometry'),('inverses','Inverses & invertibility'),('cheatsheet','TL;DR cheat sheet')],
 3:[('index','Spaces & subspaces'),('solutions-rank','Complete solutions & rank'),('basis','Independence, span & basis'),('cheatsheet','TL;DR cheat sheet')],
}
GROUPS={1:[[1,2,3,9,10],[4,5,11,12,18,21],[6,7,8,13,14,15,16,17,19,20,22,23,24],[]],
        2:[list(range(1,19)),list(range(19,22)),list(range(22,27)),[]],
        3:[list(range(1,9)),list(range(9,17)),list(range(17,29)),[]]}
PARTS={1:[3,3,6,0],2:[4,4,6,0],3:[5,2,4,0]}
EXAMPLES={1:12,2:17,3:16}

async def review(lecture):
    evidence=Path(f'/tmp/math4ml-navigation/lecture{lecture}');evidence.mkdir(parents=True,exist_ok=True)
    pages=['intro.html']+[f'lecture{lecture}/{file}.html' for file,_ in ROUTES[lecture]]
    expected_sidebar=['Mathematics, in view']+[f'Page {i} · {title}' for n in sorted(ROUTES) for i,(_,title) in enumerate(ROUTES[n],1)]
    reports=[];errors=[];links=0;examples=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch();page=await browser.new_page()
        page.on('pageerror',lambda e:errors.append(str(e)))
        for width in (1440,390):
            await page.set_viewport_size({'width':width,'height':1050})
            for relative in pages:
                await page.goto((ROOT/relative).as_uri())
                await page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
                await page.evaluate('MathJax.startup.promise')
                nav=[x.strip() for x in await page.locator('.bd-sidenav a').all_text_contents()]
                assert nav==expected_sidebar,(relative,nav)
                assert await page.locator('.bd-sidebar-primary .caption-text').count()==len(ROUTES)
                if relative!='intro.html':
                    index=pages.index(relative)-1;stem=ROUTES[lecture][index][0]
                    path=page.locator('.lecture-path a')
                    assert await path.evaluate_all("es=>es.map(e=>e.getAttribute('href'))")==[f+'.html' for f,_ in ROUTES[lecture]]
                    assert await page.locator('.lecture-path [aria-current="page"]').count()==1
                    assert await page.locator('.section-intro').count()==PARTS[lecture][index]
                    assert await page.locator('.checkpoint').count()==PARTS[lecture][index]
                    found=await page.locator(f'[id^="w{lecture}-p"]').evaluate_all(f"es=>es.map(e=>e.id).filter(id=>/^w{lecture}-p[0-9]+$/.test(id))")
                    assert sorted(found)==[f'w{lecture}-p{i:02}' for i in sorted(GROUPS[lecture][index])],(relative,found)
                    solutions=page.locator('details').filter(has=page.locator('summary').filter(has_text=re.compile(r'(?:Show explained solution|Explained solution) \d+')))
                    assert await solutions.count()==len(GROUPS[lecture][index]),relative
                    await page.screenshot(path=str(evidence/f'{stem}-{width}.png'))
                    if PARTS[lecture][index]:
                        summary=page.locator('.checkpoint + details summary').first
                        await summary.focus();await page.keyboard.press('Enter')
                        assert await page.locator('.checkpoint + details').first.get_attribute('open') is not None
                        await summary.press('Enter')
                        jump=page.locator('.page-roadmap a').last
                        href=await jump.get_attribute('href');await jump.click()
                        anchor=href[1:]
                        await page.wait_for_function(f"Math.abs(document.getElementById('{anchor}').getBoundingClientRect().top)<250")
                        await page.wait_for_timeout(650)
                    if await solutions.count():
                        await solutions.first.locator('summary').focus();await page.keyboard.press('Enter')
                        assert await solutions.first.get_attribute('open') is not None
                        if width==1440:await solutions.first.screenshot(path=str(evidence/f'{stem}-answer.png'))
                        # Also inspect the layout with every answer expanded.
                        await solutions.evaluate_all('es=>es.forEach(e=>e.open=true)')
                    if width==1440:
                        for example in await page.locator('.example').all():
                            title=await example.locator('.admonition-title').first.inner_text()
                            match=re.search(fr'{lecture}\.(\d+)',title)
                            if match:examples.append(int(match.group(1)))
                            if lecture in (2,3):
                                step_labels=await example.locator('.step-label').all_text_contents()
                                steps=[int(re.search(r'Step (\d+)',x).group(1)) for x in step_labels]
                                assert len(steps)>=2 and steps==list(range(1,len(steps)+1)),title
                report={'page':relative,'width':width,'mathErrors':await page.locator('mjx-merror').count(),
                        'overflow':await page.evaluate('document.documentElement.scrollWidth>innerWidth')}
                assert not report['mathErrors'] and not report['overflow'],report
                reports.append(report)
                if width==1440:
                    for url in await page.locator('article [href],article [src]').evaluate_all("es=>es.map(e=>e.getAttribute('href')||e.getAttribute('src'))"):
                        u=urlsplit(url)
                        if u.scheme or u.netloc:continue
                        target=(ROOT/relative).parent/unquote(u.path) if u.path else ROOT/relative
                        assert target.exists(),(relative,url)
                        if u.fragment and target.suffix=='.html':assert f'id="{unquote(u.fragment)}"' in target.read_text(),(relative,url)
                        links+=1
            # Print must expose answers on topic pages, not depend on another tab.
            await page.goto((ROOT/f'lecture{lecture}/index.html').as_uri())
            await page.evaluate('MathJax.startup.promise')
            await page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
            assert await page.locator('article details:not([open])').count()==0
        assert examples==list(range(1,EXAMPLES[lecture]+1)),examples
        await page.goto((ROOT/f'lecture{lecture}/cheatsheet.html').as_uri())
        await page.evaluate('MathJax.startup.promise')
        await page.evaluate("document.documentElement.dataset.theme='dark'")
        await page.screenshot(path=str(evidence/'cheatsheet-dark.png'))
        await page.emulate_media(media='print')
        await page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
        assert await page.locator('#jb-print-docs-body').evaluate("e=>getComputedStyle(e).display")=='none'
        await page.pdf(path=str(evidence/'cheatsheet-print.pdf'),format='A4',print_background=True)
        assert not errors,errors
        result={'pages':reports,'localArticleLinksAndAssets':links,'javascriptErrors':errors,
                'numberedSidebarPages':4,'practiceOnMatchingTopicPages':True,
                'preservedSolutions':sum(map(len,GROUPS[lecture])),'keyboardAnswersAndCheckpoints':True,'printAnswersOpen':True}
        (evidence/'review.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
        await browser.close()

if __name__=='__main__':
    import sys
    asyncio.run(review(int(sys.argv[1])))
