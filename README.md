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
   * [Python (e.g. pyright)](#python-eg-pyright)
   * [Ruby](#ruby)
   * [D](#d)
   * [Godot](#godot)
   * [Kotlin](#kotlin)
   * [Julia](#julia)
   * [Lua](#lua)
   * [Zig](#zig)
   * [CSS](#css)
   * [PHP](#php)
   * [Crystal](#crystal)
   * [Astro](#astro)
   * [Postgres](#postgres)
   * [Erlang](#erlang)
   * [Known Issues](#known-issues)

<!-- Added by: ben, at: Tue 21 Feb 2023 09:01:14 GMT -->

<!--te-->

# Languages Tested

Working:

* Angular
* Bash
* CSS
* Cmake
* Crystal
* D
* Dart
* Dockerfile
* Godot (gdscript)
* Groovy
* Jai
* Jsonnet (see jsonnet/README.md)
* Kotlin
* PHP
* Python (pyright)
* Racket
* Ruby
* Vala
* Vim (vimscript)
* Vue
* WASM (WAT)
* Zig

Broken or partially working:

* JSON
* Lua
* YAML

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

# Python (e.g. pyright)

If configuring a language server for Python, this will completely disable the
built-in Jedi completer in YCM.

## Pyright

Example extra conf (actually for ycmd itself):

```python
import sys.path as p

DIR_OF_THIS_SCRIPT = p.abspath( p.dirname( __file__ ) )
DIR_OF_THIRD_PARTY = p.join( DIR_OF_THIS_SCRIPT, 'third_party' )
DIR_OF_WATCHDOG_DEPS = p.join( DIR_OF_THIRD_PARTY, 'watchdog_deps' )

def Settings( **kwargs ):
  if language == 'python':
    return {
      'ls': {
        'python': {
          'analysis': {
            'extraPaths': [
              p.join( DIR_OF_THIS_SCRIPT ),
              p.join( DIR_OF_THIRD_PARTY, 'bottle' ),
              p.join( DIR_OF_THIRD_PARTY, 'regex-build' ),
              p.join( DIR_OF_THIRD_PARTY, 'frozendict' ),
              p.join( DIR_OF_THIRD_PARTY, 'jedi_deps', 'jedi' ),
              p.join( DIR_OF_THIRD_PARTY, 'jedi_deps', 'parso' ),
              p.join( DIR_OF_WATCHDOG_DEPS, 'watchdog', 'build', 'lib3' ),
              p.join( DIR_OF_WATCHDOG_DEPS, 'pathtools' ),
              p.join( DIR_OF_THIRD_PARTY, 'waitress' )
            ],
            'useLibraryCodeForTypes': True
          }
        }
      }
    }
```

# Racket

You need to have racket installed so you can use `raco` to install
the required packages for the language server.
You can install racket through the [racket website](https://download.racket-lang.org/) or your package manager.

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

## Kotlin - JetBrains

JetBrains Kotlin Language Server Protocol (LSP) implementation based on IntelliJ

https://github.com/Kotlin/kotlin-lsp.

See [jetbrains-kotlin/README.md](jetbrains-kotlin/README.md) for more
information.

### Limitations

Uses pull-style diagnostics, which YCM doesn't currently support.

## Kotlin - fwcd

NOTE: I have had little success with this, but the JetBrains one seems to work
well.

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

# Zig

Uses [zls](https://github.com/zigtools/zls)

For this to work sometimes, one needs to run the zls executable to create a user/global config json file
by running the executable in /zig/zls/zig-out/bin/zls after running the install.py.
[NOTE] if your workspace directory has a zls.json file, it should would also work.

# CSS

Uses [css](https://github.com/hrsh7th/vscode-langservers-extracted)

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

# Astro

In addition to defining `g:ycm_language_server` block as shown in
[`astro/snippet.vim`](astro/snippet.vim) this LSP requires `.ycm_extra_conf.py`
to pass Language Server `initializationOptions` pointing to a directory
containing either `typescript.js` or `tsserverlibrary.js` file, such as
`node_modules/typescript/lib`, via `typescript.tsdk` key/value address, eg.

```python
import os

def Settings( **kwargs ):
    current_directory = os.path.abspath(os.path.curdir)
    if kwargs[ 'language' ] == 'astro':
        configs = {
            'ls': {
                'typescript': {
                    'tsdk':  f"{current_directory}/node_modules/typescript/lib"
                },
            },
        }

        return configs
```

...  Authors of Astro Language Server recommend installing `prettier` plugins
too, so adding the following to your `npm init` rituals may be a good idea;

```bash
npm install --save-dev typescript prettier prettier-plugin-astro @astrojs/ts-plugin
```

Finally, hopefully for now, adding the `@astrojs/ts-plugin` to your project's
`tsconfig.json` may be necessary to enable all features of Astro LS

```json
{
  "compilerOptions": {
    "plugins": [
      {
        "name": "@astrojs/ts-plugin"
      }
    ]
  }
}
```

# Postgres

Within the root of a project running `postgrestools init` is recommend by
[Configuration](https://pgtools.dev/#configuration) documentation to create a
`postgrestools.jsonc` file, then editing that file for your database setup
seems required to make full use of this Language Server's tooling.

# Erlang

Be sure to have satisfied [minimum requirements](https://github.com/erlang-ls/erlang_ls?tab=readme-ov-file#minimum-requirements), and checking [configuration](https://erlang-ls.github.io/configuration/) documentation may be prudent.

<details><summary>Minimum Requirements install hints</summary>
**Arch (BTW™)**

```bash
sudo pacman -S erlang &&
  yay -S rebar3
```
</details>

> :warning: doc-comments, as of 2025-02-11, are only extracted correctly when a project includes `{project_plugins, [rebar3_ex_doc]}.`, within its `rebar.conf` file.  Check [`erlang-ls/erlang_ls` -- Issue `1578`](https://github.com/erlang-ls/erlang_ls/issues/1578) for the full scoop.

# Jai

This is using [Jails](https://github.comSogoCZE/Jails), which is very much
"work in progress", so many things aren't fully working yet, but it's easy
enough to set up.

You may need to create a `jails.json` in your project root to tell Jails where
to find modules.

Example `jails.json`:

```json
{
    "workspaces": [
        {
            "entry": "/foo/main.jai",
            "local_modules": "/modules"
        }
    ]
}
```

# Vala

Installing [vala-language-server](https://github.com/vala-lang/vala-language-server) from
source automatically takes a long time
and would be difficult to get right generically.

Please install `vala-language-server` through your system package manager
before enabling vala support through YCM.

For formatting support you will need `uncrustify` as well.

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
