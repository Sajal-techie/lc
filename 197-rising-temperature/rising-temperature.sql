select cur.id from Weather as cur Where Exists (select 1 from weather as yesterday where cur.temperature > yesterday.temperature and cur.recordDate = yesterday.recordDate +1);