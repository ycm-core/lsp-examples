let g:ycm_language_server += [
  \   {
  \     'name': 'erlang',
  \     'filetypes': [ 'erlang' ],
  \     'cmdline': [  expand( g:ycm_lsp_dir . '/erlang/erlang_ls/_build/default/bin/erlang_ls' ), '--transport', 'stdio' ],
  \     'project_root_files': [ 'erlang_ls.config', 'erlang_ls.yaml' ]
  \   },
  \ ]
