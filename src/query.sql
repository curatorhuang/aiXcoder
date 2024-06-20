select first_display_time,
FROM_UNIXTIME(first_display_time/1000) AS formatted_time
from request_delay_v2
where user_name = 'test_user2'
and lang_id = 1
and (status=0 or status=6 or status=-1 and request_duration>0)
order by first_display_time desc limit
39,1









