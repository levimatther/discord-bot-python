# Basic Discord Bot

This bot is created using discord's libraries for searching over google & persisting history for lookup.

## Technologies Used:

- Python3.8
- Redis
- MySQL

## Installation:
- [Install python3.8](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)

- [Install pip3](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)

- [Install Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

- [Install Git](https://linuxize.com/post/how-to-install-git-on-ubuntu-18-04/)

- [Install MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
- [Install Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)


Install Python Dependencies:
```bash
sudo apt install python3-dev 
```

Clone the repository using:
```bash
git@github.com:suhridmathur/discord-bot.git
```
Create environment and install python packages:
```bash
virtualenv -p python3.8 env
pip install -r requirementst.txt
```

Export the following envirnment variables in bashrc:
- BOT_TOKEN
- BOT_DB_URI
- GOOGLE_SEARCH_API_KEY
- GOOGLE_SEARCH_CX


Run server:
```python
python bot.py
```
