.PHONY: download test ship

download:
	python download.py


test:
	rm -rf ./test-data/
	flake8 census_data_downloader
	coverage run test.py
	coverage report -m


ship:
	rm -rf build/
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing
