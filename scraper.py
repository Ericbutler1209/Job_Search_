
from bs4 import BeautifulSoup
import requests
from pathlib import Path

def banner():
    ascii_art = r"""
  ____                      _                          
 / ___|  ___  __ _ _ __ ___| |__   ___ _ __ ___   __ _ 
 \___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '_ ` _ \ / _` |
  ___) |  __/ (_| | | | (__| | | |  __/ | | | | | (_| |
 |____/ \___|\__,_|_|  \___|_| |_|\___|_| |_| |_|\__,_|
    """
    print(ascii_art)
    print("Welcome to the Job Search App (Python Edition)!")
    print("================================================\n")

def purpose():
    print("This program will:")
    print(" - Scrape university mission statements using requests + BeautifulSoup.")
    print(" - Save results to text files for your assignment.")
    print(" - (Later) scrape fake job postings and write a CSV.\n")

# ---------- HTTP helper ----------
def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()
    return resp.text

# ---------- Parsing helpers ----------
def first_text_matching(soup: BeautifulSoup, selectors: list[str], must_contain: str | None = None) -> str | None:
    """Try selectors; return first block containing optional substring (case-insensitive)."""
    must = (must_contain or "").lower()
    for sel in selectors:
        for el in soup.select(sel):
            text = " ".join(el.get_text(separator=" ", strip=True).split())
            if not text:
                continue
            if not must or must in text.lower():
                return text
    return None

def save_text(filename: str, text: str):
    Path(filename).write_text(text, encoding="utf-8")
    print(f"Saved -> {filename}\n")

# ---------- TODO 6: XULA ----------
def scrape_xula_mission() -> str:
    """
    Scrape XULA from https://www.xula.edu/about/mission-values.html
    Hints: look for div.editorarea and substring 'founded by Saint'.
    """
    url = "https://www.xula.edu/about/mission-values.html"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")

    # Primary per hint
    text = first_text_matching(
        soup,
        selectors=["div.editorarea", "main .editorarea", ".editorarea *"],
        must_contain="founded by saint"
    )

    # Fallbacks
    if not text:
        text = first_text_matching(soup, selectors=["div.editorarea"]) \
               or first_text_matching(soup, selectors=["main", "article", ".content", ".container"]) \
               or soup.get_text(" ", strip=True)
    return text or ""

# ---------- TODO 7: Southern University ----------
def scrape_southern_mission() -> str:
    """
    Southern University & A&M College mission page.
    """
    url = "https://www.subr.edu/page/mission-statement-subr"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")

    # Try common content containers first; bias with a must_contain snippet you provided earlier.
    text = first_text_matching(
        soup,
        selectors=["main", "article", "section", ".content", ".container", ".editorarea", "div"],
        must_contain="student-focused"
    )

    if not text:
        text = first_text_matching(soup, selectors=["main", "article", "section", ".content", ".container"]) \
               or soup.get_text(" ", strip=True)
    return text or ""

def main():
    banner()
    purpose()

    # ---- XULA
    print("Scraping XULA mission…")
    try:
        xula_text = scrape_xula_mission()
        print("\nXULA Mission (first 400 chars):")
        print(xula_text[:400] + ("..." if len(xula_text) > 400 else ""))
        save_text("xula_mission.txt", xula_text)
    except Exception as e:
        print(f"XULA scrape failed: {e}\n")

    # ---- Southern University
    print("Scraping Southern University mission…")
    try:
        southern_text = scrape_southern_mission()
        print("\nSouthern University Mission (first 400 chars):")
        print(southern_text[:400] + ("..." if len(southern_text) > 400 else ""))
        save_text("southern_mission.txt", southern_text)
    except Exception as e:
        print(f"Southern scrape failed: {e}\n")

if __name__ == "__main__":
    main()
