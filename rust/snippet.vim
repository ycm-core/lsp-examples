let g:ycm_language_server += [
  \   { 'name': 'rust',
  \     'filetypes': [ 'rust' ],
  \     'cmdline': [ expand( g:ycm_lsp_dir .  '/rust/rust-analyzer/target/release/rust-analyzer' ) ],
  \     'project_root_files': [ 'Cargo.toml' ],
  \   },
  \ ]
