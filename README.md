# Small Procurements

Machine-readable data for public procurements that are too small to get published
through regular channels. In Switzerland, public procurements between 50K and 150K CHF
do not get published in [SIMAP](https://www.simap.ch/) but as a hodgepodge of Excel
and PDF files. We collect this data, clean it up, and make it available in
machine-readable form.


## Deelopment Roadmap

1. Add all [11 Swiss data sources](https://www.bkb.admin.ch/bkb/de/home/bkb/ab_50000_franken.html).
   Each of them has a different format.
2. Publish this data in [eForms](https://docs.ted.europa.eu/home/eforms/FAQ/index.html)
   format.
3. Support additional countries, if there’s similar data sources elsewhere.


## Data Sources

* [Swiss Post Public Procurements](https://www.post.ch/de/ueber-uns/verantwortung/beschaffungspolitik) 2021:
  Extracted text from
  [PDF](https://www.post.ch/-/media/post/ueber-uns/dokumente/beschaffungsreporting.pdf?vs=1&sc_lang=de&hash=C704119B042E8D00BD413C568C30712F).
  Manually added county codes, company IDs and CPV codes.


## License

Code: MIT; Data: Creative Commons Zero.
