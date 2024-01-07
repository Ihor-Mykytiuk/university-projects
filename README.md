# DB_Course_Project

Микитюк Ігор

ІПЗ-23

Проектування та розробка бази даних «Облік мережевого і комп’ютерного устаткування»

Теоретична тема: "Класифікація та характеристика баз даних. Стандарти БД"

## Опис атрибутів таблиці

| **Таблиця Buildings**         |                  |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| BuildingID                    | int              | Унікальний ідентифікатор будівлі. |
| BuildingName                  | varchar          | Назва будівлі.    |
| Address                       | varchar          | Адреса будівлі.   |

| **Таблиця ClassRooms**        |                  |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| ClassRoomID                   | int              | Унікальний ідентифікатор класу (аудиторії). |
| RoomNumber                    | int              | Номер класу (аудиторії). |
| BuildingID                    | int              | Зовнішній ключ, пов'язаний із BuildingID у таблиці Buildings. |

| **Таблиця Computers**         |                  |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| ComputerID                    | int              | Унікальний ідентифікатор комп'ютера. |
| SerialNumber                  | varchar          | Серійний номер комп'ютера. |
| CharacteristicID              | int              | Зовнішній ключ, пов'язаний із CharacteristicID у таблиці ComputerCharacteristics. |
| PurchaseDate                  | date             | Дата придбання комп'ютера. |
| RoomID                        | int              | Зовнішній ключ, пов'язаний із RoomID у таблиці ClassRooms. |

| **Таблиця NetworkEquipment**  |                  |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| NetworkEquipmentID            | int              | Унікальний ідентифікатор мережевого обладнання. |
| SerialNumber                  | varchar          | Серійний номер мережевого обладнання. |
| BuildingID                    | int              | Зовнішній ключ, пов'язаний із BuildingID у таблиці Buildings. |
| DeviceTypeID                  | int              | Зовнішній ключ, пов'язаний із DeviceTypeID у таблиці DeviceTypes. |
| Manufacturer                  | varchar          | Виробник мережевого обладнання. |
| Model                         | varchar          | Модель мережевого обладнання. |

| **Таблиця DeviceTypes**       |                  |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| DeviceTypeID                  | int              | Унікальний ідентифікатор типу пристрою. |
| TypeName                      | varchar          | Назва типу пристрою. |
| Description                   | varchar          | Опис типу пристрою. |

| **Таблиця ComputerCharacteristics** |            |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| CharacteristicID              | int              | Унікальний ідентифікатор характеристик комп'ютера. |
| Memory                        | varchar          | Обсяг пам'яті комп'ютера. |
| RAM                           | varchar          | Оперативна пам'ять комп'ютера. |
| CPU                           | varchar          | Процесор комп'ютера. |
| VideoCard                     | varchar          | Відеокарта комп'ютера. |

| **Таблиця Peripherals**       |                  |                   |
|-------------------------------|------------------|-------------------|
| **Стовпець**                  | **Тип даних**    | **Опис**          |
| PeripheralID                  | varchar          | Унікальний ідентифікатор периферійного пристрою. |
| Type                          | varchar          | Тип периферійного пристрою. |
| Brand                         | varchar          | Бренд периферійного пристрою. |
| Model                         | varchar          | Модель периферійного пристрою. |
| ComputerID                    | int              | Зовнішній ключ, пов'язаний із ComputerID у таблиці Computers. |

## Тестові запити

1. Виведення кількості комп'ютерів у 320 аудиторії Центрального корпусу

    ```sql
    SELECT b.BuildingName, cr.RoomNumber, COUNT(*) AS NumberOfComputers
    FROM Computers c
    JOIN ClassRooms cr ON c.RoomID = cr.ClassRoomID
    JOIN Buildings b ON cr.BuildingID = b.BuildingID
    WHERE cr.RoomNumber = 320 AND b.BuildingName = 'Центральний корпус'
    GROUP BY b.BuildingName, cr.RoomNumber;
    ```

2. Виведення інформації про комп'ютери та їхню периферію, розташовану в Гуманітарному корпусі університету.

    ```sql
    SELECT c.SerialNumber, p.Type, p.Brand, p.Model
    FROM Computers c
    JOIN ClassRooms cr ON c.RoomID = cr.ClassRoomID
    JOIN Buildings b ON cr.BuildingID = b.BuildingID
    JOIN Peripherals p ON c.ComputerID = p.ComputerID
    WHERE b.BuildingName = 'Гуманітарний корпус';
    ```

3. Виведення інформації про комп'ютери, в яких встановлена відеокарта виробника Nvidia.

    ```sql
    SELECT c.SerialNumber, cc.VideoCard
    FROM Computers c
    JOIN ComputerCharacteristics cc ON c.CharacteristicID = cc.CharacteristicID
    WHERE cc.VideoCard LIKE 'NVIDIA%';
    ```

4. Отримання інформації про мережеве обладнання університету, включаючи його розташування у корпусах, серійний номер, тип та модель.

    ```sql
    SELECT b.BuildingName, ne.SerialNumber, dt.TypeName, ne.Model
    FROM NetworkEquipment ne
    JOIN Buildings b ON ne.BuildingID = b.BuildingID
    JOIN DeviceTypes dt ON ne.DeviceTypeID = dt.DeviceTypeID;
    ```

5. Виведення інформації про придбані до 2022 року комп'ютери, включаючи характеристику. Відсортовано за зростанням дати придбання.

    ```sql
    SELECT с.SerialNumber, с.PurchaseDate, сс.Memory,
    сс.RAM,сс.CPU, сс.VideoCard
    FROM Computers с
    JOIN ComputerCharacteristics сс ON с.CharacteristicID = сс.CharacteristicID
    WHERE с.PurchaseDate < '2022-01-01'
    ORDER BY с.PurchaseDate DESC;
    ```
