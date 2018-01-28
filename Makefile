.PHONY: clean test

test:
	nosetests  -v --cover-erase --cover-branches --with-coverage --cover-html

clean:
	find . -name *.pyc -exec rm -f {} \; ;\
	rm -rf ./cover
