from playwright.sync_api import sync_playwright
import time
import os

def run():
    os.makedirs('/home/jules/verification', exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto('http://localhost:8085')
        page.wait_for_timeout(1000)

        # Take English desktop screenshot
        page.screenshot(path='/home/jules/verification/english_desktop.png', full_page=True)

        # Switch to Gujarati and screenshot
        page.click('#btn-lang-gu')
        page.wait_for_timeout(500)
        page.screenshot(path='/home/jules/verification/gujarati_desktop.png', full_page=True)

        # Switch to Hindi and screenshot
        page.click('#btn-lang-hi')
        page.wait_for_timeout(500)
        page.screenshot(path='/home/jules/verification/hindi_desktop.png', full_page=True)

        # Mobile viewport screenshot
        page_mobile = browser.new_page(viewport={"width": 375, "height": 812})
        page_mobile.goto('http://localhost:8085')
        page_mobile.wait_for_timeout(1000)
        page_mobile.screenshot(path='/home/jules/verification/english_mobile.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    run()
