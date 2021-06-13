let g:ycm_language_server =
  \ [
  \   {
  \     'name': 'crystal',
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/crystal/bin/crystalline' ) ],
  \     'project_root_files' : [ 'shard.yml' ],
  \     'filetypes': [ 'crystal' ]
  \   }
  \ ]
