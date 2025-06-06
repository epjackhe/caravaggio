import requests
from bs4 import BeautifulSoup

URL = "https://caravaggio.coopculture.it/index.php?option=com_snapp&view=event&id=E2BE2FD9-64E4-5D37-412E-0194603DC454&catalogid=99786C19-0560-A43D-591F-019712AF59E4&lang=it"
HEADERS = {"User-Agent": "Mozilla/5.0"}

UNAVAILABLE_TEXTS = [
    "posti esauriti",
    "sold out",
    "non disponibile",
]

def check_availability():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        return False

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator=' ').lower()
    return not any(phrase in text for phrase in UNAVAILABLE_TEXTS)

if __name__ == "__main__":
    if check_availability():
        print("Tickets might be available!")
    else:
        print("Tickets not available yet.")
