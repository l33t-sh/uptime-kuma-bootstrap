from uptime_kuma_api import UptimeKumaApi
import yaml

with open('config/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)


def login(_config):
    api.login(
        username=_config['login']['username'],
        password=_config['login']['password'],
        token=_config['login']['totp'] if "totp" in config['login'] else None
    )


def create_update_tags(_config):
    login(config)
    get_tags = api.get_tags()
    if "tags" in _config:
        print("### | tags detected in config file!")
        for tag in config['tags']:
            for get_tag in get_tags:
                if tag['name'] == get_tag['name']:
                    print("### | Tag [{}] detected! ".format(
                        tag['name']
                    ))
                    api.edit_tag(
                        id_=get_tag['id'],
                        name=tag['name'],
                        color=tag['color']
                    )
                    tag_not_found = False
                    break
                else:
                    tag_not_found = True
            if tag_not_found:
                print("### | Creating tag [{}]".format(
                    tag['name']
                ))
                api.add_tag(
                    name=tag['name'],
                    color=tag['color']
                )


def delete_obsolete_tags(_config):
    login(config)
    get_tags = api.get_tags()
    for get_tag in get_tags:
        for tag in config['tags']:
            if get_tag['name'] == tag['name']:
                tag_not_found = False
                break
            else:
                tag_not_found = True
        if tag_not_found is True:
            print("### | Obsolete tag found [{}]".format(
                get_tag['name']
            ))
            api.delete_tag(get_tag['id'])


with UptimeKumaApi(config['url']) as api:
    create_update_tags(config)
    delete_obsolete_tags(config)


