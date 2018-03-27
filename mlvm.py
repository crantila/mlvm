#!/usr/bin/env python3

import pathlib
import subprocess

import begin


INSTALL_BASE = '/opt'
MLVM_VERSION = '1.2-linux'

BINARY_DIRECTORY = pathlib.Path('/opt/MarkLogic')
SERVICE_FILE = pathlib.Path('/etc/init.d/MarkLogic')
SETTINGS_FILE = pathlib.Path('/etc/sysconfig/MarkLogic')
INSTALLED_PATHS = [SETTINGS_FILE, BINARY_DIRECTORY, SERVICE_FILE]


@begin.subcommand
def activate(label: 'version label (used at install time)'):
    """
    Activate an installed MarkLogic version.
    """
    deactivate()

    installed_root = pathlib.Path('/opt/MarkLogic-{label}'.format(label=label))
    assert installed_root.exists()
    installed_binary = installed_root.joinpath('opt/MarkLogic')
    installed_settings = installed_root.joinpath('etc/sysconfig/MarkLogic')
    installed_service = installed_root.joinpath('etc/init.d/MarkLogic')
    assert installed_binary.exists()
    assert installed_settings.exists()
    assert installed_service.exists()

    BINARY_DIRECTORY.symlink_to(installed_binary, target_is_directory=True)
    SERVICE_FILE.symlink_to(installed_service)
    SETTINGS_FILE.symlink_to(installed_settings)


@begin.subcommand
def deactivate():
    """
    Deactivate the currently active MarkLogic version.
    """
    can_deactivate = all([p.is_symlink() or (not p.exists()) for p in INSTALLED_PATHS])
    if not can_deactivate:
        raise RuntimeError('MLVM will not delete an existing installation.')

    for path in INSTALLED_PATHS:
        try:
            path.unlink()
        except FileNotFoundError:
            pass


@begin.subcommand
def install(archive: 'RPM package to install', label: 'version label'):
    """
    Install a new MarkLogic version.
    """
    # some sanity checks
    archive = pathlib.Path(archive)
    assert archive.exists()
    assert archive.is_file()
    install_root = pathlib.Path('/opt/MarkLogic-{label}'.format(label=label))
    assert not install_root.exists()

    # do the install
    install_root.mkdir(parents=True)
    command = 'cd {root} && rpm2cpio {archive} | cpio -idum'.format(
        root=str(install_root),
        archive=str(archive),
    )
    subprocess.run(command, shell=True)


@begin.subcommand
def start():
    """
    Start the active MarkLogic version.
    """
    is_activated = all([p.exists() and p.is_symlink() for p in INSTALLED_PATHS])
    if not is_activated:
        raise RuntimeError('Please activate a MarkLogic version before starting.')

    subprocess.run(['service', 'MarkLogic', 'start'])


@begin.subcommand
def stop():
    """
    Stop the active MarkLogic version.
    """
    is_activated = all([p.exists() and p.is_symlink() for p in INSTALLED_PATHS])
    if not is_activated:
        raise RuntimeError('Please activate a MarkLogic version before stopping.')

    subprocess.run(['service', 'MarkLogic', 'stop'])


@begin.start
@begin.logging
def start():
    print('mlvm {0}\n'.format(MLVM_VERSION))
