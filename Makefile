.PHONY: download test


download:
	pipenv run python download.py

test:
	rm -rf ./test-data/
	pipenv run coverage run test.py
	pipenv run coverage report -m

ship:
	rm -rf build/
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/* --skip-existing