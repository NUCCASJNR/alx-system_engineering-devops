# Fixes bad `phpp` extensions to `php`

exec { 'fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
