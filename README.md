# Uptime-Kuma as a code?

This repo contains a simple app that will configure / bootstrap the Uptime-Kuma monitoring.
<br>Idea behind this, is to run it in my homelab pipelines to keep the application "up-to-date"

> **Warning**
> <br>This script is destructive. It will not ask for confirmation as its designed to be used in the CICD scenarios
> <br>Please read the `README.md` and `example_config.yml` before using it on "prod"


## Features:

- ✅ | Adding and updating tags
- ✅ | Deleting obsolete tags
- ❌ | Adding and updating monitors
- ❌ | Deleting obsolete monitors
- ❌ | Associating tags with monitors
- ❌ | And more ...

## How-To:

1. Get the repo
```bash
git clone https://github.com/l33t-sh/uptime-kuma-bootstrap.git
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Create config.yml file in the `config` folder 
<br>Use `example_config.yml` as template
```bash
cp config/example_config.yml config/config.yml
```

4. $$$
```bash
python app.py
```



#### Big thanks to: https://github.com/louislam/uptime-kuma
