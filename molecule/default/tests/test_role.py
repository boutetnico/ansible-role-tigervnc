import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    [
        ("tigervnc-common"),
        ("tigervnc-standalone-server"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("/home/vnc/.vnc/passwd", "vnc", "vnc", 0o600),
    ],
)
def test_tigervnc_password_file_exist(host, file, user, group, mode):
    restic = host.file(file)
    assert restic.exists
    assert restic.is_file
    assert restic.user == user
    assert restic.group == group
    assert restic.mode == mode


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/etc/systemd/system/vncserver@.service"),
    ],
)
def test_systemd_config_file_exists(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize(
    "name",
    [
        ("vncserver@1"),
    ],
)
def test_vncserver_service_is_running(host, name):
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize(
    "endpoint",
    [
        ("tcp://127.0.0.1:5901"),
    ],
)
def test_vncserver_is_reachable(host, endpoint):
    server = host.socket(endpoint)
    assert server.is_listening
