# python-demo
Test project using python for simple API and docker

### command to build
packaging :: `python setup.py sdist bdist_wheel`

docker build :: `docker build . -t python-demo`

docker run :: `docker run -it -p 5000:5000 python-demo`
