<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 7</title>
        <style>
            .wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .main_content {
                width: 400px;
                padding: 20px;
                border: 1px solid #000;
                border-radius: 10px;
            }
            .question {
                font-weight: bold;
            } 
        </style>
    </head>
    <body>
        <h3>Завдання 7</h3>
        <div class="wrapper">
            <div class="main_content">
                <h1>Анкета оцінки якості ресторану</h1>
                <form action="task7.php" method="post">
                    <p class="question">Які аспекти вам сподобались</p>
                    <input type="checkbox" name="aspects[]" id="price" value="Ціни">
                    <label for="price">Ціни</label><br>
                    <input type="checkbox" name="aspects[]" id="food-and-beverages" value="Їжа та напої">
                    <label for="food-and-beverages">Їжа та напої</label><br>
                    <input type="checkbox" name="aspects[]" id="staff" value="Персонал">
                    <label for="staff">Персонал</label><br>
                    <input type="checkbox" name="aspects[]" id="interior" value="Інтер'єр">
                    <label for="interior">Інтер'єр</label><br>

                    <p class="question">Як ви оцінюєте якість обслуговування</p>
                    <select name="service-quality" id="service-quality">
                        <option value="Відмінно">Відмінно</option>
                        <option value="Добре">Добре</option>
                        <option value="Задовільно">Задовільно</option>
                        <option value="Погано">Погано</option>
                    </select><br>

                    <p class="question">Що б ви хотіли змінити</p>
                    <select name="changes[]" id="changes" multiple>
                        <option value="Меню">Меню</option>
                        <option value="Персонал">Персонал</option>
                        <option value="Інтер'єр">Інтер'єр</option>
                        <option value="Ціни">Ціни</option>
                    </select><br>

                    <p class="question">Загальне враження</p>
                    <input type="radio" name="impression" id="excellent" value="Відмінно">
                    <label for="excellent">Відмінно</label>
                    <input type="radio" name="impression" id="good" value="Добре">
                    <label for="good">Добре</label>
                    <input type="radio" name="impression" id="satisfactory" value="Задовільно">
                    <label for="satisfactory">Задовільно</label>
                    <input type="radio" name="impression" id="poor" value="Погано">
                    <label for="poor">Погано</label><br><br>

                    <input type="submit" value="Готово" name="Send">
                </form>
                <?php
                    if (isset($_POST['Send'])) {
                    // У випадку відсутності відповіді виводити відповідне повідомлення
                        if (!isset($_POST['aspects']) || !isset($_POST['service-quality']) || !isset($_POST['changes']) || !isset($_POST['impression'])) {
                            echo "Заповніть всі поля!";
                        }
                        else {
                            $aspects = $_POST['aspects'];
                            $service_quality = $_POST['service-quality'];
                            $changes = $_POST['changes'];
                            $impression = $_POST['impression'];
                            echo "<h2>Ваші відповіді:</h2>";
                            echo "<p>Аспекти, які вам сподобались: ";
                            foreach ($aspects as $aspect) {
                                echo "$aspect ";
                            }
                            echo "</p>";
                            echo "<p>Якість обслуговування: $service_quality</p>";
                            echo "<p>Що б ви хотіли змінити: ";
                            foreach ($changes as $change) {
                                echo "$change ";
                            }
                            echo "</p>";
                            echo "<p>Загальне враження: $impression</p>";
                        }
                    }
                ?>
            </div>
        </div>
        <h3 class='back'><a href='lab4.php'>Назад</a></h3>
    </body>
</html>