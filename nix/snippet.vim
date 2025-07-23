let g:ycm_language_server += [
  \   {
  \     'name': 'nix',
  \     'filetypes': [ 'nix' ],
  \     'cmdline': [  expand( g:ycm_lsp_dir . '/nix/nil/target/release/nil' ), '--stdio' ],
  \     'project_root_files': [ 'flake.nix' ]
  \   },
  \ ]
