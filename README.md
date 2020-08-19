# Overview

This repo includes a simple way to install some language servers that might work
with YouCompleteMe (strictly ycmd). 

This repo comes with no warranty, and these engines are not officially supported
by YCM, though they should work for the most part.

# Languages Tested

Working:

* Angular
* Bash
* D
* Dart
* Dockerfile
* Groovy
* Kotlin
* Ruby
* Vue
* Vim (vimscript)
* Rust (with rust-analyzer)

Broken or partially working:

* JSON
* PHP
* YAML
* Lua

See also:

* [C-family with ccls](https://github.com/MaskRay/ccls/wiki/YouCompleteMe)

# Quick start

Assuming you installed this repo in `/path/to/this/directory`:

* For each of the servers you want, run the `install` script in that directory.
* Add the following to your `vimrc` (remove any that you didn't install):

```viml
let s:lsp = '/path/to/this/directory'
let g:ycm_language_server = [
  \   {
  \     'name': 'angular',
  \     'cmdline': [ 'node' ,
  \        expand( s:lsp . '/angular/node_modules/@angular/language-server' ),
  \        '--ngProbeLocations',
  \        expand( s:lsp . '/angular/node_modules/' ),
  \        '--tsProbeLocations',
  \        expand( s:lsp . '/angular/node_modules/' ),
  \        '--stdio' ],
  \     'filetypes': [ 'ts','html' ],
  \   },
  \   {
  \     'name': 'bash',
  \     'cmdline': [ 'node', expand( s:lsp . '/bash/node_modules/.bin/bash-language-server' ), 'start' ],
  \     'filetypes': [ 'sh', 'bash' ],
  \   },
  \   {
  \     'name': 'dart',
  \     'cmdline': [ 'dart', expand( s:lsp . '/dart/analysis_server.dart.snapshot' ), '--lsp' ],
  \     'filetypes': [ 'dart' ],
  \   },
  \   {
  \     'name': 'groovy',
  \     'cmdline': [ 'java', '-jar', expand( s:lsp . '/groovy/groovy-language-server/build/libs/groovy-language-server-all.jar' ) ],
  \     'filetypes': [ 'groovy' ]
  \   },
  \   {
  \     'name': 'yaml',
  \     'cmdline': [ 'node', expand( s:lsp . '/yaml/node_modules/.bin/yaml-language-server' ), '--stdio' ],
  \     'filetypes': [ 'yaml' ],
  \   },
  \   {
  \     'name': 'php',
  \     'cmdline': [ 'php', expand( s:lsp . '/php/vendor/bin/php-language-server.php' ) ],
  \     'filetypes': [ 'php' ],
  \   },
  \   {
  \     'name': 'json',
  \     'cmdline': [ 'node', expand( s:lsp . '/json/node_modules/.bin/vscode-json-languageserver' ), '--stdio' ],
  \     'filetypes': [ 'json' ],
  \   },
  \   {
  \     'name': 'ruby',
  \     'cmdline': [ expand( s:lsp . '/ruby/bin/solargraph' ), 'stdio' ],
  \     'filetypes': [ 'ruby' ],
  \   },
  \   {
  \     'name': 'kotlin',
  \     'filetypes': [ 'kotlin' ], 
  \     'cmdline': [ expand( s:lsp . '/kotlin/server/build/install/server/bin/server' ) ],
  \   },
  \   {
  \     'name': 'd',
  \     'filetypes': [ 'd' ], 
  \     'cmdline': [ expand( s:lsp . '/d/serve-d' ) ],
  \   },
  \   {
  \     'name': 'vue',
  \     'filetypes': [ 'vue' ], 
  \     'cmdline': [ expand( s:lsp . '/vue/node_modules/.bin/vls' ) ]
  \   },
  \   {
  \     'name': 'docker',
  \     'filetypes': [ 'dockerfile' ],
  \     'cmdline': [ expand( s:lsp . '/docker/node_modules/.bin/docker-langserver' ), '--stdio' ]
  \   },
  \   {
  \     'name': 'vim',
  \     'filetypes': [ 'vim' ],
  \     'cmdline': [ expand( s:lsp . '/viml/node_modules/.bin/vim-language-server' ), '--stdio' ]
  \   },
  \   {
  \     'name': 'scala',
  \     'filetypes': [ 'scala' ],
  \     'cmdline': [ 'metals-vim' ],
  \     'project_root_files': [ 'build.sbt' ]
  \   },
  \   {
  \     'name': 'purescript',
  \     'filetypes': [ 'purescript' ],
  \     'cmdline': [ expand( s:lsp . '/viml/node_modules/.bin/purescript-language-server' ), '--stdio' ]
  \   },
  \   {
  \     'name': 'fortran',
  \     'filetypes': [ 'fortran' ],
  \     'cmdline': [ 'fortls' ],
  \   },
  \   {
  \     'name': 'haskell',
  \     'filetypes': [ 'haskell', 'hs', 'lhs' ],
  \     'cmdline': [ 'hie-wrapper', '--lsp' ],
  \     'project_root_files': [ '.stack.yaml', 'cabal.config', 'package.yaml' ]
  \   },
  \   {
  \     'name': 'julia',
  \     'filetypes': [ 'julia' ],
  \     'project_root_files': [ 'Project.toml' ],
  \     'cmdline': <See note below>
  \   },
  \   {
  \     'name': 'lua',
  \     'filetypes': [ 'lua' ],
  \     'cmdline': [ expand( s:lsp . '/lua/lua-language-server/root/extension/server/bin/macOS/lua-language-server'),
  \                  expand( s:lsp . '/lua/lua-language-server/root/extension/server/main.lua' ) ]
  \   },
  \   {
  \     'name': 'rust',
  \     'filetypes': [ 'rust' ],
  \     'cmdline': [ expand( s:lsp .  '/rust/rust-analyzer/target/release/rust-analyzer' ) ],
  \     'project_root_files': [ 'Cargo.toml' ],
  \   },
  \ ]
```

* Adjust the directory as appropriate

* **NOTE**: YCM will regard the path of `.ycm_extra_conf.py` as root path of project folder.
So please make sure you put your `.ycm_extra_conf.py` at right place (root of current project)

# Configuration

The `g:ycm_language_server` option is used to tell YCM (strictly, ycmd) to use
its 'generic' language server completer. It's a list of dictionaries with the
following keys:

* 'name' (string): Name of the language server
* 'filetypes' (list): List of Vim filetypes to use this language server for
* 'cmdline' (list): List of words forming a command line to execute. Note:
  *must* be a list, even if it has only one element (such as `[ 'executable' ]`.
* 'project_root_files' (list, optional): List of filename to search for when
  trying to determine the 'root' of the project. THis is useful for languages or
  language servers which don't automatically detect the 'workspace' root.

For full documentation, please see the YouCompleteMe docs.

# Purescript

Ycmd currently doesn't support `showMessageRequest`, so users need to manually build their projects
on the command line before starting the server. To do this execute `pulp build` in the project root.

# Scala

Ycmd currently doesn't support `showMessageRequest`, so users need to "import build" manually.
Unlike purescript, for scala, this can be done in the editor by executing
`:YcmCompleter ExecuteCommand build-import`. For this operation to succeed `sbt` and `bloop`
need to be in the `$PATH`. `metals` also requires java 8.

For completions to work make sure the version of `metals` has [this bug fix][metals-pr].

# Haskell

Currently haskell-ide-engine always completes snippets, which trips up ycmd.
The [pull request][hie-pr] that fixed this bug has already been merged, but isn't
available in version 0.13.0.0. Until the next version of HIE compile its git master.

The HIE install instructions can be found [here][hie-install].

HIE also requires a `.ycm_extra_config.py` with the following content:

```python
def Settings(**kwargs):
  return { 'ls': { "languageServerHaskell": {} } }
```

# Fortran

The server causes a spurious error:

- `fortls` doesn't support `didChangeConfiguration`.

This error can be ignored, as they don't interfere with normal work of ycmd/fortls.

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

Make sure to put a `.ycm_extra_conf.py` file in the root of your project, otherwise
[the language server may fail][kt-issue].

# Julia

The command line for starting the server is:

```viml
let g:julia_cmdline = ['julia', '--startup-file=no', '--history-file=no', '-e', '
\       using LanguageServer;
\       using Pkg;
\       import StaticLint;
\       import SymbolServer;
\       env_path = dirname(Pkg.Types.Context().env.project_file);
\       debug = false;
\
\       server = LanguageServer.LanguageServerInstance(stdin, stdout, debug, env_path, "", Dict());
\       server.runlinter = true;
\       run(server);
\   ']
```

You can replace the first command line argument (`'julia'`) with an absolute
path, if `julia` isn't in your `$PATH`.
With the above list in your vimrc, you can set `'cmdline'` in
`g:ycm_language_server` to just `g:julia_cmdline`.

Julia server *does* support configuration via the extra conf, but it doesn't
seem to be documented anywhere.

# Lua

Uses [lua-language-server][].

Quick testing suggests that:

- It returns snippets even though YCM explicitly opted out, meaning completions
  don't work unless you use [Ben's Fork][puremourning-fork]
- It violates a number of other items of the protocol other than that such as
  missing mandatory fields.
- Signature help doesn't seem to work.

However, it looks like diagnostics and GoTo work.

The command line requeired depends on your OS:

* Windows: `/path/to/lua-language-server/bin/Windows/lua-language-server.exe`
* Linux: `/path/to/lua-language-server/bin/Linux/lua-language-server`
* macOS: `/path/to/lua-language-server/bin/macOS/lua-language-server`

There is one command line argument. It needs to be the absolute path to
`/path/to/lua-language-server/main.lua`.

The `install.py` for Lua downloads the pre-built visual studio code extension,
but you can build `lua-language-server` yourself easily if you have `ninja`
installed:

```
git clone https://github.com/sumneko/lua-language-server
cd lua-language-server
cd 3rd/luamake
ninja ninja/<your os>.ninja
cd ../../
./3rd/luamake/luamake rebuild
```

This will put the binaries in `bin/<your os>`.

# Rust (rust-analyzer)

YCM uses `rls` by default. In order to use `rust-analyzer` you must _not_ have
built YCM with `--rust-completer`. If you previously did, then you need to
remove the directory
`</path/to/>/YouCompleteMe/third_party/ycmd/third_party/rls`.

Building `rust-analyzer` requires `rustup` and the `rust` source code (see the
`rust-analyzer` docs for details, but in short:

* Install `rustup`
* `rustup update stable`
* `rustup default stable`
* `rustup component add rust-src`
* `rustup component add rustfmt`

Then you can enable rust with `./install.py --enable-rust`.

# Known Issues

- `yaml` completer completions don't work because the server [bugs][yaml-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `json` completer completions don't work because the server [bugs][json-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `php` completer generally never works. It just seems broken.
- `lua` - yet another completer that returns snippets even if client doesn't
  support them.

There is highly experimental (essentially unsupported) support for snippet
completions in [Ben's Fork][puremourning-fork] of YCM. For example, the 
following makes json work with that fork:

```viml
    \   {
    \     'name': 'json',
    \     'cmdline': [ 'node', s:lsp_dir . '/json/node_modules/.bin/vscode-json-languageserver', '--stdio' ],
    \     'filetypes': [ 'json' ],
    \     'capabilities': #{ textDocument: #{ completion: #{ completionItem: #{ snippetSupport: v:true } } } },
    \   },
```


[yaml-bug]: https://github.com/redhat-developer/yaml-language-server/issues/161
[json-bug]: https://github.com/vscode-langservers/vscode-json-languageserver-bin/issues/2
[rbenv]: https://github.com/rbenv/rbenv
[d-conf]: https://github.com/Pure-D/serve-d/blob/master/source/served/types.d#L64
[kt-conf]: https://github.com/fwcd/KotlinLanguageServer/blob/master/server/src/main/kotlin/org/javacs/kt/KotlinWorkspaceService.kt#L81
[kt-issue]: https://github.com/ycm-core/lsp-examples/issues/5
[hie-pr]: https://github.com/haskell/haskell-ide-engine/pull/1424
[hie-install]: https://github.com/haskell/haskell-ide-engine#installation
[metals-pr]: https://github.com/scalameta/metals/issues/1057
[lua-language-server]: https://marketplace.visualstudio.com/items?itemName=sumneko.lua
[puremourning-fork]: https://github.com/puremourning/YouCompleteMe
