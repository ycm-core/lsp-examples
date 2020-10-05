let g:ycm_language_server += [
  \   {
  \     'name': 'php',
  \     'cmdline': [ 'php', '-d', 'memory_limt=1024M', g:ycm_lsp_dir . '/php/serenata/bin/console', '--uri=tcp://127.0.0.1:11111' ],
  \     'filetypes': [ 'php' ],
  \     'port': 11111
  \   },
  \ ]
