## DNS for Jekyll's web presence

This repository contains the DNS entries for Jekyll's web presence, which is largely jekyllrb.com.

### Making changes

Modify the YAML file for the zone you'd like to update. The top-level key
is the subdomain value, and its value is a Hash/Dictionary of values.

A record:

```yaml
www:
  type: CNAME
  value: jekyll.github.io.
```

This will create a CNAME record at `www.<your-zone>` which points to
`jekyll.github.io`. Easy, huh?

Now create a new branch, commit your changes, and create a PR.

### Testing

Before applying your change, test it:

```bash
$ script/cibuild || script/apply
```

It should print that there were mismatches and what it would do. Post this in the PR.

### Applying your change

Once you're satisfied with your change, run:

```bash
$ script/apply --doit
```

If it complains about too many changes, be VERY CAREFUL! You can _force_
changes by adding the `--force` flag to your `script/apply` call.

Once your changes have been applied, copy the output and paste it into your PR. Then merge the PR.
