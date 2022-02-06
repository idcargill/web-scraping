# Web Scraping

[Recent PR](https://github.com/idcargill/web-scraping)

## Tasks

- Scrape a Wikipedia page and record which passages need citations.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
  - E.g. Citation needed for “lorem spam and impsum eggs”
  - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

- function get_citations_needed_count
- function get_citations_needed_report

### Functions

> get_citations_needed(URL)

returns the number of citations needed or 0.

> get_citations_needed_report(URL)

returns the paragraph text that require citations. or 'No citations needed here'
