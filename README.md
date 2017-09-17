# open511-orl

[Open511](http://open511.org) implementation for Orlando road closures, accidents, and events

## Endpoints

All endpoints accept the following arguements:

- **format**: Response format - JSON (default), XML

### `/ (root)`

Information about the jurisdictions and servers available from the server

```json
{
  "jurisdictions": [
    {
      "geography_url": "http://open511.cityoforlando.net/jurisdiction/cityoforlando.net/geography",
      "id": "cityoforlando.net",
      "name": "Orlando",
      "url": "http://open511.cityoforlando.net/jurisdiction/cityoforlando.net"
    }
  ],
  "services": [
    {
      "service_type_url": "http://open511.org/services/events",
      "url": "/events/"
    },
    {
      "service_type_url": "http://open511.org/services/areas",
      "url": "/areas/"
    }
  ],
  "meta": {
    "version": "v1"
  }
}
```

### `/jurisdictions`

Information about all of the covered jurisdictions. Static values set in `config.py`

```json
{
  "jurisdictions": [
    {
      "description": "Road closure information from Orlando, FL",
      "email": "test@cityoforlando.net",
      "geography_url": "/jurisdictions/cityoforlando.net/geography",
      "id": "cityoforlando.net",
      "languages": [
        "en"
      ],
      "license_url": "http://www.cityoforlando.net/legal/",
      "name": "Orlando",
      "phone": "123-456-7890",
      "timezone": "America/New_York",
      "url": "/jurisdictions/cityoforlando.net"
    }
  ],
  "meta": {
    "version": "v1"
  }
}
```

### `/jurisdictions/<city_id>`

Information about a specific jurisdiction by `id` value

```json
{
  "jurisdiction": {
    "description": "Road closure information from Orlando, FL",
    "email": "test@cityoforlando.net",
    "geography_url": "/jurisdictions/cityoforlando.net/geography",
    "id": "cityoforlando.net",
    "languages": [
      "en"
    ],
    "license_url": "http://www.cityoforlando.net/legal/",
    "name": "Orlando",
    "phone": "123-456-7890",
    "timezone": "America/New_York",
    "url": "/jurisdictions/cityoforlando.net"
  },
  "meta": {
    "version": "v1"
  }
}
```

### `/jurisdictions/<city_id>/geography`

The city limit as GeoJSON. Static values placed in the geometries folder and refereced in `config.py`

```json
{
  "geography": {
    "coordinates": [
      [
        [
          [
            -81.4194608188114,
            28.613177133793723
          ],
          [
            -81.41918968233719,
            28.61303979445275
          ], ...
        ], ...
      ], ...
    ],
    "type": "MultiPolygon"
  },
  "meta": {
    "version": "v1"
  }
}
```

## Setup

This project should be compatible with any version of Python3. Install the Python dependancies using:

```bash
pip install -r requirements.txt
```

## Running

We can use the Flask CLI to handle a variety of tools including starting the server. The first thing we need to do is add a path to the Flask root to our environment. You'll also want to enable debug mode when not deploying to production.

Bash:
```bash
export FLASK_APP=/path/to/open511/__init__.py
export FLASK_DEBUG=1
```

Powershell:
```powershell
$env:FLASK_APP = "C:\path\to\open511\__init__.py"
$env:FLASK_DEBUG = 1
```

To run the app, simply call `run`:

```bash
flask run
```

When running in debug mode, the server will automatically reload when a .py file changes. The server might have to be restarted when changing .html templates before the changes are shown.

# Production

The `flask` command is not designed for the rigors of a production envirnment. For example, it can only handle one connection at a time. The current plan is to use [Zappa](http://zappa.io/) to deploy the API to AWS Lambda, but that will come later.