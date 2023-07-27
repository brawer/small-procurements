# Small Procurements

Machine-readable data for public procurements that are too small to get published
through regular channels. In Switzerland, public procurements between 50K and 150K CHF
do not get published in [SIMAP](https://www.simap.ch/) but as a hodgepodge of Excel
and PDF files. We collect this data, clean it up, and annotate it with company IDs
and CPV codes. Eventually we plan making it available in machine-readable form,
probably in the same XML format that is used for European procurement records.


## Development Roadmap

1. Add all [Swiss data sources](https://www.bkb.admin.ch/bkb/de/home/bkb/ab_50000_franken.html).
   Each of them has a different format.
2. Publish this data in [eForms](https://docs.ted.europa.eu/home/eforms/FAQ/index.html)
   format.
3. Support additional countries, if there’s similar data sources elsewhere.


## License

Code: MIT; Data: Creative Commons Zero.
