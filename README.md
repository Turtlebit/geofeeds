# TurtleBit.net (AS208505) geofeeds

[Source code](https://github.com/Turtlebit/geofeeds)

This repository contains all geofeeds exposed on [geofeed.turtlebit.net](https://geofeed.turtlebit.net).

Geofeeds are generated via the `generate_geofeeds.py` and the configuration file `geo.yml`.

## Available geofeeds

 - [Global geofeed](https://geofeed.turtlebit.net/geofeed.csv)
 - [Europe geofeed](https://geofeed.turtlebit.net/geofeed-europe.csv)
 - [Asia geofeed](https://geofeed.turtlebit.net/geofeed-asia.csv)


## How to use

To update geofeeds, you will need to have Python and [Poetry](https://github.com/python-poetry/poetry) installed on your machine.

To add, update or remove a geofeed information:

 - update the `geo.yml` file
 - run `poetry run geofeeds`.
 - Review all changes, commit and make a pull request for review.

Once, the pull request has been merged, geofeeds will be automatically updated on [geofeed.turtlebit.net](https://geofeed.turtlebit.net).


## Script contributions

In case you make modifications to the `generate_geofeeds.py` script, please run `ruff`.
