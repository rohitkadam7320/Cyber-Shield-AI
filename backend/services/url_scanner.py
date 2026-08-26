from urllib.parse import urlparse

def basic_url_analysis(url):
    p = urlparse(url)

    if p.scheme not in ("http", "https") or not p.netloc:
        return False, 90, "Malicious"

    score = 0
    low = url.lower()

    for word in ["login", "verify", "account", "update", "password", "free", "security-alert"]:
        if word in low:
            score += 10

    if not url.startswith("https://"):
        score += 15
    if len(url) > 100:
        score += 15
    if "@" in url:
        score += 20
    if url.count("-") > 4:
        score += 10

    score = min(score, 100)
    level = "Malicious" if score >= 60 else "Suspicious" if score >= 30 else "Safe"

    return True, score, level
