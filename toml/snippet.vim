let g:ycm_language_server += [
  \   {
  \     'name': 'tombi',
  \     'cmdline': [
  \       expand( g:ycm_lsp_dir ) . '/toml/node_modules/.bin/tombi',
  \       'lsp'
  \     ],
  \     'filetypes': [ 'toml' ],
  \     'project_root_files': [ 'Cargo.toml', 'pyproject.toml', '.git' ],
  \     'capabilities': { 'textDocument': { 'completion': { 'completionItem': { 'snippetSupport': v:true } } } },
  \   },
  \ ]

