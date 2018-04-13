# Glottolog-Datasette

> Serve a version of the Glottolog database via Datasette as a REST-ful API. 

## Examples

- Request: `>>> languoid?label__contains=greek`
- Response: (truncated for most pertinent information)
```json
{
  "rows": [
    {
      "id": "anci1242",
      "label": "Ancient Greek",
      "type": "language",
      "status": "extinct",
      "parent": "indo1319",
      "family": "east2798",
      "lat": 39.8155,
      "long": 21.9129,
      "iso639P3code": "grc",
      "child_family_count": 0,
      "child_language_count": 0,
      "child_dialect_count": 6
    },
    {
      "id": "apul1236",
      "label": "Apulia-Calabrian Greek",
      "type": "language",
      "status": "safe",
      "parent": "indo1319",
      "family": "koin1234",
      "lat": "",
      "long": "",
      "iso639P3code": "",
      "child_family_count": 0,
      "child_language_count": 0,
      "child_dialect_count": 0
    }, ...
  ],
  "table_rows_count": 23495,
  "filtered_table_rows_count": 23,
  "next": null,
  "next_url": null,
  "query_ms": 15.398740768432617,
  "source": "Glottolog",
  "source_url": "http://glottolog.org/meta/downloads/",
  "license": "CC-BY 4.0 International",
  "license_url": "https://creativecommons.org/licenses/by/4.0/"
}
```

- The full Datasette API: <http://datasette.readthedocs.io/en/latest/?badge=latest>
- Other examples of <https://github.com/simonw/datasette/wiki/Datasettes>

Note that thanks to the versioned API-system, future version of the data model are not necessarily compatible.

## Collaboration

Pull requests are welcome.
