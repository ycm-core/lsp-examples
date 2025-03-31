let g:ycm_language_server += [
  \   {
  \     'name': 'postgres',
  \     'filetypes': [ 'sql' ],
  \     'cmdline': [  expand( g:ycm_lsp_dir . '/postgres/node_modules/.bin/postgrestools' ), 'lsp-proxy' ],
  \     'project_root_files': [ 'postgrestools.jsonc' ]
  \   },
  \ ]
