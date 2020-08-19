let g:ycm_language_server += [
  \   { 'name': 'haskell',
  \     'filetypes': [ 'haskell', 'hs', 'lhs' ],
  \     'cmdline': [ 'hie-wrapper', '--lsp' ],
  \     'project_root_files': [ '.stack.yaml', 'cabal.config', 'package.yaml' ]
  \   },
  \ ]
