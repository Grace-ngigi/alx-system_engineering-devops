# reducing the amount of Nginx server failed requests to 0.

# Increase the limit of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx service
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
