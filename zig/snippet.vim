let g:ycm_language_server += [
  \   { 'name': 'zig',
  \     'filetypes': [ 'zig' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/zls/zig-out/bin/zls' ) ],
  \   },
  \ ]
