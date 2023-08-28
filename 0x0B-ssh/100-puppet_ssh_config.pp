# client configuration configured to use the private key
# configured to refuse to authenticate using a password

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => "
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  "
}
