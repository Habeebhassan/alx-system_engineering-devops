# Ensure that the directory '/var/www/html' exists with specific permissions and ownership

file { '/var/www/html':
  ensure => directory,
  mode   => '0755',
  owner  => 'www-data',
  group  => 'www-data',
}

# Ensure that the file '/var/www/html/.htaccess' exists with specific content, permissions, and ownership
file { '/var/www/html/.htaccess':
  ensure  => file,
  content => 'RewriteEngine On\nRewriteRule ^index\.html$ welcome.html',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

# Ensure that the 'apache2' service is running and enabled at boot time
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html', '/var/www/html/.htaccess'],
}
