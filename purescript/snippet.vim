let g:ycm_language_server += [
  \   { 'name': 'purescript',
  \     'filetypes': [ 'purescript' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/purescript/node_modules/.bin/purescript-language-server' ), '--stdio' ]
  \   },
  \ ]
