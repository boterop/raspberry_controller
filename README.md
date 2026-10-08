## Install

Run in raspberry console

```sh
  sudo apt-get install rpi.gpio
  python3 -m venv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
```

## Set Up

Copy and paste _.env.example_, rename it with _.env_, and set the data required

## Run the project

`python3 main.py`

## Create systemctl service

Go to `/etc/systemd/system` and create a file `script.service` and write:

```
[Unit]
Description="Script Description"
After=network.target

[Service]
User=server
WorkingDirectory=/home/server/script/
ExecStart=/home/server/script/.venv/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

then `sudo systemctl enable script` and `sudo systemctl start script`

## Features

- <b>Fan controller</b>

  Turn on the fan when the temperature is over MAX_TEMPETURE and turn it off when is under MIN_TEMPETURE (both configurable from .env file)

    ![GPIO](./docs/images/gpio-fan.jpg)