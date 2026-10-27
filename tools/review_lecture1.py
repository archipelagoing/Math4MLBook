"""Review the four-page lecture route. Requires Playwright and Chromium.
Screenshots are saved under /tmp. No publication is performed.
"""
import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parents[1] / 'book/_build/html'
PAGES = ['intro.html', 'lecture1/index.html', 'lecture1/matrix-guide.html',
         'lecture1/practice.html', 'lecture1/solutions.html']

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 1050})
        errors, reports, examples = [], [], []
        page.on('pageerror', lambda e: errors.append(str(e)))
        for width in (1440, 390):
            await page.set_viewport_size({'width': width, 'height': 1050})
            for relative in PAGES:
                await page.goto((ROOT / relative).as_uri())
                await page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
                await page.evaluate('MathJax.startup.promise')
                report = {'page': relative, 'width': width,
                          'mathErrors': await page.locator('mjx-merror').count(),
                          'overflow': await page.evaluate('document.documentElement.scrollWidth > innerWidth')}
                reports.append(report)
                assert not report['mathErrors'] and not report['overflow'], report
                import re
                assert not re.search(r'\b(knitting|crochet|stitch|stitches|swatch|sampler|fabric|yarn)\b', await page.locator('article').inner_text(), re.I)
                if relative != 'intro.html':
                    assert await page.locator('.lecture-path a').count() == 4
                    assert await page.locator('.lecture-path a[aria-current="page"]').count() == 1
                if relative in ('lecture1/index.html', 'lecture1/matrix-guide.html'):
                    assert await page.locator('.section-intro').count() == 6
                    assert await page.locator('.section-recap').count() == 6
                    assert await page.locator('.checkpoint').count() == 6
                    if width == 1440:
                        examples += await page.locator('.example > .admonition-title').all_text_contents()
                        for figure in await page.locator('article figure').all():
                            identifier = await figure.get_attribute('id')
                            await figure.screenshot(path=f'/tmp/math4ml-shadow-{identifier}.png')
                if relative == 'lecture1/index.html':
                    await page.screenshot(path=f'/tmp/math4ml-restored-{width}.png')
                    nav = await page.locator('.bd-sidenav > .toctree-l1.current a').all_text_contents()
                    assert len(nav) == 4, nav  # Current chapter remains four pages.
                    if width == 1440:
                        await page.locator('#fig-w1-shadows').screenshot(path='/tmp/math4ml-shadow-views-preview.png')
                        checkpoint = page.locator('.bd-article details summary').first
                        await checkpoint.focus()
                        await page.keyboard.press('Enter')
                        assert await page.locator('.bd-article details').first.get_attribute('open') is not None
                        await page.locator('.example').filter(has_text='Worked example 1.2').first.screenshot(path='/tmp/math4ml-structured-example.png')
                        await page.locator('.page-roadmap').screenshot(path='/tmp/math4ml-structured-roadmap.png')
                        await page.locator('.page-roadmap a[href="#w1-vector-arithmetic"]').click()
                        assert page.url.endswith('#w1-vector-arithmetic')
                        await page.wait_for_function("Math.abs(document.getElementById('w1-vector-arithmetic').getBoundingClientRect().top) < 250")
                        await page.wait_for_timeout(600)
                        await page.screenshot(path='/tmp/math4ml-structured-section.png')
                        await page.locator('.page-roadmap a[href="#w1-angles"]').click()
                        await page.wait_for_function("Math.abs(document.getElementById('w1-angles').getBoundingClientRect().top) < 250")
                        await page.wait_for_timeout(600)
                        await page.screenshot(path='/tmp/math4ml-structured-angles.png')
            # A solution must return to an included concept, not a removed tab.
            await page.locator('a[href="index.html#w1-vectors"]').first.click()
            assert page.url.endswith('index.html#w1-vectors'), page.url
        await page.evaluate("document.documentElement.dataset.theme='dark'")
        await page.screenshot(path='/tmp/math4ml-restored-dark.png')
        await page.emulate_media(media='print')
        await page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
        assert await page.locator('.bd-article details:not([open])').count() == 0
        assert not errors, errors
        import re
        assert [int(re.search(r'1\.(\d+)', title).group(1)) for title in examples] == list(range(1, 13)), examples
        print(json.dumps({'pages': reports, 'javascriptErrors': errors,
                          'lecturePages': 4, 'numberedSections': 12, 'workedExamples': 12, 'checkpoints': 12, 'keyboardCheckpoint': True,
                          'solutionReturnLink': True, 'printAnswersOpen': True}, indent=2))
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
