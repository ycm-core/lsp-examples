let g:ycm_language_server += [
  \   { 'name': 'vue',
  \     'filetypes': [ 'vue' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/vue/node_modules/.bin/vls' ) ]
  \   },
  \ ]
