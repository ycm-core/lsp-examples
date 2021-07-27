let g:ycm_language_server += [
  \   {
  \     'name': 'php',
  \     'cmdline': [ 'php', '-d', 'memory_limt=1024M', g:ycm_lsp_dir . '/php/phpactor/bin/phpactor', 'language-server' ],
  \     'filetypes': [ 'php' ],
  \   },
  \ ]
