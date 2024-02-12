SELECT
  setting_serv.type,
  COUNT(applications.id_appl) AS num_applications
FROM
  application_storege.applications
JOIN
  application_storege.setting_serv ON applications.id_sevreses = setting_serv.id_sevreses
WHERE
  EXTRACT(YEAR FROM applications.date_start) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY
  setting_serv.type
ORDER BY
  num_applications DESC
LIMIT 1;
