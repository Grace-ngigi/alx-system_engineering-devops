class { 'nginx':
  worker_processes => 'auto',
  worker_connections => 4096,
}

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "* soft nofile 65535\n* hard nofile 65535\n",
}

file { '/etc/sysctl.conf':
  ensure  => file,
  content => "net.core.somaxconn = 65535\nnet.ipv4.tcp_max_syn_backlog = 65535\n",
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}
