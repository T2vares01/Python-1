from playwright.sync_api import sync_playwright

with sync_playwright() as pc:
    nav = pc.chromium.launch(headless= False)
    pg = nav.new_page()
    pg.goto("https://www.youtube.com/watch?v=1NNMzL4W8ws&t=669s")
