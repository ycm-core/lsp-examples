let g:ycm_language_server += [
  \   {
  \     'name': 'php',
  \     'cmdline': [ 'php', expand( g:ycm_lsp_dir . '/php/vendor/bin/php-language-server.php' ) ],
  \     'filetypes': [ 'php' ],
  \   },
  \ ]
