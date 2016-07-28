<?php

require_once __DIR__ . '/raven-php/lib/Raven/Autoloader.php';

Raven_Autoloader::register();

$dsn = 'http://8818e066631e49aab4feaa0e795aba1c:ad9111625cf04118b583ec9994178aeb@sentry.demo.com/4';

$options = array(
    'tags' => array(
        'php_version' => phpversion(),
    ),
    'trace' => false,
);

$pattern_content = '^\[([^]]+)] PHP ([^:]+):\s+(.+)';

$parrern_level = implode('|', array(
    'debug',
    'info',
    'warning',
    'error',
    'fatal',
));
//$file  = 'log.txt';//要写入文件的文件名（可以是任意文件名），如果文件不存在，将会创建一个
//$content = "第一次写入的内容\n";
 
//if($f = file_put_contents($file, $content,FILE_APPEND)){
//    // 这个函数支持版本(PHP 5) 
//    echo "写入成功。<br />";
//}

$client = new Raven_Client($dsn, $options);
echo('begin');
while (($line = fgets(STDIN)) !== false) {
//    if (!preg_match("/{$pattern_content}/", $line, $match)) {
//       continue;
//    }

#    echo($line);
#    list($line, $timestamp, $level, $message) = $match;

#    $timestamp = gmdate('Y-m-d\TH:i:s\Z', strtotime($timestamp));

#    preg_match("/{$parrern_level}/i", $level, $match);

#    $level = isset($match[0]) ? $match[0] : 'error';
    
    $message = 'this is test msg';
    $level = 'error';
    $timestamp = '2016-07-08 10:10:10';
    $client->captureMessage($message, array(), array(
        'timestamp' => $timestamp,
        'level' => $level,
    ));
}

?>
