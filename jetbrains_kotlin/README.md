# Kotlin LSP

JetBrains Kotlin Language Server Protocol (LSP) implementation based on IntelliJ
IDEA's Kotlin plugin.

## Installation

Requires being run with java 17 or later. The `JAVA_HOME` environment variable
must be set to ponit to a java 17 or later to run the language server.

1. Download the zip from https://github.com/Kotlin/kotlin-lsp/blob/main/RELEASES.md
   and unpack it into this directory/kotlin-lsp. Make the `kotlin-lsp.sh` script
   executable.
2. Include the snippet

Example:

```
cd lsp-examples/jetbrains_kotlin
wget <url of latest zip>
mkdir kotlin-lsp
cd kotlin-lsp
unzip ../<latest zip>
chmod +x kotlin-lsp.sh
```

If you can't have JAVA_HOME set globally in your Vim environment, you can
manually set up the snippet to use any java 17 or later installation.

```viml
let g:ycm_language_server += [
  \   {
  \     'name': 'jetbrains_kotlin',
  \     'cmdline': [
  \       '/usr/bin/env', 'JAVA_HOME=/path/to/java17',
  \       expand( g:ycm_lsp_dir ) . '/jetbrains_kotlin/kotlin-lsp/kotlin-lsp.sh',
  \       '--stdio',
  \     ],
  \     'filetypes': [ 'kotlin' ],
  \     'project_root_files': [ 'build.gradle', 'build.gradle.kts', 'pom.xml' ],
  \   },
  \ ]

```

## Inlay Hints

To enable inlay hints, add a `.ycm_extra_conf.py` to your project root with the
`config_sections` for `jetbrains.kotlin`. The server currently supports two hint
categories:

```python
def Settings( **kwargs ):
  return {
    'config_sections': {
      'jetbrains.kotlin': {
        'hints': {
          # Show parameter name hints at call sites
          'parameters': True,
          # Show return type hints in call chains
          'call': { 'chains': True },
        },
      },
    },
  }
```

See `test/.ycm_extra_conf.py` for a working example.
