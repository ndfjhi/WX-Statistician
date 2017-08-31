# -*- coding:utf-8 -*-
import itchat
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
print('\n作者：ndfjhi\n版本号：0.0.1')

def getfriend():
    boy=0
    girl=0
    place={'未设置':0}
    friends=itchat.get_friends()
    Userid=friends[0]['NickName']
    for friend in friends:
        if friend['Province'] == '':
            place['未设置'] = place['未设置'] + 1
        elif friend['Province'] in place:
            place['{}'.format(friend['Province'])]=place['{}'.format(friend['Province'])]+1
        else:place['{}'.format(friend['Province'])]=1 #统计各省的人数
        if friend['Sex']==1:boy=boy+1 #统计男女比例
        else:girl=girl+1
    return boy,girl,place,Userid
def picture(boy=0,girl=0,place={},Userid='None'):
    num=boy+girl
    perboy=boy/num*100
    pergirl=girl/num*100

    sexes=[u'男',u'女']
    nums=[boy,girl]
    labels=['{}\n{}人'.format(sex,num)for sex,num in zip(sexes,nums)]
    fracs=[perboy,pergirl]
    explode = [0, 0.05]  # 0.05 凸出这部分，

    fig=plt.figure(num=1,figsize=(18,8))#设置画布大小
    fig.suptitle('{}的好友数据'.format(Userid),fontsize=20,color='g')#设置用户名
    ax=fig.add_subplot(121)
    ax.set_title('男女比例\n总好友数:%d'%(num))
    ax.pie(x=fracs,labels=labels,explode=explode,autopct='%3.1f %%',
           shadow=False,labeldistance=1.1, startangle = 90,pctdistance = 0.6)
    '''
    labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    shadow，饼是否有阴影
    startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    pctdistance，百分比的text离圆心的距离
    patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    '''
    ax=fig.add_subplot(122)
    places=place.keys()
    peoples=place.values()
    ax.set_title('地区分布')
    xticks=range(len(place))#设置x轴每个元素位置
    bar_width=0.6 #定义柱状图每个柱的宽度
    bars=ax.bar(xticks,peoples,width=bar_width,edgecolor='none',color='rcbg',alpha=0.8,align='center')
    # 画柱状图，横轴是地点标签的位置，纵轴是人数，定义柱的宽度，同时设置柱的透明度为0.8
    ax.set_ylabel('人数')
    ax.set_xticks(xticks)# x轴每个标签的具体位置，设置为每个柱的中央
    ax.set_xticklabels(places,fontsize=12,rotation=90)#设置X轴标签
    for xx,yy in zip(xticks,peoples):
        ax.text(xx,yy+0.5,'%d'%(yy),ha='center',va='bottom',fontsize=14)#每根柱上面加数字的
    plt.show()
def main():
    itchat.login()
    boy,girl,place,Userid=getfriend()
    picture(boy,girl,place,Userid)
if __name__=='__main__':
    main()


