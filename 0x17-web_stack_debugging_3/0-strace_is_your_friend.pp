# Fixing Apache 500 Error

exec {
'Fix-wordpess':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
