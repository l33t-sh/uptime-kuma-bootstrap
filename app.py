from uptime_kuma_api import UptimeKumaApi
from functions.login import login
from functions.tags import create_update_tags, delete_obsolete_tags
import yaml

with open('config/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

with UptimeKumaApi(config['url']) as api:
    login(api, _config=config)
    create_update_tags(api, _config=config)
    delete_obsolete_tags(api, _config=config)




