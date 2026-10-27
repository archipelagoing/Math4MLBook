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
        errors, reports = [], []
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
                if relative == 'lecture1/index.html':
                    await page.screenshot(path=f'/tmp/math4ml-restored-{width}.png')
                    nav = await page.locator('.bd-sidenav a').all_text_contents()
                    assert len(nav) == 5, nav  # Home plus four lecture pages.
                    if width == 1440:
                        await page.locator('#fig-w1-sampler').screenshot(path='/tmp/math4ml-restored-sampler.png')
                        checkpoint = page.locator('.bd-article details summary').first
                        await checkpoint.focus()
                        await page.keyboard.press('Enter')
                        assert await page.locator('.bd-article details').first.get_attribute('open') is not None
                        await page.locator('.bd-article .example').first.screenshot(path='/tmp/math4ml-restored-example.png')
            # A solution must return to an included concept, not a removed tab.
            await page.locator('a[href="index.html#w1-vectors"]').first.click()
            assert page.url.endswith('index.html#w1-vectors'), page.url
        await page.evaluate("document.documentElement.dataset.theme='dark'")
        await page.screenshot(path='/tmp/math4ml-restored-dark.png')
        await page.emulate_media(media='print')
        await page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
        assert await page.locator('.bd-article details:not([open])').count() == 0
        assert not errors, errors
        print(json.dumps({'pages': reports, 'javascriptErrors': errors,
                          'lecturePages': 4, 'keyboardCheckpoint': True,
                          'solutionReturnLink': True, 'printAnswersOpen': True}, indent=2))
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
