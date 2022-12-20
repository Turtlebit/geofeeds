"""
This script generate a global and per continent geofeeds.

It opens a `geo.yml` file containing a list of subnets. Here's an example:

```yaml
- subnet: 2a0c:b641:61b::/48
  continent: europe
  country: PT
  region: PT-13
  city: Porto
  geo: null
```

Only ``subnet``, ``continent`` and ``country`` are mandatory. You can omit a value or
use ``null`` for ``region``, ``city`` and ``geo`` attributes.
"""

import csv
from datetime import datetime
from typing import Optional

import yaml

# XXX: To avoid broken links, never comment a continent if it has been one
# day uncommented.
CONTINENTS = [
    # "africa",
    # "america",
    "asia",
    "europe",
    # "oceania",
]


def generate_csv(conf, continent: Optional[str] = None):
    """
    Generate a geofeed CSV containing the name of the given continent
    (in case no continent has been given, the CSV file is called `geofeed.csv`).
    """

    name = f"geofeed-{continent}.csv" if continent else "geofeed.csv"
    continent = continent.capitalize() if continent else ""
    now = datetime.utcnow().isoformat()

    if continent:
        print(f"Generating geofeed for {continent}...")
    else:
        print("Generating global geofeed...")

    with open(name, "w") as f:
        # Add header to the CSV
        f.writelines(
            "# Self-published geofeed as defined in "
            "datatracker.ietf.org/doc/html/rfc8805\n"
            f"# TurtleBit {continent} Geofeed,lastupdated (rfc3339): {now}\n"
        )

        writer = csv.writer(f, delimiter=",")

        # Write each line to the file
        for val in conf:
            subnet = [
                val["subnet"],
                val["country"],
                val.get("region", ""),
                val.get("city", ""),
                val.get("geo", ""),
            ]

            for idx, v in enumerate(subnet):
                if v is None or v in ("null", "nil", "none"):
                    subnet[idx] = ""

            writer.writerow(subnet)


with open("./geo.yml", "r") as f:
    conf = yaml.load(f, yaml.BaseLoader)

    continents_conf = {}
    for continent in CONTINENTS:
        continents_conf[continent] = [v for v in conf if v["continent"] == continent]

    # Generate the global geofeed file
    generate_csv(conf)

    # Generate a geofeed file for each continent
    for continent, conf in continents_conf.items():
        generate_csv(conf, continent)

    print("All geofeeds have been generated.")
