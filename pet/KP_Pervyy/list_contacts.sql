SELECT
	COALESCE(t1.last_name, '-') AS Фамилия,
	COALESCE(t1.first_name, '-') AS Имя,
	COALESCE(t1.middle_name, '-') AS Отчество,
	COALESCE(t1.phone, '-') AS Телефон,
	t2.plot_no AS Участок
FROM neighbors AS t1
JOIN plot_owners as t2
	ON t1.neighbor_id = t2.neighbor_id