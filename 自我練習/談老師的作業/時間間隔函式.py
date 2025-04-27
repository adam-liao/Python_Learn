import time
def format_elaped(start_time,end_time):
    eli_time=end_time-start_time
    if eli_time < 0.1:
        return f'{eli_time:.6f}秒'
    elif eli_time<60:
        return f'{eli_time:.2f}秒'
    elif eli_time<3600:
        minu_time=int(eli_time)//60
        sec_time=int(eli_time)%60
        return f'{minu_time:2d}:{sec_time:2d}'
    elif eli_time<86400:
        minu_time=int(eli_time) //3600
        sec_time=int(eli_time)%3600//60
        return f'{day_time:2d}:{minu_time:2d}:{sec_time:2d}'
    else:
        day_time=int(eli_time)//86400 
        minu_time=int(eli_time)% 86400 //3600
        sec_time=int(eli_time)%3600//60
        return f'{day_time:2d}:{minu_time:2d}:{sec_time:2d}'
        
    

timer=time.time()
timer_end=timer+90

print(format_elaped(timer,timer_end))