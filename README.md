 # TO DO:
 - add ajax to tamam far3y which depends on tamam asasy selection == done
 - implement (POST) request to  saveing daily tamam data == done
 - filter tamam by date and user == done

 - ## Qwta3 Nadafa algorithm
    - build the distribution algorithm
    - try to modify the process effeciency (memory, process) 
 

select * from accounts_user where id in (SELECT user_id from home_daily_nadafa where id in (SELECT daily_nadafa_id from home_daily_nadafa_qeta3at_nadafa where qeta3_nadafa_id in (SELECT id from home_qeta3_nadafa where weight=4)))