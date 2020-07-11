from bs4 import BeautifulSoup


def example_html_filter(html_text: str) -> str:
    soup = BeautifulSoup(html_text, 'html.parser')
    return str(soup.find_all('a'))
