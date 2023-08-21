import argparse
import requests
import json
import utils

def myParser():
    parser = argparse.ArgumentParser(epilog=utils.getText(), 
                                    description='Returns average exchange rate in PLN', 
                                    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-c', '--code', help='Put country code to get the currency rate')
    parser.add_argument('-ctr', '--country', 
                        help='Put country name in order to get a currency rate and code')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    myArgs = myParser()
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/')
    data = json.loads(r.text)

    if myArgs.code:
        print(utils.currencyCode(myArgs.code, utils.prepData(data)))
    elif myArgs.country:
        code = utils.countryName(myArgs.country)
        print(utils.currencyCode(code, utils.prepData(data)))
    else:
        print("\n\tNo code or country name given.\n")