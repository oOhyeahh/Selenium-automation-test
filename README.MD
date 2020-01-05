## Set Up
[Python](https://www.python.org/downloads/) v3.7.3+ 
[Virtualenv](https://virtualenv.pypa.io/en/latest/installation/) 
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


- Create virtual environment (python3.7)
  ```sh
  $ virtualenv --python=python3.7 venv
  ```
- Active virtual environment: 
  ```sh
  $ source venv/bin/activate
  ```
- Install packages
  ```sh
  $ pip install -r requirements.txt
  ``` 

## How to run the automation test

```sh
$ python -m pytest
```