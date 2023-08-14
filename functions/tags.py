from uptime_kuma_api import UptimeKumaApi as Api


def create_update_tags(self, _config):
    get_tags = Api.get_tags(self)
    if "tags" in _config:
        for tag in _config['tags']:
            for get_tag in get_tags:
                if tag['name'] == get_tag['name']:
                    print("### | [CREATE/UPDATE] | Tag [{}] detected! ".format(
                        tag['name']
                    ))
                    Api.edit_tag(
                        self,
                        id_=get_tag['id'],
                        name=tag['name'],
                        color=tag['color']
                    )
                    tag_not_found = False
                    break
                else:
                    tag_not_found = True
            if tag_not_found:
                print("### | [CREATE/UPDATE] | Creating tag [{}]".format(
                    tag['name']
                ))
                Api.add_tag(
                    self,
                    name=tag['name'],
                    color=tag['color']
                )


def delete_obsolete_tags(self, _config):
    get_tags = Api.get_tags(self)
    for get_tag in get_tags:
        for tag in _config['tags']:
            if get_tag['name'] == tag['name']:
                tag_not_found = False
                break
            else:
                tag_not_found = True
        if tag_not_found is True:
            print("### | [DELETE] | Obsolete tag found [{}]".format(
                get_tag['name']
            ))
            Api.delete_tag(self, get_tag['id'])