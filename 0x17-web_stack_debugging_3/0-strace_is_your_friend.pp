# web debugging
file { '/var/www/html/wp-settings.php':
  ensure => file,
  source => 'puppet:///modules/wordpress/wp-settings.php',
  notify => Exec['fix-wordpress'],
}

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
