# Hearok-Pinger

Simple program that sends GET requests to website to keep it online. Also will add ways to make checks and make sure that your paths are functioning properly.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Setup

Clone the repository and enter it

```
git clone https://github.com/RafaelCenzano/heroku-pinger.git
cd heroku-pinger
```

### Requirements

Use pip to install needed libraries

```
pip install -r requirements.txt
```

or

```
pip install certifi==2019.3.9
pip install chardet==3.0.4
pip install idna==2.8
pip install requests==2.21.0
pip install urllib3==1.24.1
```

## Running the tests

Test auto run when you run the program using:

```
python main.py
```

### What are the tests checking

The tests check to make sure that the ping function works by pinging always online websites:
- Google
- Facebook
- Github
- Stack Overflow


### What happens when a test fails

The tests will exit the program if tests fail

## Authors

* [**Rafael Cenzano**](https://github.com/RafaelCenzano)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
