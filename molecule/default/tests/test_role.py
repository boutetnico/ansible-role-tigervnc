import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("tigervnc-common"),
        ("tigervnc-standalone-server"),
        ("dbus-x11"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_vnc_group_exists(host):
    group = host.group("vnc")
    assert group.exists


def test_vnc_user_exists(host):
    user = host.user("vnc")
    assert user.exists
    assert user.group == "vnc"
    assert user.home == "/home/vnc"


def _vnc_dir(host):
    """Return the VNC config directory based on OS version."""
    if host.file("/home/vnc/.config/tigervnc").exists:
        return "/home/vnc/.config/tigervnc"
    return "/home/vnc/.vnc"


@pytest.mark.parametrize(
    "directory,user,group",
    [
        ("/home/vnc", "vnc", "vnc"),
    ],
)
def test_vnc_directories_exist(host, directory, user, group):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == user
    assert d.group == group


def test_vnc_config_directory_exists(host):
    d = host.file(_vnc_dir(host))
    assert d.exists
    assert d.is_directory
    assert d.user == "vnc"
    assert d.group == "vnc"


def test_tigervnc_password_file_exist(host):
    f = host.file(f"{_vnc_dir(host)}/passwd")
    assert f.exists
    assert f.is_file
    assert f.user == "vnc"
    assert f.group == "vnc"
    assert f.mode == 0o600


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
        ("vncserver@2"),
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
        ("tcp://127.0.0.1:5902"),
    ],
)
def test_vncserver_is_reachable(host, endpoint):
    server = host.socket(endpoint)
    assert server.is_listening
