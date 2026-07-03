<?php
function create_table2($data, $border=1, $cellpadding=4, $cellspacing=4)
{
	echo "<h4> Результат виклику функції create_table2: </h4> border=$border";
	echo "<table border=$border  cellpadding=$cellpadding cellspacing=$cellspacing>\n";
	reset($data); //    встановлює покажчик масиву на його початок
	$value=current($data);//current повертає поточний елемент масиву
	while($value)
	{
		echo "<tr><td>$value</td></tr>\n";
		$value = next($data);
		//next - переміщують показник на елемент вперед на один елемент; 
		//next – спочатку змінює покажчик, потім – повертає значення, each–навпаки;
	}
	echo '</table>';
	echo"<div>Кількість параметрів:". func_num_args()."<br />";
	//Функція func_num_args() визначає, скільки аргументів було передано функції користувача
	$args = func_get_args();
	//func_get_args() повертає масив, який містить ці аргументи
	foreach ($args as $arg)
		echo $arg."<br/>";
	echo "</div>";
}

// Функція для завдання 2
function generate_array($a) {
	$arr = array();
	for($i=0; $i<10; $i++) {
		$arr[$i] = mt_rand(1, $a + 10);
		echo "arr[$i] = ".$arr[$i]."<br>";
	}
	$min_value = min($arr);
	$max_value = max($arr);
	$avg_value = array_sum($arr)/count($arr);
	// Індекси та значення мінімального, максимального та середнього елементів масиву
	echo "Мінімальний елемент масиву: arr[".array_search($min_value, $arr)."] = $min_value<br>"; //array_search повертає ключ для значення
	echo "Максимальний елемент масиву: arr[".array_search($max_value, $arr)."] = $max_value<br>"; 
	echo "Середнє арифметичне елементів масиву: $avg_value<br>";
}

// Функція для завдання 3
function elements_and_squares($arr) {
	foreach ($arr as $elem) {
		echo "<div>$elem<sup>2</sup> = ".($elem*$elem)."</div><br>"; // Використовуємо тег <sup> для відображення верхнього індексу
	}
}

// Функція для завдання 5.1
function print_array($arr) {
	echo "<div>Заданий масив чисел разом із індексами в заданому порядку:<br>";
	foreach ($arr as $key => $value) {
		echo "arr[$key] = $value<br>";
	}
	echo "</div>";
	echo "<div>Заданий масив чисел разом із індексами в оберненому порядку:<br>";
	$arr = array_reverse($arr);
	foreach ($arr as $key => $value) {
		echo "arr[$key] = $value<br>";
	}
	echo "</div>";
}

// Функція для завдання 5.2
function print_table($arr) {
	// Виведення двовимірного масиву у вигляді таблиці
	echo "<table border='1'>";
	foreach ($arr as $row) {
		echo "<tr>";
		foreach ($row as $elem) {
			echo "<td>$elem</td>";
		}
		echo "</tr>";
	}
	echo "</table>";

	// Формування двох масивів: 1 - мінімальні значення рядків, 2 - числа, які знаходяться в останньому стовпці
	$min_values = array();
	$last_column = array();
	foreach ($arr as $row) {
		$min_values[] = min($row);
		$last_column[] = end($row);
	}
	echo "<div>Мінімальні значення рядків вхідного масиву: ";
	foreach ($min_values as $value) {
		echo "$value ";
	}
	echo "</div>";
	echo "<div>Числа, які знаходяться в останньому стовпці: ";
	foreach ($last_column as $value) {
		echo "$value ";
	}
	echo "</div>";
}
// Функція для завдання 6
function generate_array2($N) {
	// Елементи масиву - перші N натуральних чисел, піднесені до квадрату
	$arr = array();
	for ($i = 1; $i <= $N; $i++) {
		$arr[$i] = $i * $i;
	}
	echo "<div>Масив, елементами якого є перші $N натуральних чисел, піднесені до квадрату і відповідні індекси:<br>";
	foreach ($arr as $key => $value) {
		echo "arr[$key] = $value<br>";
	}
	echo "</div>";
}
?>
