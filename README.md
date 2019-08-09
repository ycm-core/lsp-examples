# Overview

This repo includes a simple way to install some language servers that might work
with YouCompleteMe (strictly ycmd). 

This repo comes with no warranty, and these engines are not officially supported
by YCM, though they should work for the most part.

# Languages Tested

Working:

* D
* Dockerfile
* Kotlin
* Ruby
* Vue
* Vim (vimscript)

Broken or partially working:

* JSON
* PHP
* YAML

# Quick start

Assuming you installed this repo in `$HOME/Development/lsp`:

* For each of the servers you want, run the `install` script in that directory.
* Add the following to your `vimrc` (remove any that you didn't install):

```viml
let g:ycm_language_server = [
  \   {
  \     'name': 'yaml',
  \     'cmdline': [ 'node', expand( '$HOME/Development/lsp/yaml/node_modules/.bin/yaml-language-server' ), '--stdio' ],
  \     'filetypes': [ 'yaml' ],
  \   },
  \   {
  \     'name': 'php',
  \     'cmdline': [ 'php', expand( '$HOME/Development/lsp/php/vendor/bin/php-language-server.php' ) ],
  \     'filetypes': [ 'php' ],
  \   },
  \   {
  \     'name': 'json',
  \     'cmdline': [ 'node', expand( '$HOME/Development/lsp/json/node_modules/.bin/vscode-json-languageserver' ), '--stdio' ],
  \     'filetypes': [ 'json' ],
  \   },
  \   {
  \     'name': 'ruby',
  \     'cmdline': [ expand( '$HOME/Development/lsp/ruby/bin/solargraph' ), 'stdio' ],
  \     'filetypes': [ 'ruby' ],
  \   },
  \   { 'name': 'kotlin',
  \     'filetypes': [ 'kotlin' ], 
  \     'cmdline': [ expand( '$HOME/Development/lsp/kotlin/server/build/install/server/bin/server' ) ],
  \   },
  \   { 'name': 'd',
  \     'filetypes': [ 'd' ], 
  \     'cmdline': [ expand( '$HOME/Development/lsp/d/serve-d' ) ],
  \   },
  \   { 'name': 'vue',
  \     'filetypes': [ 'vue' ], 
  \     'cmdline': [ expand( '$HOME/Development/lsp/vue/node_modules/.bin/vls' ) ]
  \   },
  \   { 'name': 'docker',
  \     'filetypes': [ 'dockerfile' ], 
  \     'cmdline': [ expand( '$HOME/Development/lsp/docker/node_modules/.bin/docker-langserver' ), '--stdio' ]
  \   },
  \   { 'name': 'vim',
  \     'filetypes': [ 'vim' ],
  \     'cmdline': [ expand( '$HOME/Development/lsp/viml/node_modules/.bin/vim-language-server' ), '--stdio' ]
  \   },
  \ ]
```

* Adjust the directory as appropriate

# Ruby

You need to be running a version of ruby that the parser understands:
https://github.com/whitequark/parser#compatibility-with-ruby-mri

Recommend running in [rbenv][] for that:

```
$ rbenv shell 2.3.8
$ cd ruby
$ ./install
$ vim test/test.rb
```

# D

There is a number of external dependencies that you will want to install:

- `libphobos`/`liblphobos` - the D standard library
- `dmd` - the D compiler
- `dscanner` - at the very least responsible for diagnostics
- `dcd` - the D compiler daemon
- Potentially `dfmt` - `serve-d` seems to be able to format code even without it.
- `dub` - the D package manager

On top of that, you will want to configure the server, at least to let `serve-d`
know about your modules. The configuration is done through ycmd's extra confs
and the full list of `serve-d`'s configuration options can be found
[here][d-conf].

Note that the server executable on Windows is called `serve-d.exe`.

# Kotlin

For whatever reason, the server expects you to have maven in your `PATH` and,
just like `serve-d`, `kotlin-language-server` has its own [configuration][kt-conf].

The server executable is actually a shell script and the build process produces
`server` for Linux and `server.bat` for Windows.

**NOTICE**: YCM will regard the path of `.ycm_extra_conf.py` as root path of kotlin
project folder. So please make sure you put your `.ycm_extra_conf.py` at right place
(root of current project) to make it work properly.

# Known Issues

- `yaml` completer completions don't work because the server [bugs][yaml-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `json` completer completions don't work because the server [bugs][json-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `php` completer generally never works. It just seems broken.
- `kotlin` completer currently requires merging of [a pull request][kt-pr] into
  master.


[yaml-bug]: https://github.com/redhat-developer/yaml-language-server/issues/161
[json-bug]: https://github.com/vscode-langservers/vscode-json-languageserver-bin/issues/2
[rbenv]: https://github.com/rbenv/rbenv
[d-conf]: https://github.com/Pure-D/serve-d/blob/master/source/served/types.d#L64
[kt-conf]: https://github.com/fwcd/KotlinLanguageServer/blob/master/server/src/main/kotlin/org/javacs/kt/KotlinWorkspaceService.kt#L81
[kt-pr]: https://github.com/fwcd/KotlinLanguageServer/pull/120
