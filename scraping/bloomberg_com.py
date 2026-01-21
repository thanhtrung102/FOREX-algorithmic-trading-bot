from bs4 import BeautifulSoup
import cloudscraper

def get_article(card):
    """Extract headline and link from a card element."""
    if card is None:
        return None
    href = card.get('href', '')
    if not href.startswith('http'):
        href = 'https://www.reuters.com' + href
    return dict(
        headline=card.get_text(strip=True),
        link=href
    )


def bloomberg_com():
    """
    Scrape financial headlines from Reuters.
    Note: This function is named bloomberg_com for legacy compatibility,
    but actually scrapes Reuters finance section.

    Returns:
        list: List of dicts with 'headline' and 'link' keys, or empty list on error.
    """
    try:
        s = cloudscraper.create_scraper()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
        }

        resp = s.get("https://www.reuters.com/business/finance/", headers=headers, timeout=10)

        if resp.status_code != 200:
            return []

        soup = BeautifulSoup(resp.content, 'html.parser')

        links = []
        # Try multiple selector patterns as Reuters may change their HTML structure
        selectors = [
            '[class*="media-story-card__body"] a[data-testid="Heading"]',
            '[class*="story-card"] a[data-testid="Heading"]',
            'article a[data-testid="Heading"]',
            'h3 a',
        ]

        for selector in selectors:
            cards = soup.select(selector)
            if cards:
                for card in cards:
                    article = get_article(card)
                    if article and article['headline']:
                        links.append(article)
                break

        return links if links else []
    except Exception as e:
        print(f"Error scraping Reuters: {e}")
        return []


# Alias for clarity
reuters_finance = bloomberg_com
