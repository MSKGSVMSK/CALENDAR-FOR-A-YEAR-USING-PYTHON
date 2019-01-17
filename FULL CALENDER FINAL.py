#final stage of calender year program without function

#initialisation

terminate=False
days_in_month=(31,28,31,30,31,30,31,31,30,31,30,31)
month_names=("JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
month_seperator=format(' ','8')
blank_week=format(' ','21')
blank_col=format(' ','3')

#prompt for years until quit

while(not terminate):
    #program greeting
    print("THIS PROGRAM WILL DISPLAY A CALENDER MONTH BETWEEN 1800 AND 2019")

    #get year
    year=int(input("ENTER AN YEAR FROM 1800 TO 2100 \n(ENTER -1 TO QUIT):"))
    while((year<1800 or year>2100) and year!=-1):
        year=int(input("OOPS! INVALID YEAR.TRY AGAIN:"))
    if(year==-1):
        terminate=True
    else:
        #for leap year
        if(year%4==0 and (not(year%100==0)or (year%400==0))):
            leapyear=True
        else:
            leapyear=False

        #day of the week
        century_digit=year//100
        year_digit=year%100
        value=year_digit+(year_digit//4)
        if(century_digit==18):
            value+=2
        elif(century_digit==20):
            value+=6

        #leapyear check

        if not leapyear:
            value+=1

        #first day of the month for jan 1

        first_day_of_current_month=(value+1)%7

        #calender for 12 months

        calender_year=[]
        for month_num in range(12):
            month_name=month_names[month_num]

            #new month init

            current_day=1
            if first_day_of_current_month==0:
                starting_col=7
            else:
                starting_col=first_day_of_current_month
            current_col=1
            calender_week=''
            calender_month=[]

            #add any needed leading space for starting week of the month  
            while current_col < starting_col:
                calender_week+=blank_col
                current_col+=1
                
            if((month_name=="FEBRUARY") and leapyear):
                num_days_in_month=29
            else:
                num_days_in_month=days_in_month[month_num]

            while current_day<=num_days_in_month:
                calender_week+=format(str(current_day),'>3')

                if(current_col==7):
                    calender_month+=[calender_week]
                    calender_week=''
                    current_col=1
                else:
                    current_col+=1
                current_day+=1

            #fill out final row of month with needed blanks

            calender_week+=blank_week[0:(7-current_col+1)*3]
            calender_month+=[calender_week]

            #reset values for next month

            first_day_of_current_month=current_col
            calender_year+=[calender_month]
            calender_month=[]
        #print calender year
        print('\n',year,'\n')

        #each row starts with jan, apr, jul, oct

        for month_num in [0,3,6,9]:
            #display three months in each row 
            for i in range(month_num,month_num+3):
                print(''+format(month_names[i],'19'),month_seperator,end='')

            #display each week on seperate line

            week=0
            lines_to_print=True
            while lines_to_print:
                lines_to_print=False
                #another week to display for 1st mon in row
                for k in range(month_num,month_num+3):
                    if week<len(calender_year[k]):
                        print(calender_year[k][week],end='')
                        lines_to_print=True
                    else:
                        print(blank_week,end='')
                    print(month_seperator,end='')
                #move to next line
                print()

                #increment week
                week+=1
                
