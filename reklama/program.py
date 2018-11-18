import webbrowser as przegladarka


sugerowane_reklamy = {
    'rower': 0,
    'iphone': 0
}


if __name__ == "__main__":
    with open('rozmowa.txt') as rozmowa:
        for linia in rozmowa.readlines():
            if 'rower' in linia:
                sugerowane_reklamy['rower'] += 1
            elif 'iphone' in linia:
                sugerowane_reklamy['iphone'] += 1
    if sugerowane_reklamy['rower'] >= sugerowane_reklamy['iphone']:
        przegladarka.open('reklamy/rower.html', new=2)
    else:
        przegladarka.open('reklamy/iphone.html', new=2)
