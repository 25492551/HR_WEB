r"""
Browser compatibility smoke test (Phase 7).

Runs a minimal cross-browser check using Playwright (Python):
- Loads the homepage via local HTTP server.
- Captures console errors + page errors.
- Verifies key UI behaviors don't crash (menu toggle, CTA click prevented).

Usage (PowerShell):
  & .\venv\Scripts\python.exe .\03_script\08_browser_compat_smoke_test.py --url http://127.0.0.1:8000/
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

from playwright.sync_api import Error, sync_playwright


@dataclass
class BrowserResult:
    name: str
    ok: bool
    user_agent: str
    console_errors: list[str]
    page_errors: list[str]


def run_for_browser(playwright, browser_name: str, url: str) -> BrowserResult:
    console_errors: list[str] = []
    page_errors: list[str] = []

    browser_type = getattr(playwright, browser_name)
    browser = browser_type.launch(headless=True)
    page = browser.new_page()

    def on_console(msg):
        if msg.type == "error":
            console_errors.append(msg.text)

    def on_pageerror(err):
        page_errors.append(str(err))

    page.on("console", on_console)
    page.on("pageerror", on_pageerror)

    try:
        page.goto(url, wait_until="networkidle", timeout=60_000)
        user_agent = page.evaluate("() => navigator.userAgent")

        # Basic DOM sanity checks
        page.locator("header.header").wait_for(timeout=10_000)
        page.locator("section#hero").wait_for(timeout=10_000)
        page.locator("section#contents-1 .card").first.wait_for(timeout=10_000)
        page.locator("section#end .end-message").wait_for(timeout=10_000)

        # Menu toggle (should not throw)
        btn = page.locator("button.nav-hamburger")
        btn.click()
        page.locator("#nav-menu[aria-hidden=\"false\"]").wait_for(timeout=5_000)
        page.keyboard.press("Escape")
        page.locator("#nav-menu[aria-hidden=\"true\"]").wait_for(timeout=5_000)

        # CTA click should be prevented (stay on same URL).
        # Note: CTA is marked aria-disabled=true by design, so we click via JS to validate
        # that the handler prevents navigation (requested: "no CTA function now").
        before = page.url
        page.eval_on_selector("a.card-cta", "el => el.click()")
        after = page.url
        if after != before:
            console_errors.append(f"CTA navigation occurred unexpectedly: {before} -> {after}")

        ok = len(console_errors) == 0 and len(page_errors) == 0
        return BrowserResult(browser_name, ok, user_agent, console_errors, page_errors)
    except Error as e:
        user_agent = ""
        page_errors.append(f"Playwright error: {e}")
        return BrowserResult(browser_name, False, user_agent, console_errors, page_errors)
    finally:
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Homepage URL, e.g. http://127.0.0.1:8000/")
    args = parser.parse_args()

    url = args.url
    browsers = ["chromium", "firefox", "webkit"]

    results: list[BrowserResult] = []
    with sync_playwright() as p:
        for b in browsers:
            results.append(run_for_browser(p, b, url))

    print("Browser compatibility smoke test results")
    print(f"Target: {url}")
    print("-" * 60)

    exit_code = 0
    for r in results:
        status = "PASS" if r.ok else "FAIL"
        print(f"{r.name:8}  {status}")
        if r.user_agent:
            print(f"  UA: {r.user_agent}")
        if r.console_errors:
            print("  Console errors:")
            for line in r.console_errors:
                print(f"   - {line}")
        if r.page_errors:
            print("  Page errors:")
            for line in r.page_errors:
                print(f"   - {line}")
        if not r.ok:
            exit_code = 1
        print("-" * 60)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

