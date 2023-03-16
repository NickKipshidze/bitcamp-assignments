import sys, requests, json

try:
    coin_count = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")

    data = json.loads(
        json.dumps(
            response.json()
        )
    )

    print(f"${float(data['bpi']['USD']['rate'].replace(',',''))*coin_count:,.4f}")

except requests.RequestException:
    pass