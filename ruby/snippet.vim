let g:ycm_language_server += [
  \   {
  \     'name': 'ruby',
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/ruby/bin/solargraph' ), 'stdio' ],
  \     'filetypes': [ 'ruby' ],
  \   },
  \ ]
