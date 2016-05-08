# test-releases-api

This repository was used for testing adding of release assets using the GitHub
API. It contains a Python 3 script, github-api-releases.py, which can be used
to add a release asset to an existing GitHub release.

The github-api-releases.py script requires that you have an environment
variable (GITHUB\_TOKEN) set. You can generate a personal access token via
the user settings when you are logged into your GitHub account on the web
interface, or you can use curl to request a token. In either case, I used the
repo scope to get permission to be able to add assets.

To use curl:

```
curl -u username --data '{"scopes":["repo"], "note":"test"}' https://api.github.com/authorizations
```

Replace username with your GitHub username. The value of "note" (test in this
example) should be replaced with something meaningful to you, because it will
show up if you look at the personal access tokens page on the GitHub web
interface. Curl will prompt you for your GitHub password. Then the response
from the API will contain a "token" value that you can use with
github-api-releases.py.
