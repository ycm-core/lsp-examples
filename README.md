# Overview

This repo includes a simple way to install some language servers that might work
with YouCompleteMe (strictly ycmd). 

This repo comes with no warranty, and these engines are not officially supported
by YCM, though they should work for the most part.

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

# Known Issues

- `yaml` completer completions don't work because the server [bugs][yaml-bug]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `json` completer completions don't work because the server [bugs][json-bugs]
  always returns snippets, even though ycmd claims not to support them.
  Validation works though.
- `php` completer generally never works. It just seems broken.


[yaml-bug]: https://github.com/redhat-developer/yaml-language-server/issues/161
[json-bug]: https://github.com/vscode-langservers/vscode-json-languageserver-bin/issues/2
[rbenv]: https://github.com/rbenv/rbenv
