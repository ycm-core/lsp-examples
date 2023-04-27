let g:ycm_language_server += [
  \   { 'name': 'MATLAB',
  \     'filetypes': [ 'matlab' ],
  \     'cmdline': [ 'node',
  \                   expand( g:ycm_lsp_dir . '/matlab/MATLAB-language-server/out/index.js' ),
  \                   '--stdio' ]
  \   },
  \ ]

