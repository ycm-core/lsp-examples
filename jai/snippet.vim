let g:ycm_language_server += [
  \   {
  \     'name': 'jai_lsp',
  \     'cmdline': [ g:ycm_lsp_dir .. '/jai/jai_lsp/jai_lsp',
  \                  '-log_file', '/dev/stderr',
  \                  '-log_level', 'VERY_VERBOSE' ],
  \     'filetypes': [ 'jai' ],
  \   },
  \ ]
