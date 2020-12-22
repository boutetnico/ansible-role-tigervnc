[![tests](https://github.com/boutetnico/ansible-role-tigervnc/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-tigervnc/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.tigervnc-blue.svg)](https://galaxy.ansible.com/boutetnico/tigervnctigervnc)

ansible-role-tigervnc
=====================

This role installs and configures [TigerVNC](https://tigervnc.org/).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable               | Required | Default                 | Choices   | Comments                                       |
|------------------------|----------|-------------------------|-----------|------------------------------------------------|
| tigervnc_dependencies  | yes      | `[dbus-x11]`            | list      |                                                |
| tigervnc_packages      | yes      |                         | list      | See `defaults/main.yml`.                       |
| tigervnc_user          | yes      | `vnc`                   | string    | User running the VNC server.                   |
| tigervnc_group         | yes      | `vnc`                   | string    | Group running the VNC server.                  |
| tigervnc_extra_groups  | yes      | `[]`                    | list      | List of extra groups of vnc server user.       |
| tigervnc_home_dir      | yes      | `/home/vnc`             | string    | Home directory of vnc server user.             |
| tigervnc_password      | yes      | `abcd1234`              | string    | Password required to connect to the VNC server.|
| tigervnc_password_file | yes      | `/home/vnc/.vnc/passwd` | string    | Path to the VNC server password file.          |
| tigervnc_options       | yes      | `-geometry 1440x900`    | string    | VNC server options.                            |
| tigervnc_services      | yes      |                         | string    | See `defaults/main.yml`.                       |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-tigervnc

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
