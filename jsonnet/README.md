# Installation

1. Go to: https://github.com/grafana/jsonnet-language-server/releases
2. Pic the release for your platform
3. Put it in the bin/ directory under here, and rename to
   jsonnet-language-server.
4. Make sure it is executable: `chmod +x bin/jsonnet-language-server`
5. Include the snippet.

# Extra conf

Settings are classically undocumented, so go to
https://github.com/grafana/jsonnet-language-server/blob/main/pkg/server/configuration.go#L33

Example extra conf:

```python
def read_file( path ):
    with open( path, 'r' ) as f:
        return f.read()

def Settingss( **kwargs ):
    if kwargs[ 'language' ] == 'jsonnet':
        return {
            'ls': {
                'jpath': [
                    '/foo/bar/lib'
                ],
                # 'enable_eval_diagnositcs': True,
                'enable_lint_diagnostics': True,
                'ext_vars': {
                    'key': 'value',
                },
                'ext_code': {
                    'otherkey': read_file('input.jsonnet')
                },
                # 'formatting': '' // uses formatting options from jsonnetfmt
            }
        }
```
