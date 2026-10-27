"""Optional Playwright checks for the concise lecture; previews go to /tmp.
Install Playwright and its Chromium browser separately before running.
"""
import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parents[1] / 'book/_build/html'
PAGES = ['intro.html', 'lecture1/index.html', 'lecture1/matrix-guide.html']

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 1000})
        errors, reports = [], []
        page.on('pageerror', lambda e: errors.append(str(e)))
        for width in (1440, 390):
            await page.set_viewport_size({'width': width, 'height': 1000})
            for relative in PAGES:
                await page.goto((ROOT / relative).as_uri())
                await page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
                await page.evaluate('MathJax.startup.promise')
                report = {
                    'page': relative, 'width': width,
                    'mathErrors': await page.locator('mjx-merror').count(),
                    'overflow': await page.evaluate('document.documentElement.scrollWidth > innerWidth'),
                }
                reports.append(report)
                assert not report['mathErrors'] and not report['overflow'], report
                if relative != 'intro.html':
                    name = Path(relative).stem
                    await page.screenshot(path=f'/tmp/math4ml-brief-{name}-{width}.png', full_page=True)
                    if width == 1440:
                        await page.pdf(path=f'/tmp/math4ml-brief-{name}.pdf', format='A4', print_background=True,
                                       margin={'top':'12mm', 'bottom':'12mm', 'left':'12mm', 'right':'12mm'})
        await page.evaluate("document.documentElement.dataset.theme='dark'")
        await page.screenshot(path='/tmp/math4ml-brief-dark.png', full_page=True)
        assert not errors, errors
        print(json.dumps({'pages': reports, 'javascriptErrors': errors}, indent=2))
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
