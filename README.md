# ansible-role-general-installer

ansible role to download and install software

* [suzuki-shunsuke.general-installer](https://galaxy.ansible.com/suzuki-shunsuke/general-installer/)

## Requirements

* http://docs.ansible.com/ansible/latest/unarchive_module.html#notes

## Role Variables

name | required | default | short description
--- | --- | --- | ---
general_installer_uri | yes | | download uri
general_installer_checked_file | no | undefined |
general_installer_files | no | [] |
general_installer_links | no | {} |
general_installer_params | no | {} |
general_installer_unarchived_suffixes | no | [".tgz", ".zip", ".tar", ".tar.gz", ".tar.bz2", ".tar.xz"]

You can use placeholders in the following parameters.

* general_installer_uri
* general_installer_links
* general_installer_checked_file
* general_installer_files

You can define the pairs of the placeholder name and value as `general_installer_params`.

### general_installer_checked_file

If this file has already existed, this role doesn't download the software.
If this variable is undefined or falthy this role download the software.

## Dependencies

Nothing.

## Example Playbook

```yaml
- hosts: servers
  roles:
    # Install jq
    - role: suzuki-shunsuke.general-installer
      install:
        general_installer_uri: https://github.com/stedolan/jq/releases/download/jq-$VERSION/jq-$ARCH
        general_installer_checked_file: /usr/local/bin/jq-$VERSION
        general_installer_files:
          - src: jq-$ARCH
            dest: /usr/local/bin/jq-$VERSION
        general_installer_links:
          /usr/local/bin/jq: /usr/local/bin/jq-$VERSION
        general_installer_params:
          "$VERSION": "1.5"
          "$ARCH": linux64
      become: yes
```

When we run the above playbook, `jq` is installed as the following.

```
/usr/local/bin/
  jq-1.5
  jq -> /usr/local/bin/jq-1.5
```

## Change Log

See [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
