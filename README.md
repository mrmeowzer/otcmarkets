# otcmarkets

Created a program to scrape the OTC Backend API for certain tickers I was interested in. The program will create two threads (any more will cause a 429 too many requests error) to pull the data. The data will then be used to populate a table named Stock in a Postgres database.

How to use?
* Setup a Postgres database
* Populate the Postgres connection info in the config.py
* Run getotclist.py (this could take awhile to run based on the number of tickers that is pulled)

I've also included a sample Dockerfile if a container is needed.
