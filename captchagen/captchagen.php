<?php

require __DIR__ . '/vendor/autoload.php';

use Gregwar\Captcha\CaptchaBuilder;
use Gregwar\Captcha\PhraseBuilder;

$phraseBuilder = new PhraseBuilder(4);

$pass = fopen('captchas/pass.txt', 'w');

for ($i = 0; $i < $argv[1]; $i++) {
	$captchaBuilder = new CaptchaBuilder(null, $phraseBuilder);
	$captchaBuilder
		->setDistortion(false)
		->setMaxBehindLines(rand(0, 1))
		->setMaxFrontLines(rand(0, 1))
		->build()
		->save('captchas/' . $i . '.jpg');
	fwrite($pass, $captchaBuilder->getPhrase());
    fwrite($pass, ' ');
}

fclose($pass);