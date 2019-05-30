#!/usr/local/bin/python

import sys

from octodns.provider.yaml import YamlProvider
from octodns.yaml import safe_load
from octodns.manager import Manager
from octodns.zone import Zone
from octodns.record import CnameRecord, AliasRecord

def print_record(record):
    if isinstance(record, CnameRecord) or isinstance(record, AliasRecord):
        print "{} {} -> {}".format(record._type, record.fqdn[0:-1], record.value[0:-1])
    else:
        print "{} {} -> {}".format(record._type, record.fqdn[0:-1], record.values)
    # else:
    #     attrs = vars(record)
    #     print ', '.join("%s: %s" % item for item in attrs.items())


def main(config_file):
    manager = Manager(config_file)

    for zone_name, config in manager.config['zones'].items():
        zone = Zone(zone_name, manager.configured_sub_zones(zone_name))

        try:
            sources = config['sources']
        except KeyError:
            raise Exception('Zone {} is missing sources'.format(zone_name))

        try:
            sources = [manager.providers[source] for source in sources]
        except KeyError:
            raise Exception('Zone {}, unknown source: {}'.format(zone_name,
                                                                     source))

        for source in sources:
            if isinstance(source, YamlProvider):
                source.populate(zone)

        for record in zone.records:
            print_record(record)

config_file = "config/test.yaml"
main(config_file)
