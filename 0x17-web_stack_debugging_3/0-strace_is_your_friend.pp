# Fix Apache 500 error

exec { 'Fix Amazon go':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
