"""Browser review of Lecture 2; writes screenshots/evidence under /tmp."""
import asyncio
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]/'book/_build/html'
PAGES=['intro.html','lecture2/index.html','lecture2/elimination.html','lecture2/practice.html','lecture2/solutions.html']

async def main():
    errors=[];reports=[];link_count=0
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        page=await browser.new_page(viewport={'width':1440,'height':1050})
        page.on('pageerror',lambda e:errors.append(str(e)))
        for width in [1440,390]:
            await page.set_viewport_size({'width':width,'height':1050})
            for relative in PAGES:
                await page.goto((ROOT/relative).as_uri())
                await page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
                await page.evaluate('MathJax.startup.promise')
                r={'page':relative,'width':width,'mathErrors':await page.locator('mjx-merror').count(),
                   'overflow':await page.evaluate('document.documentElement.scrollWidth > innerWidth')}
                assert not r['mathErrors'] and not r['overflow'],r
                reports.append(r)
                if relative!='intro.html':
                    assert await page.locator('.lecture-path a').count()==4
                    assert await page.locator('.lecture-path [aria-current="page"]').count()==1
                if relative in ['lecture2/index.html','lecture2/elimination.html']:
                    for cls in ['section-intro','section-recap','checkpoint','example']:
                        assert await page.locator('.'+cls).count()==4,(relative,cls)
                    assert await page.locator('article figure img[alt]').count()>=1
                    if width==1440:
                        for figure in await page.locator('article figure').all():
                            await figure.screenshot(path='/tmp/math4ml-lecture2/'+await figure.get_attribute('id')+'.png')
                        await page.locator('.example').first.screenshot(path='/tmp/math4ml-lecture2/'+Path(relative).stem+'-example.png')
                    await page.screenshot(path=f'/tmp/math4ml-lecture2/{Path(relative).stem}-{width}.png')
                    summary=page.locator('.bd-article details summary').first
                    await summary.focus();await page.keyboard.press('Enter')
                    assert await page.locator('.bd-article details').first.get_attribute('open') is not None
                    anchor='w2-products' if relative.endswith('index.html') else 'w2-gaussian'
                    await page.locator(f'.page-roadmap a[href="#{anchor}"]').click()
                    await page.wait_for_function(f"Math.abs(document.getElementById('{anchor}').getBoundingClientRect().top)<250")
                    await page.wait_for_timeout(650)
                    await page.screenshot(path=f'/tmp/math4ml-lecture2/{Path(relative).stem}-section-{width}.png')
                # Resolve every local article link/asset, including fragment IDs.
                if width==1440:
                    for url in await page.locator('article [href], article [src]').evaluate_all("els=>els.map(e=>e.getAttribute('href') || e.getAttribute('src'))"):
                        parts=urlsplit(url)
                        if parts.scheme or parts.netloc:continue
                        target=(ROOT/relative).parent/unquote(parts.path) if parts.path else ROOT/relative
                        assert target.exists(),(relative,url)
                        if parts.fragment and target.suffix=='.html':
                            html=target.read_text()
                            assert f'id="{unquote(parts.fragment)}"' in html,(relative,url)
                        link_count+=1
            await page.locator('a[href="index.html#w2-products"]').first.click()
            assert page.url.endswith('index.html#w2-products')
        await page.goto((ROOT/'lecture2/elimination.html').as_uri())
        await page.evaluate('MathJax.startup.promise')
        await page.evaluate("document.documentElement.dataset.theme='dark'")
        await page.screenshot(path='/tmp/math4ml-lecture2/dark.png')
        await page.emulate_media(media='print')
        await page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
        assert await page.locator('.bd-article details:not([open])').count()==0
        await page.pdf(path='/tmp/math4ml-lecture2/elimination-print.pdf',format='A4',print_background=True)
        assert not errors,errors
        result={'pages':reports,'localArticleLinksAndAssets':link_count,'javascriptErrors':errors,
                'keyboardCheckpoint':True,'sectionJumps':True,'solutionReturnLink':True,'printAnswersOpen':True}
        Path('/tmp/math4ml-lecture2/browser-review.json').write_text(json.dumps(result,indent=2))
        print(json.dumps(result,indent=2))
        await browser.close()

if __name__=='__main__':asyncio.run(main())
