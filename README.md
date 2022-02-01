# Overview

This repo includes a simple way to install some language servers that might work
with YouCompleteMe (strictly ycmd). 

This repo comes with no warranty, and these engines are not officially supported
by YCM, though they should work for the most part.

<!--ts-->
 * [Overview](#overview)
 * [Languages Tested](#languages-tested)
 * [Quick start](#quick-start)
 * [Configuration](#configuration)
 * [Purescript](#purescript)
 * [Scala](#scala)
 * [Haskell](#haskell)
 * [Fortran](#fortran)
 * [Ruby](#ruby)
 * [D](#d)
 * [Godot](#godot)
 * [Kotlin](#kotlin)
 * [Julia](#julia)
 * [Lua](#lua)
 * [Known Issues](#known-issues)

<!-- Added by: ben, at: Sun 20 Sep 2020 13:24:56 BST -->

<!--te-->

# Languages Tested

Working:

* Angular
* Bash
* Cmake
* Crystal
* D
* Dart
* Dockerfile
* Godot (gdscript)
* Groovy
* Kotlin
* PHP
* Ruby
* Vim (vimscript)
* Vue

Broken or partially working:

* JSON
* YAML
* Lua

See also:

* [C-family with ccls](https://github.com/MaskRay/ccls/wiki/YouCompleteMe)

# Quick start

Assuming you installed this repo in `/path/to/this/directory`:

* Decide which languages you want. Each language is a directory in this repo.
* Run `python3 ./install.py --enable-LANG1 --enable-LANG2 ...`.
  Replace LANG1/LANG2 etc. with the language dirs. e.g. `./install.py
  --enable-dart --enable-bash`. You can also use `--all` and `--disable-LANG`.
* Add the line to your vimrc that it tells you to, this will be similar to:

```viml
source /path/to/this/directory/vimrc.generated
```

* Optionally: edit `vimrc.generated` to customise `g:ycm_language_server`

* **NOTE**: YCM will regard the path of `.ycm_extra_conf.py` as root path of
  project folder.  So please make sure you put your `.ycm_extra_conf.py` at
  right place (root of current project)

# Configuration

The `g:ycm_language_server` option is used to tell YCM (strictly, ycmd) to use
its 'generic' language server completer. It's a list of dictionaries with the
following keys:

* 'name' (string): Name of the language server
* 'filetypes' (list): List of Vim filetypes to use this language server for
* 'cmdline' (list): List of words forming a command line to execute. Note:
  *must* be a list, even if it has only one element (such as `[ 'executable' ]`.
  If not supplied, no server is started and a port must be supplied.
* 'port' (number): A TCP port on localhost to connect to if stdio is not
  possible.
* 'project_root_files' (list, optional): List of filename to search for when
  trying to determine the 'root' of the project. THis is useful for languages or
  language servers which don't automatically detect the 'workspace' root.

For full documentation, please see the YouCompleteMe docs.

# Purescript

Ycmd currently doesn't support `showMessageRequest`, so users need to manually
build their projects on the command line before starting the server. To do this
execute `pulp build` in the project root.

# Scala

Ycmd currently doesn't support `showMessageRequest`, so users need to "import
build" manually.  Unlike purescript, for scala, this can be done in the editor
by executing `:YcmCompleter ExecuteCommand build-import`. For this operation to
succeed `sbt` and `bloop` need to be in the `$PATH`. `metals` also requires java
8.

For completions to work make sure the version of `metals` has [this bug fix][metals-pr].

# Haskell

haskell-ide-engine [is not actively being developed anymore][hie-not-developing], in
favour of [haskell-language-server][haskell-language-server] ([installation
instructions][hls-install]).


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

# Godot

Godot must be running and you must go to `Project -> Project Settings -> Global`
and set `Language Server` to `On`. At least since Godot 3.4, `Language Server`
options are under `Editor Settings` and `On` by default.

If Godot is closed or restarted, you might need to force YCM to reconnect (this
isn't automatic). Use `:YcmCompleter RestartServer` to reconnect.

You can check the status of the connection with `:YcmDebugInfo`.

Recommend [vim-godot](https://github.com/habamax/vim-godot) for syntax, etc.
(don't believe the hype about using _other_ completion systems though, of
course).

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

# PHP

Uses [phpactor](https://phpactor.readthedocs.io/en/master/index.html).

# Crystal

Uses [Crystalline](https://github.com/elbywan/crystalline) as an LSP server and
[vim-crystal](https://github.com/vim-crystal/vim-crystal.git) to determine file
type.

Keep in mind, that Crystalline version **must** match crystal version (see
details on crystalline page).

The configuration is pretty straightforward. Add this to your .vimrc:
```viml
let g:ycm_language_server =
  \ [
  \   {
  \     'name': 'crystal',
  \     'cmdline': [ 'crystalline'],
  \     'project_root_files' : [ 'shard.yml' ],
  \     'filetypes': [ 'crystal' ]
  \   }
  \ ]
```
Place crystalline in the path (i.e. /usr/local/bin) or use absolute path
in the example above..

# Known Issues

- `yaml` completer completions don't work because the server [bugs][yaml-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `json` completer completions don't work because the server [bugs][json-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
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
[hie-not-developing]: https://stackoverflow.com/questions/64087188/what-is-the-current-situation-for-using-vim-as-ide-for-haskell-on-archlinux/
[haskell-language-server]: https://github.com/haskell/haskell-language-server
[hls-install]: https://github.com/haskell/haskell-language-server#installation
