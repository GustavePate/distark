PYTHON=`which python`
PROTOC=`which protoc`
NAME=`python setup.py --name`
VERSION=`python setup.py --version`
SDIST=dist/$(NAME)-$(VERSION).tar.gz
VENV=/tmp/venv
ZOO=/opt/zookeeper-3.4.5


##############################
#  my targets
##############################

indent:
	$(PYTHON) -m reindent --nobackup *.py
	
protoc:
	$(PROTOC) --python_out=./src/distark/commons/protos/ --proto_path=./ressources/commons/protos/ ./ressources/commons/protos/generic_service.proto
	$(PROTOC) --python_out=./src/distark/commons/protos/services/ --proto_path=./ressources/commons/protos/services/ ./ressources/commons/protos/services/*
	
startbroker:
	echo "TODO"

startworker:
	echo "TODO"

startclient:
	echo "TODO"

zoo:
	$(ZOO)/bin/zkServer.sh restart

zools:
	$(ZOO)/bin/zkCli.sh -server localhost:2181

test.travis:
	py.test --maxfail=5 --showlocals --duration=2 -v -m "not slow and not fullstack"

test.qa:
	py.test --cov src/

test:
	py.test --maxfail=5 --showlocals --pep8 --clearcache --duration=3 -v -s 

clean:
	find . -type f -name "FILE-TO-FIND" -exec rm -f {} \;
	find . -type f -name "*.pyc" -exec rm -f {} \;

##############################
# original targets
############################## 
all: check test source deb

dist: source deb

source:
	$(PYTHON) setup.py sdist

deb:
	$(PYTHON) setup.py --command-packages=stdeb.command bdist_deb

rpm:
	$(PYTHON) setup.py bdist_rpm --post-install=rpm/postinstall --pre-uninstall=rpm/preuninstall

install:
	$(PYTHON) setup.py install --install-layout=deb


check:
	find . -name \*.py | grep -v "^test_" | xargs pylint --errors-only --reports=n
	# pep8
	# pyntch
	# pyflakes
	# pychecker
	# pymetrics

upload:
	$(PYTHON) setup.py sdist register upload
	$(PYTHON) setup.py bdist_wininst upload

init:
	pip install -r requirements.txt --use-mirrors

update:
	rm ez_setup.py
	#wget http://peak.telecommunity.com/dist/ez_setup.py

daily:
	$(PYTHON) setup.py bdist egg_info --tag-date

deploy:
	# make sdist
	rm -rf dist
	python setup.py sdist

	# setup venv
	rm -rf $(VENV)
	virtualenv --no-site-packages $(VENV)
	$(VENV)/bin/pip install $(SDIST)

original_(added)__clean:
	$(PYTHON) setup.py clean
	rm -rf build/ MANIFEST dist build my_program.egg-info deb_dist
	find . -name '*.pyc' -delete

