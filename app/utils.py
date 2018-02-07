def to_project_style(text):
    if not text:
        return text

    text = text.strip()
    url_txt = ''
    for ch in text:
        url_txt += ch if ch.isalnum() or ch == '.' else ' '

    count = -1
    while count != len(url_txt):
        count = len(url_txt)
        url_txt = url_txt.strip()
        url_txt = url_txt.replace('  ', ' ')
        url_txt = url_txt.replace(' ', '_')
        url_txt = url_txt.replace('_', '_')

    return url_txt.lower()
