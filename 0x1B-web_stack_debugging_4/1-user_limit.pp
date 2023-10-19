# Set limits for the holberton user
user { 'holberton':
  ensure => present,
}

# Increase file descriptor limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton soft nofile 65535\nholberton hard nofile 65535\n",
}

# Apply changes to the system
exec { 'reload_limits':
  command     => 'sysctl -p',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.d/holberton.conf'],
}

# Allow the holberton user to access the desired file
file { '/path/to/your/file':
  ensure  => file,
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0644',
  content => "Content of your file goes here\n",
}
