SELECT model,
       (LEN(REPLACE(model, '1', '**')) - LEN(model)) * 1
       + (LEN(REPLACE(model, '2', '**')) - LEN(model)) * 2
       + (LEN(REPLACE(model, '3', '**')) - LEN(model)) * 3
       + (LEN(REPLACE(model, '4', '**')) - LEN(model)) * 4
       + (LEN(REPLACE(model, '5', '**')) - LEN(model)) * 5
       + (LEN(REPLACE(model, '6', '**')) - LEN(model)) * 6
       + (LEN(REPLACE(model, '7', '**')) - LEN(model)) * 7
       + (LEN(REPLACE(model, '8', '**')) - LEN(model)) * 8
       + (LEN(REPLACE(model, '9', '**')) - LEN(model)) * 9
FROM product
