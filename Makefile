.PHONY : dev_install test install_and_test

dev_install :
	pip install -e .

test :
	python -m unittest discover -v -s test

install_and_test : dev_install
	python -m unittest discover -v -s test
