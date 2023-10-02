import json

import requests

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)

PAGE_SIZE = 100

URL = "https://api.wr-rims-prod.pulselive.com/rugby/v3/match"

# for year in range(2023, 2009, -1):
for year in [2023]:
    params = {
        "endDate": str(year) + "-12-31",
        "startDate": str(year) + "-01-01",
        "sort": "desc",
        "sport": "mru",
        "states": "C",
        "pageSize": "1",
        "page": "0",
    }

    x = requests.get(URL, params=params, verify=False)
    data = json.loads(x.text)
    with open(f"json/{year}-sample.json", "w") as outfile:
        json.dump(data, outfile)

    num_entries = data["pageInfo"]["numEntries"]
    print(f"year {year} has {num_entries} entries")

    params["pageSize"] = PAGE_SIZE

    for page in range(0, num_entries // PAGE_SIZE + 1):
        print(f"getting year {year} page {page}")
        params["page"] = page
        x = requests.get(URL, params=params, verify=False)
        data = json.loads(x.text)
        with open(f"json/{year}-{page:02}.json", "w") as outfile:
            json.dump(data, outfile)

    print(f"year {year} done")

quit()
