let g:ycm_language_server += [
  \   {
  \     'name': 'systemd-lsp',
  \     'filetypes': [ 'systemd' ],
  \     'cmdline': [  expand( g:ycm_lsp_dir . '/systemd/systemd-lsp/target/release/systemd-lsp' ) ],
  \   },
  \ ]
