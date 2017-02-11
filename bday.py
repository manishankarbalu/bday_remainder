from datetime import datetime, timedelta

def ddmm_from(date):
    str_format = "%d/%m"
    return date.strftime(str_format)


def tmr_ddmm_from(today):
    one_day = timedelta(days=1)
    tomorrow = today + one_day
    return ddmm_from(tomorrow)


def check_birthday(date,name,ddd):
    #name = global people_name
    #ddd=global people_dob
    stoday = ddmm_from(date)
    stomorrow = tmr_ddmm_from(date)

    tomorrow_birth = []
    today_birth = []
    for i in xrange(0,len(ddd)):
        sdmbirth = ddd[i]
        if stoday == sdmbirth:
            today_birth.append(name[i])
        elif stomorrow == sdmbirth:
            tomorrow_birth.append(name[i])

    if tomorrow_birth:
        all_tomorrow = ', '.join(tomorrow_birth)
    return (len(today_birth), len(tomorrow_birth),today_birth,tomorrow_birth)

def printd(tt_b,j):
	if(j):
		st=''
		for i in tt_b:
			st=st+i+','
		st=st[:-1]
		print "People having birthday today is/are:"+st
	else:
		st=''
		for i in tt_b:
			st=st+i+','
		st=st[:-1]
		print "People having birthday tomorrow is/are:"+st

people_name=[]#['shankar','gopal']
people_dob=[]#['12/02','12/02']
today = datetime.today()
stoday = ddmm_from(today)
t_b=[]
tt_b=[]
t1,t2,t_b,tt_b = check_birthday(today,people_name,people_dob)
if(t1!=0):
	printd(t_b,1)
else:
	if(t2!=0):
		printd(tt_b,0)
	else:
		print "Nobirthdays"

