let g:ycm_language_server += [
  \   { 'name': 'docker',
  \     'filetypes': [ 'dockerfile', 'Dockerfile' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/docker/node_modules/.bin/docker-langserver' ), '--stdio' ]
  \   },
  \ ]
