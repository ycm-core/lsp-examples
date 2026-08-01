let g:ycm_language_server += [
  \   {
  \     'name': 'jsonnet',
  \     'cmdline': [
  \       expand( g:ycm_lsp_dir ) . '/jsonnet/bin/jsonnet-language-server'
  \     ],
  \     'filetypes': [ 'jsonnet' ],
  \     'project_root_files': [ 'tkrc.yaml', 'jsonnetfile.json' ],
  \   },
  \ ]

