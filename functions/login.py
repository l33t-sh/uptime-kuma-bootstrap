from uptime_kuma_api import UptimeKumaApi as Api


def login(self, _config):
    print("### | Logging in as [{}]".format(
        _config['login']['username']
    ))
    Api.login(
        self,
        username=_config['login']['username'],
        password=_config['login']['password'],
        token=_config['login']['totp'] if "totp" in _config['login'] else None
    )