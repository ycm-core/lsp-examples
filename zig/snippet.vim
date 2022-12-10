let g:ycm_language_server += [
  \   { 'name': 'zls',
  \     'filetypes': [ 'zig' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir . '/zig/zls/zig-out/bin/zls' ) ],
  \   },
  \ ]
