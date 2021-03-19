let g:ycm_language_server += [
  \   {
  \     'name': 'python',
  \     'cmdline': [ 'node', expand( g:ycm_lsp_dir . '/python/node_modules/.bin/pyright-langserver' ), '--stdio' ],
  \     'filetypes': [ 'python' ],
  \   },
  \ ]
