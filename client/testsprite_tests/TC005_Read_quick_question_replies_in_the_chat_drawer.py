import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:5174/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Reload the homepage (EduReach College) to try to load the SPA and reveal the floating 'EduReach Bot' chat button.
        await page.goto("http://localhost:5174/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Open the site in a new browser tab (http://localhost:5174/) to try loading the SPA and reveal the 'EduReach Bot' chat button.
        # Open URL in new tab
        page = await context.new_page()
        await page.goto("http://localhost:5174/")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Switch to the newly opened 'EduReach College' tab and wait for the SPA to render so the floating 'EduReach Bot' can be located.
        # Switch to tab 0950
        page = context.pages[-1]  # switch to most recently active tab
        
        # -> Click the floating 'EduReach Bot' chat button to open the chat drawer.
        # button
        elem = page.locator(".fixed")
        await elem.click(timeout=10000)
        
        # -> Click the floating 'EduReach Bot' circular chat button (bottom-right) to open the chat drawer.
        # button
        elem = page.locator(".fixed")
        await elem.click(timeout=10000)
        
        # -> Click the 'What courses do you offer?' quick question chip
        # What courses do you offer? button
        elem = page.get_by_role("button", name="What courses do you offer?")
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The chat drawer is open and shows the 'EduReach Bot' header.
        await page.locator("xpath=/html/body/div[1]/div[2]/div[1]/div[1]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: Chat drawer header 'EduReach Bot' is visible.
        await expect(page.locator("xpath=/html/body/div[1]/div[2]/div[1]/div[1]/div[1]").nth(0)).to_be_visible(timeout=15000), "Chat drawer header 'EduReach Bot' is visible."
        
        # --> The welcome message from the bot is visible in the chat drawer.
        await page.locator("xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The bot's welcome message is shown in the chat.
        await expect(page.locator("xpath=/html/body/div[1]/div[2]/div[2]/div[1]/div[1]").nth(0)).to_be_visible(timeout=15000), "The bot's welcome message is shown in the chat."
        
        # --> Clicking the suggested question produced a bot reply message in the chat.
        await page.locator("xpath=/html/body/div[1]/div[2]/div[2]/div[2]/div[2]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: A bot reply message is visible in the chat.
        await expect(page.locator("xpath=/html/body/div[1]/div[2]/div[2]/div[2]/div[2]").nth(0)).to_be_visible(timeout=15000), "A bot reply message is visible in the chat."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    