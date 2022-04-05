<?php
    $name = $_POST['name'];
	$phone = $_POST['phone'];
    $email = $_POST['email'];
    $text = $_POST['text'];
    //создание сообщения

	$to = "zivilsk@mail.ru";
	$date = date ("d.m.Y"); 
	$time = date ("h:i");
	$from = $email;
	$subject = "Заявка c сайта";
	//доп информация в сообщении

	
	$msg="
    ФИО: $name /n
    Телефон: $phone /n
    Почта: $email /n
    Текст: $text"; 	
	mail($to, $subject, $msg, "From: $from ");
	//отправка сообщения

?>

<p>Ваша заявка отправлена! Ожидайте обратной связи.</p>