from countries import countryListA


def getText() -> list[list[str]]:
    text = [f'\t{x[-1]}: {x[0]}, {x[1]}' for x in countryListA]
    return '\n'.join(text)


def prepData(data: list[dict]) -> list[dict[str, str]]:
    data = data[0]
    return data['rates']


def findCountry(code: str) -> str:

    for i in range(len(countryListA)):
        if code == countryListA[i][2]:
            ctrName = countryListA[i][1]
            return ctrName


def currencyCode(code: str, data: list[dict[str, str]]) -> str:

    for j in range(len(data)):
        if code.upper() == data[j]['code']:
            return f"\n\tCountry: {findCountry(code.upper())}\n\tCode: {code.upper()}\n\tRate: {data[j]['mid']}\n"
    else:
        return f'\n\tNo country code in table A.\n'


def countryName(name: str) -> str:

    for i in range(len(countryListA)):
        if name == countryListA[i][0] or name == countryListA[i][1]:
            code = countryListA[i][2]
            return code
    else:
        print(f"\n\tNo country name in table A.")
        return ''