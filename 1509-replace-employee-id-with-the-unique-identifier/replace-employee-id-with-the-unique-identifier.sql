select unique_id, name from Employees as e left join EmployeeUNI as u on u.id=e.id ;