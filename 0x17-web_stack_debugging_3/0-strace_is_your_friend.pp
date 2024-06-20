file { '/var/www/html':
  ensure => directory,
  mode   => '0755',
  owner  => 'www-data',
  group  => 'www-data',
}

file { '/var/www/html/.htaccess':
  ensure  => file,
  content => 'RewriteEngine On\nRewriteRule ^index\.html$ welcome.html',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html', '/var/www/html/.htaccess'],
}
