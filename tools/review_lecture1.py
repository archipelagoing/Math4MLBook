"""Optional Playwright review; writes screenshots/PDF under /tmp.
Install playwright and its Chromium browser separately before running.
"""
import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]/'book/_build/html'
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch()
  page=await browser.new_page(viewport={"width":1440,"height":1100},device_scale_factor=1)
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  reports=[]
  for width in (1440,390):
   await page.set_viewport_size({'width':width,'height':1100})
   for path in [ROOT/'intro.html',*sorted((ROOT/'lecture1').glob('*.html'))]:
    await page.goto(path.as_uri());await page.wait_for_function('window.MathJax && MathJax.startup && MathJax.startup.promise')
    await page.evaluate('MathJax.startup.promise');await page.wait_for_timeout(100)
    reports.append({'page':path.stem,'width':width,'math':await page.locator('mjx-container').count(),'mathErrors':await page.locator('mjx-merror').count(),'overflow':await page.evaluate('document.documentElement.scrollWidth>innerWidth')})
    if path.stem=='index':
     await page.screenshot(path=f'/tmp/math4ml-lecture1-{width}.png',full_page=True)
    if path.stem=='geometry' and width==1440:
     await page.locator('#fig-w1-repeat-geometry').screenshot(path='/tmp/math4ml-geometry-figure.png')
    if path.stem=='products' and width==1440:
     await page.screenshot(path='/tmp/math4ml-products.png',full_page=True)
   
  await page.set_viewport_size({'width':1440,'height':1100})
  await page.goto((ROOT/'lecture1/vectors.html').as_uri());await page.evaluate('MathJax.startup.promise')
  summary=page.locator('.bd-article details summary').first
  await summary.focus();await page.keyboard.press('Enter')
  keyboard=await page.locator('.bd-article details').first.get_attribute('open') is not None
  await page.evaluate("document.documentElement.dataset.theme='dark'")
  await page.screenshot(path='/tmp/math4ml-dark.png',full_page=True)
  await page.evaluate("document.documentElement.dataset.theme='light';document.querySelectorAll('details').forEach(e=>e.open=false)")
  await page.pdf(path='/tmp/math4ml-lecture1-vectors-print.pdf',format='A4',print_background=True,margin={'top':'15mm','bottom':'15mm','left':'15mm','right':'15mm'})
  await page.emulate_media(media='print');await page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
  print_open=await page.locator('.bd-article details[open]').count()==await page.locator('.bd-article details').count()
  await page.screenshot(path='/tmp/math4ml-print.png',full_page=True)
  print(json.dumps({'pages':reports,'javascriptErrors':errors,'keyboardDropdown':keyboard,'printAnswersOpen':print_open},indent=2))
  await browser.close()
asyncio.run(main())
