import re


def make_arn_for_load_balancer(account_id, name, region_name, type):
    short_type = 'net' if type == 'network' else 'app'
    return "arn:aws:elasticloadbalancing:{}:{}:loadbalancer/{}/{}/50dc6c495c0c9188".format(
        region_name, account_id, short_type, name)


def make_arn_for_target_group(account_id, name, region_name):
    return "arn:aws:elasticloadbalancing:{}:{}:targetgroup/{}/50dc6c495c0c9188".format(
        region_name, account_id, name)


def lowercase(str):
    return '_'.join(re.sub(r'([A-Z])', r' \1', str).split()).lower()
