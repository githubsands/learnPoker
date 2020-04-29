init:
	pip install -r requirements.txt
	touch conftest.py
depend:
	pip install -r requirements.txt
test:
	echo "testing"
	touch conftest.py
	cd tests
	pytest
	rm -rf conftest.py
cleanup:
	rm -rf conftest.py
	echo "done cleaning up"
