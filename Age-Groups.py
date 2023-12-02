import pandas as ex
import matplotlib.pyplot as plt
df = ex.read_excel(r'/Users/hetuvpatel810/Documents/TMU_Sem_1/SocIs_Ethics_Prof  CPS 412/ChatGPT')
Age_group = df['Select the age group you belong to.']
Gender = df['How do you identify yourself?']
def age_groups():
    count_18_23 = 0
    count_24_30 = 0
    count_30 = 0
    for j in Age_group:
        if j == '18-23':
            count_18_23 += 1 
        elif j == '24-30':
            count_24_30 += 1
        elif j == '30+':
            count_30 += 1
    y_axis = [count_18_23,count_24_30,count_30]
    x_axis = ['18-23','24-30','30+']
    
    plt.bar(x_axis,y_axis)
    plt.title('Age Groups')
    plt.xlabel('Age')
    plt.ylabel('Number of People')
    plt.show()
age_groups()
