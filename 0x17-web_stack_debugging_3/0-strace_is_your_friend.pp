# Fixing Apache 500 Error

exec { 'fix-wordpess':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:bin/'
}
