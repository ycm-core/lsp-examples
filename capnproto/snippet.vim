let g:ycm_language_server += [
  \   {
  \     'name': 'capnproto',
  \     'cmdline': [
  \       expand( g:ycm_lsp_dir ) . '/capnproto/root/bin/capnprotols',
  \     ],
  \     'filetypes': [ 'capnp' ],
  \   },
  \ ]

