#!/bin/bash
serve:
	# prepare data
	unzip -o data/glottolog_languoid.csv.zip -d data/

	# remove old
	rm -f glottolog.db

	# generate new
	python3 glottologdatasette.py

	pipenv run datasette serve --cors --metadata metadata.json glottolog.db

