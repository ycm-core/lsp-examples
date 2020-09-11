let g:ycm_language_server += [
  \   { 'name': 'docker',
  \     'filetypes': [ 'dockerfile' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/docker/node_modules/.bin/docker-langserver' ), '--stdio' ]
  \   },
  \ ]
