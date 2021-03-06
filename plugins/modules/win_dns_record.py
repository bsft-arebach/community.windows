#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Hitachi ID Systems, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# This is a windows documentation stub. The actual code lives in the .ps1
# file of the same name.

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: win_dns_record
short_description: Manage Windows Server DNS records
description:
- Manage DNS records within an existing Windows Server DNS zone.
author: John Nelson (@johnboy2)
requirements:
  - This module requires Windows 8, Server 2012, or newer.
options:
  name:
    description:
    - The name of the record.
    required: yes
    type: str
  state:
    description:
    - Whether the record should exist or not.
    choices: [ absent, present ]
    default: present
    type: str
  ttl:
    description:
    - The "time to live" of the record, in seconds.
    - Ignored when C(state=absent).
    - Valid range is 1 - 31557600.
    - Note that an Active Directory forest can specify a minimum TTL, and will
      dynamically "round up" other values to that minimum.
    default: 3600
    type: int
  type:
    description:
    - The type of DNS record to manage.
    choices: [ A, AAAA, CNAME, PTR ]
    required: yes
    type: str
  value:
    description:
    - The value(s) to specify. Required when C(state=present).
    - When C(type=PTR) only the partial part of the IP should be given.
    aliases: [ values ]
    type: list
  zone:
    description:
    - The name of the zone to manage (eg C(example.com)).
    - The zone must already exist.
    required: yes
    type: str
  computer_name:
    description:
      - Specifies a DNS server.
      - You can specify an IP address or any value that resolves to an IP
        address, such as a fully qualified domain name (FQDN), host name, or
        NETBIOS name.
    type: str
'''

EXAMPLES = r'''
# Demonstrate creating a matching A and PTR record.

- name: Create database server record
  win_dns_record:
    name: "cgyl1404p.amer.example.com"
    type: "A"
    value: "10.1.1.1"
    zone: "amer.example.com"

- name: Create matching PTR record
  win_dns_record:
    name: "1.1.1"
    type: "PTR"
    value: "db1"
    zone: "10.in-addr.arpa"

# Demonstrate replacing an A record with a CNAME

- name: Remove static record
  win_dns_record:
    name: "db1"
    type: "A"
    state: absent
    zone: "amer.example.com"

- name: Create database server alias
  win_dns_record:
    name: "db1"
    type: "CNAME"
    value: "cgyl1404p.amer.example.com"
    zone: "amer.example.com"

# Demonstrate creating multiple A records for the same name

- name: Create multiple A record values for www
  win_dns_record:
    name: "www"
    type: "A"
    values:
      - 10.0.42.5
      - 10.0.42.6
      - 10.0.42.7
    zone: "example.com"

# Demonstrates a partial update (replace some existing values with new ones)
# for a pre-existing name

- name: Update www host with new addresses
  win_dns_record:
    name: "www"
    type: "A"
    values:
      - 10.0.42.5  # this old value was kept (others removed)
      - 10.0.42.12  # this new value was added
    zone: "example.com"
'''

RETURN = r'''
'''
