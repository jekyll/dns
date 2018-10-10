## DNS for Jekyll's web presence

This repository contains the DNS entries for Jekyll'd web presence, which is largely jekyllrb.com.

### Installation

```bash
script/bootstrap
```

### Usage

Modify the records you'd like to change in `config/<zone>.yaml`. Make a PR.

Once you have approval, check out the branch and run:

```bash
$ script/cibuild
# Changes will be printed. Make sure they look good.
$ script/apply --doit
# Applies the changes
```

### Current Setup

DNS for jekyllrb.com is currently managed by Cloudflare. To increase
transparency and make things a little easier to manage across a team, this
file-based DNS approach was setup. If you wish to change any DNS records
for jekyllrb.com, please submit a pull request.
