clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf *.egg-info
	-rm -f tests/.coverage
	-docker rm `docker ps -a -q`
	-docker rmi `docker images -q --filter "dangling=true"`

build: clean
	python setup.py bdist_wheel --universal

install: uninstall build
	pip install dist/*.whl

uninstall:
	-pip uninstall -y vlab-link-api

test: uninstall install
	cd tests && nosetests -v --with-coverage --cover-package=vlab_link_api

images: build
	docker build -t willnx/vlab-link-api .
